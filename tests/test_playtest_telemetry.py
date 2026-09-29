import asyncio
import importlib.util
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
MCP_DIR = ROOT / "mcp"
FIXTURES = Path(__file__).parent / "fixtures"


def load_telemetry(test_case):
    module_path = MCP_DIR / "telemetry.py"
    if not module_path.exists():
        test_case.fail(
            "Missing mcp/telemetry.py: longitudinal playtest telemetry is not implemented"
        )
    spec = importlib.util.spec_from_file_location("sts2_telemetry", module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_server():
    server_path = MCP_DIR / "server.py"
    spec = importlib.util.spec_from_file_location("sts2_mcp_server", server_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TelemetryContractTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp_dir.cleanup)
        self.work_dir = Path(self.temp_dir.name)
        self.history_dir = self.work_dir / "history"
        shutil.copytree(FIXTURES / "runs", self.history_dir)
        self.ledger_path = self.work_dir / "telemetry.jsonl"

    def ingest_standard_runs(self):
        telemetry = load_telemetry(self)
        telemetry.ingest_runs(
            history_path=self.history_dir,
            ledger_path=self.ledger_path,
            profile_id=1,
            save_scope="modded",
            metadata={
                "mod_version": "1.2.0",
                "mcp_version": "0.1.0",
                "report_path": "playtests/report.md",
            },
        )
        return telemetry

    def read_records(self):
        return [
            json.loads(line)
            for line in self.ledger_path.read_text(encoding="utf-8").splitlines()
        ]

    def test_ingestion_normalizes_real_run_shape_and_is_idempotent(self):
        telemetry = self.ingest_standard_runs()
        first_records = self.read_records()

        telemetry.ingest_runs(
            history_path=self.history_dir,
            ledger_path=self.ledger_path,
            profile_id=1,
            save_scope="modded",
        )

        self.assertEqual(first_records, self.read_records())
        self.assertEqual(3, len(first_records))
        win = next(record for record in first_records if record["start_time"] == 1000)
        self.assertEqual("modded:profile1:1000", win["run_id"])
        self.assertEqual("v0.100.0", win["build_id"])
        self.assertEqual("CHARACTER.CYCLOPS", win["character_id"])
        self.assertEqual(2, win["ascension"])
        self.assertTrue(win["win"])
        self.assertFalse(win["was_abandoned"])
        self.assertEqual("victory", win["terminal_cause"])
        self.assertEqual(["CARD.HEAVY_BLOW", "CARD.GUARD"], win["final_deck"])
        self.assertEqual(
            [
                {"card_id": "CARD.HEAVY_BLOW", "was_picked": True},
                {"card_id": "CARD.BATTLE_TRANCE", "was_picked": False},
            ],
            win["card_choices"],
        )
        self.assertTrue(win["eligible"])
        self.assertEqual("eligible", win["eligibility_status"])
        self.assertEqual("1.2.0", win["mod_version"])
        self.assertEqual("0.1.0", win["mcp_version"])
        self.assertEqual("playtests/report.md", win["report_path"])

        abandoned = next(
            record for record in first_records if record["was_abandoned"]
        )
        self.assertFalse(abandoned["eligible"])
        self.assertEqual("abandoned", abandoned["eligibility_status"])
        self.assertNotEqual("development_test", abandoned["eligibility_status"])

        loss = next(record for record in first_records if record["start_time"] == 2000)
        self.assertEqual("ENCOUNTER.THE_INSATIABLE_BOSS", loss["terminal_cause"])

        unknown_ledger = self.work_dir / "unknown-metadata.jsonl"
        telemetry.ingest_runs(
            history_path=self.history_dir,
            ledger_path=unknown_ledger,
            profile_id=2,
            save_scope="vanilla",
        )
        unknown_record = json.loads(
            unknown_ledger.read_text(encoding="utf-8").splitlines()[0]
        )
        self.assertEqual("unknown", unknown_record["mod_version"])
        self.assertEqual("unknown", unknown_record["mcp_version"])
        self.assertIn("report_path", unknown_record)

    def test_existing_run_id_is_immutable_when_source_file_changes(self):
        telemetry = self.ingest_standard_runs()
        original_lines = self.ledger_path.read_text(encoding="utf-8")
        source_path = self.history_dir / "1000.run"
        changed = json.loads(source_path.read_text(encoding="utf-8"))
        changed["win"] = False
        source_path.write_text(json.dumps(changed), encoding="utf-8")

        telemetry.ingest_runs(
            history_path=self.history_dir,
            ledger_path=self.ledger_path,
            profile_id=1,
            save_scope="modded",
        )

        self.assertEqual(original_lines, self.ledger_path.read_text(encoding="utf-8"))

    def test_aggregate_reports_eligibility_cards_rates_and_wilson_intervals(self):
        telemetry = self.ingest_standard_runs()
        telemetry.ingest_runs(
            history_path=FIXTURES / "development",
            ledger_path=self.ledger_path,
            profile_id=1,
            save_scope="modded",
            metadata={
                "development_test": True,
                "mod_version": "dev",
                "mcp_version": "0.1.0-dev",
                "report_path": "playtests/dev-report.md",
            },
        )

        metrics = telemetry.aggregate_metrics(self.ledger_path)

        self.assertEqual(4, metrics["total_records"])
        self.assertEqual(2, metrics["eligible_runs"])
        self.assertEqual(1, metrics["wins"])
        self.assertEqual(1, metrics["losses"])
        self.assertEqual(1, metrics["abandoned_runs"])
        self.assertEqual(1, metrics["development_test_runs"])
        self.assertEqual(1, metrics["win_rate"]["numerator"])
        self.assertEqual(2, metrics["win_rate"]["denominator"])
        self.assertEqual(0.5, metrics["win_rate"]["rate"])
        self.assertAlmostEqual(
            0.0945, metrics["win_rate"]["wilson_95"]["lower"], places=4
        )
        self.assertAlmostEqual(
            0.9055, metrics["win_rate"]["wilson_95"]["upper"], places=4
        )

        heavy_blow = metrics["cards"]["CARD.HEAVY_BLOW"]
        self.assertEqual(2, heavy_blow["offers"])
        self.assertEqual(1, heavy_blow["picks"])
        self.assertEqual(1, heavy_blow["skips"])
        self.assertEqual(
            {"numerator": 1, "denominator": 2, "rate": 0.5},
            {
                key: heavy_blow["pick_rate"][key]
                for key in ("numerator", "denominator", "rate")
            },
        )
        self.assertIsNotNone(heavy_blow["pick_rate"]["wilson_95"])
        self.assertEqual(1, heavy_blow["final_deck_eligible_wins"])
        self.assertEqual(0, heavy_blow["final_deck_eligible_losses"])
        self.assertEqual(1.0, heavy_blow["presence_win_rate"]["rate"])
        self.assertIsNotNone(heavy_blow["presence_win_rate"]["wilson_95"])
        self.assertNotIn("None", metrics["cards"])

    def test_wilson_intervals_clamp_probability_boundaries(self):
        telemetry = load_telemetry(self)

        boundary_cases = (
            (0, 20, "lower", 0.0),
            (20, 20, "upper", 1.0),
        )
        for successes, trials, bound, expected in boundary_cases:
            with self.subTest(successes=successes, trials=trials, bound=bound):
                interval = telemetry._wilson_95(successes, trials)
                self.assertEqual(expected, interval[bound])

    def test_filters_cohorts_and_zero_denominator_rates(self):
        telemetry = self.ingest_standard_runs()
        telemetry.ingest_runs(
            history_path=FIXTURES / "development",
            ledger_path=self.ledger_path,
            profile_id=1,
            save_scope="modded",
            metadata={"development_test": True, "mod_version": "dev"},
        )

        filtered = telemetry.aggregate_metrics(
            self.ledger_path,
            character="CHARACTER.CYCLOPS",
            game_build="v0.100.0",
            mod_version="1.2.0",
            ascension=2,
            start_time_min=1500,
            start_time_max=2500,
        )
        self.assertEqual(1, filtered["total_records"])
        self.assertEqual(1, filtered["losses"])

        all_metrics = telemetry.aggregate_metrics(self.ledger_path)
        self.assertEqual(
            {"v0.100.0", "v0.101.0"}, set(all_metrics["cohorts"]["game_build"])
        )
        self.assertEqual(
            {"1.2.0", "dev"}, set(all_metrics["cohorts"]["mod_version"])
        )
        self.assertEqual(
            2, all_metrics["cohorts"]["game_build"]["v0.100.0"]["total_records"]
        )
        self.assertEqual(
            1, all_metrics["cohorts"]["mod_version"]["dev"]["total_records"]
        )

        no_eligible = telemetry.aggregate_metrics(
            self.ledger_path, character="CHARACTER.IRONCLAD"
        )
        self.assertIsNone(no_eligible["win_rate"]["rate"])
        self.assertIsNone(no_eligible["win_rate"]["wilson_95"])
        self.assertIsNone(
            no_eligible["cards"]["CARD.ANGER"]["presence_win_rate"]["rate"]
        )


class FastMcpTelemetryBoundaryTests(unittest.TestCase):
    def test_get_playtest_metrics_dispatches_through_fastmcp_registry(self):
        server = load_server()

        registered_tools = {
            tool.name for tool in server.mcp._tool_manager.list_tools()
        }
        self.assertIn("get_playtest_metrics", registered_tools)

        with tempfile.TemporaryDirectory() as temp_dir:
            history_path = Path(temp_dir) / "history"
            shutil.copytree(FIXTURES / "runs", history_path)
            ledger_path = Path(temp_dir) / "ledger.jsonl"
            compendium = {
                "profile_id": 1,
                "current_run": None,
                "sections": {
                    "run_history": {
                        "history_path": str(history_path),
                        "entries": [
                            {"run_id": "modded:profile1:3000", "start_time": 3000}
                        ],
                    }
                },
            }
            arguments = {
                "ledger_path": str(ledger_path),
                "character": "CHARACTER.CYCLOPS",
                "game_build": "v0.100.0",
                "mod_version": "1.2.0",
                "ascension": 2,
                "start_time_min": 1000,
                "start_time_max": 2000,
                "mcp_version": "0.1.0",
                "report_path": "playtests/report.md",
                "development_test": False,
            }

            with mock.patch.object(
                server,
                "_compendium_get",
                new=mock.AsyncMock(return_value=json.dumps(compendium)),
            ) as compendium_get:
                result_text = asyncio.run(
                    server.mcp._tool_manager.call_tool(
                        "get_playtest_metrics", arguments
                    )
                )

            compendium_get.assert_awaited_once_with()
            records = [
                json.loads(line)
                for line in ledger_path.read_text(encoding="utf-8").splitlines()
            ]
            self.assertEqual(3, len(records))
            self.assertEqual(
                {"modded:profile1:1000", "modded:profile1:2000", "modded:profile1:3000"},
                {record["run_id"] for record in records},
            )
            self.assertTrue(
                all(record["mod_version"] == arguments["mod_version"] for record in records)
            )
            self.assertTrue(
                all(record["mcp_version"] == arguments["mcp_version"] for record in records)
            )
            self.assertTrue(
                all(record["report_path"] == arguments["report_path"] for record in records)
            )
            self.assertTrue(
                all(
                    record["development_test"] == arguments["development_test"]
                    for record in records
                )
            )

            result = json.loads(result_text)
            self.assertEqual(str(ledger_path), result["ledger_path"])
            self.assertEqual(2, result["total_records"])
            self.assertEqual(2, result["eligible_runs"])
            self.assertEqual(1, result["wins"])
            self.assertEqual(1, result["losses"])
            self.assertEqual(1, result["win_rate"]["numerator"])
            self.assertEqual(2, result["win_rate"]["denominator"])
            self.assertEqual(0.5, result["win_rate"]["rate"])

    def test_get_playtest_metrics_uses_compendium_history_and_forwards_filters(self):
        server = load_server()
        if not hasattr(server, "get_playtest_metrics"):
            self.fail(
                "Missing mcp/server.py:get_playtest_metrics async FastMCP telemetry boundary"
            )

        with tempfile.TemporaryDirectory() as temp_dir:
            history_path = Path(temp_dir) / "history"
            shutil.copytree(FIXTURES / "runs", history_path)
            ledger_path = Path(temp_dir) / "ledger.jsonl"
            compendium = {
                "profile_id": 1,
                "current_run": None,
                "sections": {
                    "run_history": {
                        "history_path": str(history_path),
                        "entries": [
                            {"run_id": "modded:profile1:3000", "start_time": 3000}
                        ],
                    }
                },
            }

            with mock.patch.object(
                server,
                "_compendium_get",
                new=mock.AsyncMock(return_value=json.dumps(compendium)),
            ) as compendium_get:
                result_text = asyncio.run(
                    server.get_playtest_metrics(
                        ledger_path=str(ledger_path),
                        character="CHARACTER.CYCLOPS",
                        game_build="v0.100.0",
                        mod_version="1.2.0",
                        ascension=2,
                        start_time_min=1000,
                        start_time_max=2000,
                        mcp_version="0.1.0",
                        report_path="playtests/report.md",
                    )
                )

            compendium_get.assert_awaited_once_with()
            result = json.loads(result_text)
            self.assertEqual(2, result["total_records"])
            self.assertEqual(1, result["wins"])
            self.assertEqual(1, result["losses"])

    def test_get_playtest_metrics_returns_handle_error_style(self):
        server = load_server()
        if not hasattr(server, "get_playtest_metrics"):
            self.fail(
                "Missing mcp/server.py:get_playtest_metrics async FastMCP telemetry boundary"
            )

        with mock.patch.object(
            server,
            "_compendium_get",
            new=mock.AsyncMock(side_effect=RuntimeError("compendium unavailable")),
        ), mock.patch.object(
            server, "_handle_error", wraps=server._handle_error
        ) as handle_error:
            result = asyncio.run(server.get_playtest_metrics(ledger_path="unused.jsonl"))

        self.assertEqual("Error: compendium unavailable", result)
        handle_error.assert_called_once()
        self.assertIsInstance(handle_error.call_args.args[0], RuntimeError)
        self.assertEqual("compendium unavailable", str(handle_error.call_args.args[0]))


if __name__ == "__main__":
    unittest.main()