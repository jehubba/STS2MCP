# Multiplayer Operational Readiness

Status legend: `[ ]` not started, `[~]` in progress, `[x]` complete, `[!]` blocked.

## Milestone 1: Two independently controllable players

- [x] Support a per-process HTTP port override for the STS2 MCP mod.
- [x] Preserve `STS2_MCP.conf` as the fallback when no override is supplied.
- [x] Add automated coverage for override precedence and invalid overrides.
- [x] Register `sts2-host` on port `15526` in `.vscode/mcp.json`.
- [x] Register `sts2-client` on port `15527` in `.vscode/mcp.json`.
- [x] Document how to start the host and client with distinct API ports.
- [x] Prove FastMP can connect two local game processes through `127.0.0.1:33771`.
- [x] Confirm the endpoints report different `local_player_slot` values.
- [x] Complete one manually supervised two-client combat.

### Windows FastMP runbook

FastMP is the game's local debug multiplayer path. It uses ENet on
`127.0.0.1:33771` rather than Steam networking, but the host must still be
started through Steam so Steamworks initializes and Workshop dependencies load.
The argument-bearing URI below is the launch-option form of the installed Steam
shortcut (`steam://rungameid/2868840`):

```powershell
Start-Process "steam://run/2868840//--fastmp%3Dhost_standard%20--clientId%3D1%20--sts2-mcp-port%3D15526/"
```

Steam permits only one instance of an app, so launch the client directly with
Steam initialization explicitly disabled. A Steam-disabled process cannot
discover Workshop mods. If a gameplay mod depends on Workshop content, expose
that dependency in the normal mods directory while the client starts. For the
current Cyclops setup, BaseLib is Workshop item `3737335127`:

```powershell
$game = "D:\SteamLibrary\steamapps\common\Slay the Spire 2\SlayTheSpire2.exe"
$baseLib = "D:\SteamLibrary\steamapps\workshop\content\2868840\3737335127"
$baseLibLink = "D:\SteamLibrary\steamapps\common\Slay the Spire 2\mods\BaseLib-fastmp"

New-Item -ItemType Junction -Path $baseLibLink -Target $baseLib
Start-Process $game -WorkingDirectory (Split-Path $game) `
	-ArgumentList "--fastmp=join", "--clientId=1000", `
		"--sts2-mcp-port=15527", "--force-steam=off"

# Remove the junction after the client has loaded and port 15527 responds.
(Get-Item $baseLibLink).Delete()
```

On the first launch for a new `clientId`, acknowledge the game's mod-loading
warning and any first-run prompts. If that warning interrupted the automatic
join, back out to the multiplayer menu and select Join again.

After both processes are connected, restart or reload the workspace MCP servers
so `sts2-host` targets port `15526` and `sts2-client` targets port `15527`.
Do not begin autonomous play until both `mp_get_game_state` responses identify
different `local_player_slot` values in the same run.

Milestone 1 exit criteria:

- Both API endpoints respond independently.
- Each endpoint controls a different local player in the same co-op run.
- One player's end-turn submission waits and the second advances the round.
- A map vote and post-combat reward flow complete for both players.

### Milestone 1 smoke evidence (2026-09-08)

- Steam-shortcut host PID `41520` listened on MCP port `15526` and ENet port
  `33771`; local client PID `40020` listened on MCP port `15527`.
- Both endpoints reported two players in the same run. Host player ID `1` was
  local slot `0`; client player ID `1000` was local slot `1`.
- Both players saw the same four opening Monster map nodes and voted for node
  `(0,1)`.
- On combat round 1, the host end-turn submission waited with only slot `0`
  ready. The client submission advanced both players to round 2 at `72` HP and
  reset both ready flags.
- Both endpoints agreed on shared enemy HP after card plays. The Sludge Spinner
  combat completed on round 4, and both endpoints transitioned to their own
  rewards screens.
- A temporary BaseLib junction was removed after client startup, and both game
  processes were stopped after the smoke test.

## Milestone 2: Agent isolation

- [ ] Define a host-player agent with access only to `sts2-host` tools.
- [ ] Define a client-player agent with access only to `sts2-client` tools.
- [ ] Give both agents the gameplay guidance from `AGENTS.md` and `GUIDE.md`.
- [ ] Verify neither agent can invoke the other player's action tools.

## Milestone 3: Coordination and recovery

- [ ] Add a coordinator that dispatches both player agents.
- [ ] Treat native STS2 multiplayer synchronization as authoritative.
- [ ] Correlate both endpoints by run, room, round, and enemy state.
- [ ] Coordinate end-turn submissions, map votes, and shared choices.
- [ ] Detect inactivity, endpoint failure, disagreement, and disconnects.
- [ ] Support end-turn vote retraction when replanning is required.

## Milestone 4: Integration validation

- [x] Exercise two real game instances rather than substitute HTTP responses.
- [~] Verify independent hands, card plays, potions, and rewards (potions remain untested).
- [ ] Verify shared combat, map, event, and treasure synchronization.
- [ ] Record diagnostics from both clients for any divergence.
- [ ] Add an immutable multiplayer playtest report under `playtests/runs/`.

## Milestone 5: Bug reproduction

- [ ] Define the smallest deterministic scenario for the target multiplayer bug.
- [ ] Capture both clients' state immediately before and after reproduction.
- [ ] Reproduce the failure without the fix when feasible.
- [ ] Verify the fix from both local-player perspectives.
- [ ] Retain the run report, mod logs, and relevant exception output.

## Operational readiness gate

- [~] Two MCP namespaces consistently map to two different local players (one live run verified).
- [x] A complete combat runs without manual repair.
- [x] Voting cannot deadlock silently.
- [ ] Disconnects produce a visible bounded failure.
- [ ] The target bug scenario passes from both player perspectives.
