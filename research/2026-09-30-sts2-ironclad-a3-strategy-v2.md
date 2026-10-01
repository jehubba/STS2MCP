---
task_id: 06ff8f1b-d50f-4bec-a1e0-270b61dce683
agent: research
status: complete
timestamp: 2026-09-30T00:11:58-07:00
topic: Slay the Spire 2 Ironclad Ascension 3 strategy for v0.107.1 (redo with hardened source-citation rules)
depth: deep
output_file: C:\Users\Jeffrey\source\repos\sts2-mcp\STS2MCP\research\2026-09-30-sts2-ironclad-a3-strategy-v2.md
---

# Research Report: Slay the Spire 2 Ironclad A3 Strategy (v0.107.1) — Citation-Hardened Redo

## Why This Redo Exists

This report replaces `2026-09-29-sts2-ironclad-a3-strategy.md`. That report's Sources list
included `steamcommunity.com/app/2868840/guides/?searchText=Ironclad&browsefilter=trend&...`
on equal numbered footing with genuinely productive sources. A human reviewer manually
re-fetched that URL and found that a plain, non-JS fetch returns Steam's generic/unfiltered
guide index rather than real Ironclad-filtered results — this read as suspicious/fabricated
citation practice even though the load-bearing game-mechanic facts in that report were
independently correct. This run applies five additional mandatory rules (see task prompt)
on top of the standard pipeline: only list directly-fetched, substantively-confirmed URLs
as numbered Sources; flag JS-dependent listing pages before citing them; attach a citation
identifier immediately next to every specific mechanic claim with verbatim-vs-paraphrase
tagging; separate session-verified facts from background knowledge; and add an explicit
Citation Integrity pass to Self-Evaluation.

**Retrieval note on the disputed URL, this session:** a real-browser (JS-enabled) fetch of
the same guide-search URL this session actually did filter correctly (3 of 3 results vs. 16
of 16 with the search parameter removed) — see `[ATTEMPTED-1]` below. This does not
contradict the human reviewer's finding; it is consistent with it. The reviewer's manual
re-fetch was almost certainly a plain HTTP GET (no JS execution), which is exactly the
condition rule 2 of the hardened citation rules addresses: Steam's guide search is
client-side/JS-dependent, and different retrieval methods against the identical URL can
return different content. Because the retrieval tool available in *this* session executes
real browser JS, I cannot independently confirm the plain-fetch behavior myself this
session — I am relying on the task prompt's own stated finding (an authoritative
instruction from the dispatching task, not untrusted web content) for that specific claim.
Regardless of the filtering dispute, none of the three results returned are substantively
about Ironclad Ascension 3 strategy (see `[ATTEMPTED-1]`), so the URL is excluded from
numbered Sources on non-substance grounds independent of the JS question.

## Research Scope

Depth: **deep** — Act 1/3 encounter mechanics were previously unverifiable from a public
wiki (401 error) and had no confirmed community guide; this redo also carries strict
citation-integrity obligations that require exhaustive per-claim sourcing rather than a
quick pass.

Sub-questions (unchanged from the prior run, per task instruction):

1. Which verified Ironclad cards, relics, and potions matter strategically on `v0.107.1`?
2. What is known about Act 1 threats, particularly the named encounters?
3. What drafting, shop, upgrade, removal, skip, and map rules follow from the evidence?
4. What turn-by-turn combat controller avoids static card scores?
5. What should change after runs `1790695747` and `1790731181`?

Stopping condition: enough directly-fetched-and-confirmed primary evidence to reproduce
every specific mechanic claim in the prior report with an adjacent citation identifier, or
to explicitly demote unconfirmable claims to "background knowledge — not independently
verified this session" / open verification gaps.

**Retrieval budget log** (deep-mode override of the default 10-source/4-minute
front-stops, per the pipeline's own configurable-threshold rule — this task genuinely
requires more depth than the default quick-synthesis trigger allows, given the explicit
citation-integrity mandate):

- Budget: sources 5/~15 (override) | domains 3/20 | files 6/50 | size well under 20MB
- `[SYNTHESIS TRIGGER]`: further `slaythespire.wiki.gg` card/monster subpages became
  unavailable mid-session (see below) — retrieval stopped and synthesis began once no
  further productive fetches were reachable within this session, not because a numeric
  budget alone forced it.

## Evidence by Sub-question

### 1. Verified Ironclad cards, relics, and potions on `v0.107.1`

**Build boundary [S1, verbatim].** The patch note fetched directly this session is
titled "Slay the Spire 2 - Major Update #2 - v0.107.1 - Steam News," posted "Thu, June 18,
2026 @5:41 PM PDT" on the page itself (equivalent to 2026-06-19 00:41 UTC per the matching
RSS `pubDate`, confirmed via `[S2, verbatim]`). Opening line, verbatim: *"Hey Slayers, our
second major main branch update is here with 4 patches in 1 (not including hotfixes)!"*
`[S1]`

**Cards confirmed changed exactly at v0.107.1, verbatim from S1 (these are the new,
current-as-of-v0.107.1 texts, not inferred):**

- Conflagration — *"Reworked Conflagration card: now deals 2 damage to ALL enemies 4(5)
  times (was: 8(9) AOE damage plus 2(3) per other Attack played this turn)"* `[S1,
  verbatim]`. Both the pre- and post-patch text are given directly in the same sentence.
- Drum of Battle — *"Reworked Drum of Battle card: now a 1-cost Uncommon Skill that draws
  2 cards and grants 2(3) Energy when Exhausted (the Energy gain respects Replay and
  card-duplication effects like Duplicator potion)"* `[S1, verbatim]`. This matches
  `playtests/IRONCLAD.md`'s existing entry ("Draw 2; when exhausted, gain 2 energy")
  `[S8, paraphrase-match]` — the IRONCLAD.md wording is a paraphrase of the same fact, not
  a second independent source.
- Howl From Beyond — *"Buffed Howl From Beyond card: trigger moved from start of turn ->
  end of turn"* `[S1, verbatim]`.
- Entrench — *"Buffed Entrench card: can now gain extra Block from enchantments like
  Nimble"* `[S1, verbatim]`.
- Unrelenting — *"Buffed Unrelenting card: damage increased from 12(18) -> 14(20)"` `[S1,
  verbatim]` — 14(20) is the current v0.107.1 value.
- Hellraiser (bug fix, not balance) — *"To avoid infinite-loop softlocks, Hellraiser power
  now plays only 9 cards per turn when all enemies have infinite HP, and properly plays
  'Strike' cards against infinite-HP enemies"* `[S1, verbatim]`. This confirms Hellraiser
  auto-plays Strike-tagged cards as of v0.107.1, but S1 does not give Hellraiser's energy
  cost or full rules text — that portion remains unverified this session (see Facts to
  Verify).

**Cards whose v0.107.1 value is *inferred* from a later beta patch's stated "before" value
(explicitly flagged as inference, per rule 3):** Steam's beta patch notes give both
pre-change and post-change numbers in "X → Y" format. Where a card is not mentioned in any
patch between v0.107.1 and the beta patch in question, the "before" (left-hand) number is
the value that was live at v0.107.1.

- Setup Strike — v0.108.0 beta note, verbatim: *"Buffed Setup Strike: Strength gain
  increased from 2(3) → 3(4)"* `[S2, verbatim; v0.107.1 value of 2(3) Strength is
  INFERRED from the stated "before" number, not directly stated as a v0.107.1 fact]`. This
  matches `playtests/IRONCLAD.md`'s "gain 2 Strength this turn" `[S8, paraphrase-match]`.
- Crimson Mantle — v0.108.0 beta note, verbatim: *"Nerfed Crimson Mantle card: Block gain
  decreased from 8(10) → 7(10)"* `[S2, verbatim; v0.107.1 value of 8(10) Block is
  INFERRED]`. `playtests/IRONCLAD.md` currently says "gain 8 Block" `[S8,
  paraphrase-match]` — consistent with the inferred v0.107.1 value.
- Taunt — v0.109.0 beta note, verbatim: *"Changed Taunt card: Block gain decreased from
  7(8) -> 6(7); Rarity decreased from Uncommon -> Common"* `[S2, verbatim; v0.107.1 value
  of 7(8) Block, Uncommon rarity is INFERRED, since Taunt is not mentioned in the
  intervening v0.108.0 note]`. This does NOT confirm or deny the "apply 1 Vulnerable"
  clause in `playtests/IRONCLAD.md`'s Taunt entry `[S8]` — patch notes give only the
  numeric delta, not full card text, so that clause remains unverified this session.
- Bloodletting — v0.109.0 beta note, verbatim: *"Changed Bloodletting card: rarity
  increased from Common -> Uncommon"* `[S2, verbatim]`. Confirms Bloodletting existed as
  Common rarity at v0.107.1; gives no confirmation of its HP/Energy numbers.
- Demon Form — v0.109.0 beta note, verbatim: *"Buffed Demon Form card: Strength gain
  increased from 2(3) -> 3(4)"* `[S2, verbatim; v0.107.1 value of 2(3) INFERRED]`.
- Rampage — v0.111.0 beta note, verbatim: *"Buffed Rampage card: Base damage increased
  from 9 → 10; Scaling damage from 5(9) → 5(10)"* `[S2, verbatim; v0.107.1 values of base
  9 damage / 5(9) scaling INFERRED, since Rampage is not mentioned in v0.108.0-v0.110.0]`.
  This matches `playtests/IRONCLAD.md`'s "deal 9; gain 5 damage this combat" `[S8,
  paraphrase-match]`.
- Colossus — v0.108.0 beta note, verbatim: *"Nerfed Colossus card: Block gain increased
  from 5(8) → 4(7)"* `[S2, verbatim; v0.107.1 value of 5(8) INFERRED]`. (Note: the patch
  note's own wording labels a numeric decrease as "increased," which is either a
  Mega Crit copy-paste error in the source text or an inverted before/after ordering; flagged
  here as a direct quoting-integrity issue rather than silently corrected.)
- Mangle — v0.110.0 beta note, verbatim: *"Buffed Mangle card: damage increased from 15(20)
  -> 20(26)"* `[S2, verbatim; v0.107.1-through-v0.109.0 value of 15(20) INFERRED]`.
- Pact's End — v0.110.0 beta note, verbatim: *"Buffed Pact's End card: damage increased
  from 17(23) -> 18(24)"* `[S2, verbatim; INFERRED v0.107.1 value 17(23)]`.
- Expect a Fight — reworked entirely in v0.111.0; the v0.111.0 note gives its
  *pre-rework* full text verbatim: *"Uncommon - Skill - Cost 2(1) - 'Gain 1 Energy for each
  Attack in your Hand. You cannot gain additional Energy this turn.'"* `[S2, verbatim; this
  is the actual v0.107.1-era full card text, directly quoted, not inferred, since S2
  states it as the "from" side of a rework]`. A separate v0.109.0 note also buffed it
  first: *"Buffed Expect a Fight card: no longer says 'You cannot gain additional [E] this
  turn.'"* `[S2, verbatim]` — meaning the "cannot gain additional Energy" clause was
  removed in v0.109.0 and therefore WAS present at v0.107.1, consistent with the v0.111.0
  rework quote.
- Forgotten Ritual — v0.111.0 beta note, verbatim: *"Buffed Forgotten Ritual card: no
  longer requires a card to be Exhausted to gain Energy"* `[S2, verbatim]` — confirms that
  at v0.107.1 (through v0.110.0) Forgotten Ritual DID require an Exhaust trigger to gain
  Energy, an inferred-by-negation fact, not directly stated as a positive v0.107.1
  description.

**Relics, verbatim from S1 (current-as-of-v0.107.1 texts):**

- *"Buffed Neow's Booming Conch relic: in addition to drawing extra cards, now gains 1
  Energy at the start of Elite combats"* `[S1, verbatim]`. Matches `playtests/IRONCLAD.md`
  `[S8, paraphrase-match]`.
- *"Buffed Tezcatara's Nutritious Soup relic: in addition to making your Strikes cost 0 and
  giving them Eternal, now makes all your Strikes deal 3 additional damage"* `[S1,
  verbatim]`. Matches the prior report's Strike-package description `[S8,
  paraphrase-match]`.
- Orichalcum, Ornamental Fan, Arcane Scroll, Ruined Helmet, Sturdy Clamp, Razor Tooth,
  Throwing Axe: **not found** in either S1 or the S2 beta-patch quotes retrieved this
  session. Their exact text in `playtests/IRONCLAD.md` `[S8]` is therefore **not
  independently verified this session against any official source** — it derives from
  IRONCLAD.md's own header claim of prior local-wiki verification ("Exact card and relic
  text below was verified against the active profile's local `/api/v1/wiki` registry on
  2026-09-29" `[S8, verbatim, file header]`), which this session could not re-run (no live
  game/MCP tool access in this session's toolset). Treat as **carried-forward local
  evidence, not re-verified this session** — flagged explicitly rather than silently
  presented as freshly confirmed.

**Bestiary feature, verbatim [S1]:** *"Casey here! This patch brings in the Bestiary, which
Beta testers will already be familiar with... Currently, players can find a list of
monsters they've encountered here as well as their moves and animations."* and *"The
Bestiary is now available in the Compendium"* `[S1, verbatim]`. This confirms `mcp/README.md`'s
description of `get_compendium()` grouping into a `bestiary` section is consistent with the
official feature name `[S9, paraphrase-match]`.

**Potions (Flex, Liquid Bronze, Swift, Stable Serum):** not mentioned in S1 or the S2
excerpts retrieved this session, and the follow-up `slaythespire.wiki.gg` potion-page
fetches could not complete before the site began serving an interactive Cloudflare
Turnstile challenge mid-session (see Missing Perspectives). Their exact effect text is
**not independently verified this session** by any fetched source. The usage heuristics
attributed to them in `AGENTS.md` `[S7]` and `playtests/IRONCLAD.md` `[S8]` are local
project policy derived from run observations, not confirmed mechanic text — this
distinction is preserved throughout this report rather than collapsed.

**Version-mismatch caveat, verbatim [S10]:** the mod's own top-level `README.md`, read
directly this session, states: *"Tested against STS2 `v0.103.2`."* `[S10, verbatim]`. This
is an earlier build than `v0.107.1`, the build this report and the two supplied local runs
target. This is a real, load-bearing gap: the mod's documented compatibility testing
predates the build this strategy report is written for. It does not invalidate the local
runs (their own run-context tables independently state `v0.107.1` `[S5, S6, verbatim]`),
but it means the MCP tool-calling mechanics described in `mcp/README.md` and `AGENTS.md`
have not been confirmed re-tested against `v0.107.1` in any source available this session.

**Starting kit, cross-confirmed by two independent directly-fetched sources:**

- `slaythespire.wiki.gg`, verbatim: *"He starts with 80 Max HP, the highest of any
  character. At Ascension 2 and above he starts with 64 HP."* and starting deck *"Strike
  x5", "Defend x4", "Bash x1"* and starting relic *"Burning Blood - Heal for 6 HP at the
  end of combat. Can be replaced by Black Blood."* `[S4, verbatim]`.
- Both local run files independently state the same starter deck and Burning Blood as
  starting relic `[S5, S6, verbatim, run-context/final-state tables]`.
- Note: `[S4]`'s Burning Blood heal amount (6 HP) matches `AGENTS.md`'s existing claim `[S7,
  paraphrase-match]`, and is now cross-confirmed by an external wiki source directly
  fetched this session, not solely by local files — this is a genuine improvement in
  source diversity over the prior report, which could not access this wiki at all
  (previously logged as a `401`).

**Card pool scope, verbatim [S4]:** *"There are a total of 80 regular cards in the
Ironclad's card pool"* with *"Common Cards x20", "Uncommon Cards x35", "Rare Cards x25"*,
plus *"When playing Multiplayer, five additional cards are added to his card pool"* `[S4,
verbatim]`. This confirms the strategic pool discussed in this report and the prior one is
a subset of a materially larger 80-card pool — reinforcing the existing "strategically
important pool, not a complete catalog" framing from the prior report.

### 2. Act 1 encounters and A3 responses

**Fossil Stalker.** S1 gives a verbatim, but explicitly multiplayer-scoped, mechanic
change: *"Changed Fossil Stalker: in multiplayer, now gains a set amount of Strength if it
hits any player instead of gaining Strength for each player hit."* `[S1, verbatim]`. This
confirms a Strength-on-hit mechanic exists for Fossil Stalker, but the quoted sentence is
about a multiplayer-specific per-player-hit rule being changed — it does not directly state
the singleplayer trigger condition or magnitude. The singleplayer Strength-on-unblocked-hit
behavior used operationally in `AGENTS.md` `[S7, verbatim: "Against Fossil Stalker,
unblocked hits trigger its Strength scaling."]` and observed in run `1790695747` `[S5]` is
**local-observation evidence, not independently confirmed by official patch text this
session** — flagged explicitly, where the prior report conflated the MP note with a general
SP confirmation.

**Bygone Effigy.** Not mentioned anywhere in the S1 or S2 text retrieved this session, and
its dedicated wiki.gg page could not be fetched before the Cloudflare block (see Missing
Perspectives). All evidence is local-run observation: *"Bygone Effigy dealt 67 damage in
eight turns. The agent repeatedly spent energy on Block while the elite attacked for 23,
did not establish a damage race, and died with Stable Serum unused."* `[S6, verbatim, run
`1790731181` evidence table]`. No official or wiki source confirms its HP, full move table,
or whether 23-damage attacks are typical/scripted vs. one observed instance.

**Living Fog.** S1 verbatim, but cosmetic only: *"Fixed Living Fog missing its smoke, and
corrected its encounter name in the death quote."* `[S1, verbatim]` — confirms the
encounter exists and had a cosmetic bug at v0.107.1, but says nothing about its damage
mechanics. The 33-damage-over-eight-turns figure is local-run-only evidence `[S5, verbatim,
E02]`.

**Gremlin Merc.** S1 verbatim: *"During the Gremlin Merc fight, if Gremlin Merc didn't
steal any gold but Fat Gremlin escaped, you now receive 50% of the normal gold reward
instead of 0%."* `[S1, verbatim]` — a reward-mechanic confirmation, not a damage-mechanic
one. The 22-damage-over-eleven-turns figure is local-run-only evidence `[S5, verbatim,
E04]`.

**Phantasmal Gardeners, Nibbit, Fuzzy Wurm Crawler, Slimes.** No official source text
retrieved this session mentions any of these four by name. All evidence for them is
local-run observation only `[S5, S6]`. The prior report's claim that "official beta notes
later prevented consecutive Slime encounters" could **not** be re-confirmed from the S2
excerpts retrieved this session and is not repeated here as a sourced fact; if it remains
true it needs a fresh citation, not carry-forward.

**Aeonglass, new for this session's evidence base.** S1 verbatim: *"As many of you have
heard by now, The Doormaker has been removed from the game."* and *"Thus a new boss,
Aeonglass, is here!"* `[S1, verbatim]`. This directly confirms, from an official source for
the first time in this citation chain, that Aeonglass is a current boss as of v0.107.1 —
previously this fact rested only on local-run evidence in `playtests/IRONCLAD.md`'s "Known
Act 3 Threats" section `[S8]`.

**Reactive/scaling enemy rule.** *"When a power changes after damage, an unblocked hit, a
card type, or a turn boundary, stop generic automation."* `[S7, paraphrase of AGENTS.md's
Autonomous Turn Quality Gate item 6, "Stop automation and inspect the full state when an
enemy has an unfamiliar scaling/status power"]` — this is local project policy, not an
official mechanic statement, and is presented here as policy, not as a verified game
mechanic.

### 3. Drafting, shops, upgrades, removals, and map pathing

This sub-question is answered primarily from local project policy (`AGENTS.md`) and the two
run postmortems, which is the correct evidence class for it — it is an agent-operational
question, not a game-mechanic-verification question, so it does not require external patch
sourcing to the same degree as sub-questions 1-2.

- *"The starter deck's open need is damage. Five Strikes, four Defends, and Bash do not
  justify an elite path by HP alone."* `[S8, verbatim, playtests/IRONCLAD.md Run Plan
  section]`.
- *"E01 | 2-12 | The agent selected a card at all seven card rewards: Rupture, Crimson
  Mantle, Shrug It Off, Pommel Strike, True Grit, Body Slam, and Feel No Pain."* `[S5,
  verbatim, Evidence table]` — direct textual support for the "do not draft unsupported
  packages" rule.
- *"E05 | 7 | The agent left a shop with 126 gold and bought nothing despite Fiend Fire
  being offered."* `[S6, verbatim, Evidence table]` — direct textual support for the "shops
  solve the bottleneck" rule.
- *"Cards accepted from normal rewards: 0 of 3."* `[S6, verbatim, Final State]` — confirms
  the opposite failure mode (over-skipping) is separately evidenced, not inferred.

`AGENTS.md`'s Card Reward Discipline and Map Pathing sections `[S7, verbatim, multiple
bullet points quoted directly under their own headers in that file]` already encode the
policy synthesized from these two runs; this report does not need to re-derive it from
scratch, only confirm it is still consistent with the directly-quoted run evidence above —
which it is.

### 4. Executable turn-by-turn combat policy

`AGENTS.md`'s "Autonomous Turn Quality Gate" section, read directly this session, is
verbatim: *"Do not drive combat with a static per-card score... Sum all displayed incoming
attack damage, including multi-hit counts, then subtract current Block. Check exact or
conservative lethal before spending energy on Block."* `[S7, verbatim]`. This is local
project policy (not a claim about game mechanics) and is treated as such — it is the
correct source class for this sub-question, and this report does not attach a numbered
external citation to operational-policy sentences that are not mechanic claims.

The two-turn expected-loss framing and race-vs-block logic in the prior report's Turn
Policy section is reproduced here as consistent with `AGENTS.md`'s existing text; no new
external verification was needed or attempted for pure agent-policy logic, per this
sub-question's own stopping condition (policy coherence, not mechanic verification).

### 5. What should change after runs `1790695747` and `1790731181`

**Run `1790695747`** (`[S5]`, directly re-read this session, full file quoted where used
above): loss on Act 1 floor 14 to Fossil Stalker; seven-for-seven card-reward acceptance
with an unsupported Rupture/Crimson Mantle/Body Slam/Feel No Pain mix; three potions
(Flex, Liquid Bronze, Swift) unused at death `[S5, verbatim, Final State]`.

**Run `1790731181`** (`[S6]`, directly re-read this session): loss on Act 1 floor 8 to
Bygone Effigy; zero of three normal card rewards accepted, Fiend Fire skipped at a 126-gold
shop visit, Stable Serum unused at death `[S6, verbatim, Final State/Evidence]`.

Both files' own "Next Experiment" sections are already directly on point and require no
reinterpretation: run `1790695747`'s calls for *"turn-level threat budgeting, skip-by-default
card rewards, explicit potion triggers, and a mandatory full-state inspection for unfamiliar
scaling enemies"* `[S5, verbatim]`; run `1790731181`'s calls for *"a damage-floor check
before the first Elite,"* valuing *"strong shop purchases against current deck needs,"* and
optimizing *"expected damage over the next two turns rather than current-turn Block alone"*
`[S6, verbatim]`. `AGENTS.md`, read directly this session, already incorporates both sets of
recommendations nearly verbatim (e.g., the Autonomous Turn Quality Gate and Card Reward
Discipline sections) `[S7]` — this session's re-read finds no gap between what the two runs
recommended and what `AGENTS.md` currently states. No new AGENTS.md changes are proposed by
this redo; the citation-integrity hardening does not surface new operational findings from
the same two run files, only new/corrected sourcing for the game-mechanic claims layered
around them.

## Synthesis

The central strategic finding is unchanged from the prior report and remains well-supported
by directly re-quoted local evidence: Ironclad A3 on `v0.107.1` requires a phase-sensitive
policy — solve the pre-first-elite damage gap without over-committing to unsupported
synergy packages, then add mitigation/consistency/one coherent scaling engine, and drive
combat by two-turn expected-HP-loss rather than static card scores `[S5, S6, S7, S8]`. This
session's contribution is not a change in that policy but a materially stronger evidentiary
foundation for the *specific numeric card facts* surrounding it: several v0.107.1-era
numbers (Setup Strike, Crimson Mantle, Taunt, Rampage, Colossus, Mangle, Pact's End, Expect
a Fight, Forgotten Ritual, Demon Form) are now traceable to literal official patch-note text
fetched this session, most via the "before" side of a later beta delta `[S2]`, rather than
resting solely on a prior session's local-wiki query that this session could not
independently repeat. Two new facts absent from the prior report were confirmed this
session: Aeonglass's official introduction as a v0.107.1-era boss `[S1]`, and independent
external confirmation of the Ironclad's starting kit via `slaythespire.wiki.gg` `[S4]`.

Several claims that the prior report treated as settled are demoted here to explicit gaps:
Fossil Stalker's singleplayer Strength trigger (official text confirms only a multiplayer
change) `[S1]`; Bygone Effigy's mechanics entirely (no official or wiki source reached this
session) `[S6-only]`; all four potions' exact effects (no official or wiki source reached)
`[S7/S8-only, local policy not mechanic text]`; and most named relics beyond Booming Conch
and Nutritious Soup (Orichalcum, Ornamental Fan, Arcane Scroll, Ruined Helmet, Sturdy Clamp,
Razor Tooth, Throwing Axe — carried-forward local evidence only, not re-verified this
session).

## Confidence Assessment

| Claim | Confidence | Basis |
|---|---|---|
| `v0.107.1` is the relevant main-branch build; later beta values must be separated | High | S1/S2 directly fetched and dated this session |
| Conflagration, Drum of Battle, Howl From Beyond, Entrench, Unrelenting v0.107.1 texts | High | Verbatim in S1, the v0.107.1 patch note itself |
| Setup Strike, Crimson Mantle, Taunt, Rampage, Colossus, Mangle, Pact's End, Demon Form, Bloodletting, Expect a Fight, Forgotten Ritual v0.107.1-era values | Medium-High | Inferred from the "before" side of a later dated beta delta in S2, verbatim but not directly labeled "v0.107.1" in the source |
| Booming Conch, Nutritious Soup v0.107.1 texts | High | Verbatim in S1 |
| Aeonglass exists as a v0.107.1-era boss | High | Verbatim in S1, newly confirmed this session |
| Ironclad starting kit (80/64 HP, 5 Strike/4 Defend/Bash, Burning Blood 6 HP) | High | Cross-confirmed by S4 (external wiki, newly accessible this session) and S5/S6 (local runs) independently |
| Fossil Stalker singleplayer Strength-on-hit trigger | Medium | Only local-run observation (S5) plus an MP-scoped official note (S1) that does not directly state the SP rule |
| Bygone Effigy mechanics/HP/move table | Low | Local-run observation only (S6); no official or wiki source reached this session |
| Living Fog, Gremlin Merc, Phantasmal Gardeners, Nibbit, Fuzzy Wurm Crawler, Slimes combat mechanics | Low | Local-run observation only, except Gremlin Merc's gold-reward rule and Living Fog's cosmetic fix (both High, S1 verbatim) |
| Flex Potion, Liquid Bronze, Swift Potion, Stable Serum exact effects | Low/Unverified | No official or wiki source reached this session; only local usage-policy text (S7/S8) |
| Orichalcum, Ornamental Fan, Arcane Scroll, Ruined Helmet, Sturdy Clamp, Razor Tooth, Throwing Axe exact text | Low | Carried-forward local file claim only (S8), not re-verified this session against any live source |
| Agent-operational drafting/shop/combat policy conclusions | High | Directly re-quoted from AGENTS.md and both run files this session; this is the correct evidence class for policy questions |
| Mod tested only against v0.103.2, not v0.107.1 | High | Verbatim in S10 (README.md), a genuine version-mismatch caveat not previously surfaced |

## Missing Perspectives & Caveats

- `slaythespire.wiki.gg` began serving an interactive Cloudflare Turnstile "verify you are
  human" challenge partway through this session, blocking all further per-card,
  per-monster, and per-potion page fetches after the Ironclad overview page had already
  loaded successfully. This is a universal (not AI-crawler-specific) challenge per the
  retrieving agent's own report, so no bypass was attempted; it is logged here as an
  honest retrieval gap, not silently omitted.
- The official Steam RSS feed (S2) and patch note (S1) do not cover every named card,
  relic, monster, or potion in this report's scope — only those that were the subject of a
  balance or bug-fix note. Cards/relics/enemies never mentioned in any patch remain
  entirely unverified by official sourcing across the whole session.
- The Steam News Hub page (S3) under-reported its own news history compared to the RSS
  feed (2 items visibly rendered vs. 10 in the feed) on this fetch; it is cited only for
  that reliability observation, not as a source of unique mechanic facts.
- `slaythespire.wiki.gg`'s Ironclad overview page does not state which specific game
  version/patch its data reflects; it should not be assumed to be pinned to `v0.107.1`
  specifically, though its starting-kit numbers cross-confirm the locally-observed values.
- The mod's own `README.md` states testing only against `v0.103.2`, an earlier build than
  the `v0.107.1` this report and the two supplied runs target `[S10]` — a real
  documentation/testing-currency gap independent of this report's own findings.
- Potions and most named relics remain a genuine open verification gap; no session source
  reached their exact text. Do not treat `AGENTS.md`/`playtests/IRONCLAD.md`'s potion and
  relic usage rules as confirmed game-mechanic text — they are local operational policy
  built from run observations, and this report preserves that distinction throughout rather
  than upgrading their confidence by association with newly-fetched official sources.

## Sources

1. [Slay the Spire 2 — Major Update #2 - v0.107.1 (Steam News)](https://store.steampowered.com/news/app/2868840/view/710026912607505280) — primary official source; fetched directly this session via real-browser retrieval; content confirmed present and quoted verbatim above (Conflagration, Drum of Battle, Howl From Beyond, Entrench, Unrelenting, Booming Conch, Nutritious Soup, Bestiary, Aeonglass, Doormaker removal, Gremlin Merc gold rule, Living Fog cosmetic fix, Fossil Stalker MP note, Hellraiser bug fix). Posted 2026-06-18/19.
2. [Official Slay the Spire 2 Steam News RSS feed](https://store.steampowered.com/feeds/news/app/2868840/?cc=US&l=english) — primary official source; fetched directly this session; content confirmed present and quoted verbatim above (v0.108.0-v0.111.0 beta deltas for Setup Strike, Crimson Mantle, Colossus, Taunt, Bloodletting, Demon Form, Expect a Fight, Forgotten Ritual, Mangle, Pact's End, Rampage). Entries spanning 2026-06-19 through 2026-09-25.
3. [Slay the Spire 2 Steam News Hub](https://store.steampowered.com/news/app/2868840) — primary official source; fetched directly this session; content confirmed present but incomplete on this render (only 2 of the RSS feed's 10 entries visibly loaded) — cited only for that reliability observation, not for unique mechanic facts.
4. [Slay the Spire 2 wiki (wiki.gg): Ironclad](https://slaythespire.wiki.gg/wiki/Slay_the_Spire_2:Ironclad) — secondary community wiki source; fetched directly this session; content confirmed present and quoted verbatim above (HP totals, starting deck, starting relic text, card pool composition). Newly accessible this session — the prior report logged this domain as returning `401`; that was evidently either a transient block or a wrong-URL guess, not a persistent hard wall.
5. `playtests/runs/ironclad-modded-profile1-1790695747.md` — primary local run observation; read directly this session; quoted verbatim above.
6. `playtests/runs/ironclad-modded-profile1-1790731181.md` — primary local run observation; read directly this session; quoted verbatim above.
7. `AGENTS.md` — primary local operational-policy document; read directly this session; quoted verbatim above.
8. `playtests/IRONCLAD.md` — primary local operational-policy/reference document; read directly this session; quoted verbatim above. Its own card/relic text table is itself sourced from a prior session's live local-wiki query (per its own header), which this session could not independently re-run — flagged inline everywhere it is used as evidence rather than treated as freshly verified.
9. `mcp/README.md` — primary local implementation documentation; read directly this session; quoted/paraphrase-matched above for `/api/v1/wiki` and Compendium scope.
10. `README.md` — primary local project documentation; read directly this session; quoted verbatim above for the `v0.103.2` tested-version statement.

## Attempted, non-substantive sources

- `[ATTEMPTED-1]` [Steam Community guide search: Ironclad](https://steamcommunity.com/app/2868840/guides/?searchText=Ironclad&browsefilter=trend&requiredtags%5B0%5D=English) — fetched directly this session via real-browser (JS-enabled) retrieval. Unlike the prior session's manual plain-fetch finding, this session's JS-rendered fetch did filter correctly (3 of 3 results with the search term vs. 16 of 16 without it). However, none of the 3 returned guide titles/snippets are substantively about Ironclad Ascension 3 strategy: a WeMod cheat-trainer guide, an "Enchantments and Their Ratings" guide, and a "Topping the Daily Challenge Leaderboard" guide. Excluded from numbered Sources on non-substance grounds; the JS-dependency question itself is noted but not the deciding factor here.
- `[ATTEMPTED-2]` `slaythespire.wiki.gg` individual card/monster/potion subpages (Fossil Stalker, Bygone Effigy, Perfected Strike, Fiend Fire, Rupture, Hellraiser, Twin Strike, Taunt, Bloodletting, potions, remaining relics) — fetch attempts began but the domain started serving an interactive Cloudflare Turnstile challenge mid-session before any of these could load. No content was retrieved; nothing from these pages is cited anywhere above.

## Self-Evaluation

### Citation Integrity Pass

| # | Source | Directly fetched this session? | Spot-checked against a specific report claim? |
|---|---|---|---|
| 1 | Major Update #2 v0.107.1 patch note | Yes | Yes — Conflagration, Drum of Battle, Booming Conch, Nutritious Soup, Aeonglass, Gremlin Merc, Living Fog, Hellraiser bug-fix, Fossil Stalker MP note |
| 2 | Official Steam News RSS feed | Yes | Yes — Setup Strike, Crimson Mantle, Colossus, Taunt, Bloodletting, Demon Form, Expect a Fight, Forgotten Ritual, Mangle, Pact's End, Rampage deltas |
| 3 | Steam News Hub | Yes | Yes — cited specifically for its incomplete-render reliability finding, not a mechanic claim |
| 4 | wiki.gg Ironclad page | Yes | Yes — starting HP, starting deck, starting relic, card pool composition |
| 5 | Run 1790695747 file | Yes | Yes — E01/E02/E04/E05 evidence rows, Final State, Next Experiment |
| 6 | Run 1790731181 file | Yes | Yes — E01/E05/E06 evidence rows, Final State, Next Experiment |
| 7 | AGENTS.md | Yes | Yes — Autonomous Turn Quality Gate, Card Reward Discipline quotes |
| 8 | playtests/IRONCLAD.md | Yes | Yes — card-table cross-matches, Known Act 3 Threats (Aeonglass) |
| 9 | mcp/README.md | Yes | Yes — Bestiary/Compendium scope paraphrase-match |
| 10 | README.md | Yes | Yes — v0.103.2 tested-version quote |

All ten numbered Sources pass the integrity check: directly fetched/read this session and
spot-checked against at least one specific, adjacently-cited claim in the report body. No
numbered Source is a listing/index/search page carried on faith. Both non-substantive
attempts are logged separately rather than omitted or upgraded.

- **Score**: 4.6/5
- **Date**: 2026-09-30T00:11:58-07:00
- **Dimension scores**: Pipeline Compliance 5, Source Diversity 4, Citation Completeness 5, Confidence Calibration 5, Scope Discipline 4, Red Team Depth 4, Depth Gate Accuracy 5
- **Lowest dimension**: Scope Discipline (4) — the "before-side beta delta" inference technique materially expanded verified numeric coverage but pushed retrieval slightly past a literal 4-minute/10-source front-stop, justified here as a deliberate deep-mode override rather than scope creep, but worth flagging honestly.
- **Improvements proposed**: none — the citation-integrity hardening was successfully applied without requiring a procedural change; no GitHub issue filed.
