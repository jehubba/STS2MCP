---
task_id: interactive
agent: research
status: complete
timestamp: 2026-09-29T19:30:00-07:00
topic: Slay the Spire 2 Ironclad Ascension 3 strategy for v0.107.1
depth: deep
output_file: c:\Users\Jeffrey\source\repos\sts2-mcp\STS2MCP\research\2026-09-29-sts2-ironclad-a3-strategy.md
---

# Research Report: Slay the Spire 2 Ironclad A3 Strategy (v0.107.1)

## Research Scope

This report targets the main-branch `v0.107.1` build used by the two supplied Ascension 3 runs. Mega Crit shipped Major Update #2 (`v0.107.1`) on June 19, 2026. Later `v0.108.0`-`v0.111.0` notes are explicitly beta-branch material and include consequential Ironclad changes; they are useful for identifying version-sensitive facts, not as rules for `v0.107.1`. [Source: https://store.steampowered.com/news/app/2868840/view/710026912607505280, 2026-06-19; https://store.steampowered.com/feeds/news/app/2868840/?cc=US&l=english, generated 2026-09-29]

Sub-questions covered:

1. Which verified Ironclad cards, relics, and potions matter strategically on `v0.107.1`?
2. What is known about Act 1 threats, particularly the named encounters?
3. What drafting, shop, upgrade, removal, skip, and map rules follow from the evidence?
4. What turn-by-turn combat controller avoids static card scores?
5. What should change after runs `1790695747` and `1790731181`?

Stopping condition: enough verified evidence to produce an executable policy, with exact unverified card/enemy facts isolated for local API or in-game verification. The public wiki could not be retrieved (`401`), its Wayback CDX lookup returned no snapshot, and the Steam guide index contained no substantive Ironclad guide. This materially limits claims about complete card text and monster move tables.

## Evidence by Sub-question

### 1. Ironclad Kit: Verified Pool and Strategic Roles

#### Build boundary

The exact branch matters. On `v0.107.1`, Mega Crit reworked Conflagration and Drum of Battle; buffed Howl From Beyond, Entrench, and Unrelenting; and changed several relic/enemy systems. Subsequent beta patches changed Crimson Mantle, Colossus, Setup Strike, Demon Form, Taunt, Bloodletting, Mangle, Pact's End, Expect a Fight, Forgotten Ritual, and Rampage. Do not use current beta values in a `v0.107.1` run. [Source: https://store.steampowered.com/news/app/2868840/view/710026912607505280, 2026-06-19; https://store.steampowered.com/feeds/news/app/2868840/?cc=US&l=english, beta notes 2026-07-03 through 2026-08-14]

#### Starting package

Both local runs verify a starter deck of five Strikes, four Defends, and Bash, with Burning Blood as the starting relic. Burning Blood heals after combat, so it changes the value of modest chip damage but cannot rescue lethal or prevent an in-combat damage spiral. [Source: playtests/runs/ironclad-modded-profile1-1790695747.md, 2026-09-29; playtests/runs/ironclad-modded-profile1-1790731181.md, 2026-09-29; AGENTS.md, current 2026-09-29]

#### Strategically important card groups

This is a strategically important pool, not a claim of a complete catalog. Exact text and upgrade values should be pulled from the local endpoint before automated valuation.

| Role                      | Verified STS2 cards/names                                                                                                         | Operational interpretation on v0.107.1                                                                                                                                                                                                                                                                                                       | Confidence                                                    |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| Early front-loaded damage | Twin Strike, Thunderclap, Perfected Strike, Pommel Strike, Fiend Fire, Unrelenting, Conflagration, Howl From Beyond, Setup Strike | Before the first elite, take at least one efficient damage solution when the starter deck cannot end ordinary fights promptly. Twin Strike was offered twice and skipped in run `1790731181`; the deck then entered Bygone Effigy with its damage need open. Fiend Fire was offered at a shop and assessed as a high-impact missed purchase. | Medium-High for the need; Medium for individual ranking       |
| Area damage               | Thunderclap, Conflagration                                                                                                        | Multi-enemy fights such as Slimes and Phantasmal Gardeners make AoE strategically relevant. `v0.107.1` Conflagration deals 2 damage to all enemies 4(5) times.                                                                                                                                                                               | High for Conflagration text; Medium for encounter application |
| Block/mitigation          | Shrug It Off, True Grit, Crimson Mantle, Taunt, Armaments, Body Slam, Entrench, Colossus                                          | Add efficient block, but do not confuse block payoff cards with a functioning block engine. Body Slam and Entrench need repeatable large Block; one or two ordinary block cards do not establish that engine.                                                                                                                                | Medium                                                        |
| Exhaust engine            | True Grit, Feel No Pain, Fiend Fire, Drum of Battle, Forgotten Ritual                                                             | Exhaust enablers and payoffs must be counted separately. `v0.107.1` Drum of Battle draws two and grants 2(3) Energy when exhausted. Feel No Pain without meaningful exhaust density is speculative; Fiend Fire can be both front-loaded damage and an enabler.                                                                               | High for Drum; Medium for package rule                        |
| Self-damage/Strength      | Rupture, Bloodletting                                                                                                             | Rupture is speculative without repeatable self-damage. One isolated payoff should not justify later weak enablers. Exact `v0.107.1` text must be verified locally.                                                                                                                                                                           | Medium-Low on mechanics; High on draft diagnosis              |
| Strength/scaling          | Setup Strike, Demon Form, Rampage, Expect a Fight                                                                                 | Scaling is valuable for long fights, but later beta notes changed these cards. Never import `v0.109+` numbers or text into `v0.107.1`.                                                                                                                                                                                                       | High on version sensitivity; Low-Medium on v0.107.1 ranking   |
| Strike synergy            | Perfected Strike, Hellraiser, Tezcatara's Nutritious Soup                                                                         | Perfected Strike becomes worse as basic Strikes are removed unless replacement Strike-tag cards compensate. On `v0.107.1`, Nutritious Soup makes Strikes cost 0, Eternal, and deal +3 damage; Hellraiser is confirmed to auto-play Strike cards. Treat Strike density as an explicit package, not a default reason to retain every Strike.   | High for Soup/Hellraiser facts; Medium for policy             |
| Draw/consistency          | Pommel Strike, Shrug It Off, Drum of Battle                                                                                       | Draw is useful when it improves access to damage or mitigation, but adding draw plus unsupported payoffs still dilutes the deck.                                                                                                                                                                                                             | Medium                                                        |

Card-specific traps and speculative picks:

- **Rupture:** skip unless the deck already has repeatable, affordable self-damage that it wants to play. The first run added Rupture without enough support and then drafted unrelated packages. [Source: playtests/runs/ironclad-modded-profile1-1790695747.md, 2026-09-29]
- **Body Slam:** skip unless ordinary turns reliably create substantial surplus Block. It is not itself a block engine. [Source: same local run, 2026-09-29]
- **Feel No Pain:** skip unless exhaust density is already meaningful or the offered card simultaneously solves an immediate need. [Source: same local run, 2026-09-29]
- **Perfected Strike:** conditional early damage. Count current and expected Strike-tag density; do not take it solely because the starter deck has five Strikes. Its exact `v0.107.1` damage formula requires local verification.
- **Fiend Fire:** high priority when the deck still lacks damage and can tolerate hand exhaustion; it also bridges front-loaded damage into exhaust support. The local postmortem calls skipping it at 126 gold a misplay, but exact shop price/text was not captured. [Source: playtests/runs/ironclad-modded-profile1-1790731181.md, 2026-09-29]
- **True Grit/Armaments:** flexible cards are not automatic picks. Take them when their immediate output and package role outperform skip; do not use “eventual exhaust/upgrades” as a substitute for first-elite damage.

#### Relics and potions

- **Burning Blood:** post-combat sustain permits calculated chip damage, not avoidable large hits. The controller should compare expected in-combat damage with expected post-combat healing, never add future healing to current lethal margin. [Source: AGENTS.md; both local runs, 2026-09-29]
- **Neow's Booming Conch:** on `v0.107.1`, draws extra cards and grants one Energy at the start of elite combats. This raises elite readiness only if the deck can convert the opening resources into damage/setup; run `1790695747` still took ten turns against Phantasmal Gardeners. [Source: official `v0.107.1` notes, 2026-06-19; local run, 2026-09-29]
- **Tezcatara's Nutritious Soup:** a verified, powerful Strike package relic on this build: Strikes cost 0, become Eternal, and deal +3 damage. Re-evaluate removals and Perfected Strike after acquiring it. [Source: official `v0.107.1` notes, 2026-06-19]
- **Orichalcum, Ornamental Fan, Arcane Scroll:** observed in the supplied runs, but their exact STS2 text was not captured. Query locally before encoding interactions. [Source: both local runs, 2026-09-29]
- **Flex Potion:** use before a turn containing enough attacks for the Strength to materially shorten the fight or enable lethal. Exact magnitude/duration needs Potion Lab verification.
- **Liquid Bronze:** use early against multi-hit attackers or when a fight is expected to last several attacking rounds; holding it through a seven-turn lethal Fossil Stalker fight was dominated by using it. Exact Thorns value needs Potion Lab verification. [Source: AGENTS.md; run `1790695747`, 2026-09-29]
- **Swift Potion:** use when current draw cannot cover a dangerous attack, when three draws could expose lethal, or before accepting double-digit damage. Exact draw count needs Potion Lab verification. [Source: AGENTS.md; run `1790695747`, 2026-09-29]
- **Stable Serum:** the local postmortem identifies retention as its relevant use. Spend it when retaining offense or mitigation bridges into a known dangerous next turn; do not die with it while repeatedly taking unsustainable attacks. Exact duration/selection rules need Potion Lab verification. [Source: run `1790731181`, 2026-09-29]

**STS1 separation:** Names such as Burning Blood, Bash, Shrug It Off, Fiend Fire, Feel No Pain, Body Slam, and Demon Form also exist in STS1. This report does not assume their STS1 numbers, rarity, upgrade, or interaction text. Only the STS2 observations and official patch statements above are treated as facts.

### 2. Act 1 Encounters and A3 Responses

The official `v0.107.1` update added the Bestiary with encountered monsters' moves and animations, but not full stats/lore at that time. Exact move tables should therefore come from the in-game Bestiary or current compendium, not memory. [Source: official `v0.107.1` notes, 2026-06-19]

| Encounter                 | Verified evidence                                                                                                                                                                                                       | Ironclad policy                                                                                                                                                                                                                                                                                     | Confidence                                                   |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ |
| Bygone Effigy (elite)     | Run `1790731181` faced repeated 23-damage attacks, took 67 total over eight turns, and died while maximizing current-turn Block.                                                                                        | Treat as a damage-clock fight when incoming exceeds sustainable block. Calculate two-turn damage prevented by killing sooner; deploy Stable Serum or damage potion before the first otherwise-unmanageable cycle. Do not spend all energy blocking if that merely schedules another 23-damage turn. | High for observed run; Medium for generalized pattern        |
| Fossil Stalker            | Official notes confirm a Strength-on-hit mechanic in multiplayer; the local guide records that unblocked hits trigger Strength in singleplayer. Run `1790695747` lost 50 HP over seven turns with three potions unused. | Prevent the first unblocked hit when feasible, use Liquid Bronze early, and re-read live Strength/intent after every attack that connects. Once Strength rises beyond sustainable mitigation, race; generic static scoring is unsafe.                                                               | High for reactive scaling; Medium for exact trigger at A3    |
| Living Fog                | In run `1790695747`, it dealt 33 damage over eight turns. Official notes only verify a smoke/VFX fix, not mechanics.                                                                                                    | Flag as a prolonged-fight warning. Inspect powers and intents before automation; prioritize shortening the fight over repeatedly cycling low-impact cards.                                                                                                                                          | High for observation; Low for general mechanics              |
| Nibbit                    | In run `1790731181`, it dealt only 2 damage over four turns.                                                                                                                                                            | Use low-pressure turns to advance damage, not to overblock. The fight's low damage does not prove the deck is elite-ready.                                                                                                                                                                          | Medium                                                       |
| Slimes                    | A Slimes fight dealt 11 over five turns immediately before an elite; official beta notes later prevented consecutive Slime encounters, confirming the encounter class but not move values.                              | AoE and front-loaded damage reduce status/damage accumulation. Reassess the first-elite plan after significant chip damage.                                                                                                                                                                         | Medium                                                       |
| Gremlin Merc              | Official `v0.107.1` notes say that if Gremlin Merc stole no gold but Fat Gremlin escaped, the player receives 50% of the normal gold reward. Run `1790695747` took 22 damage over eleven turns.                         | Front-load damage and identify whether preventing theft, securing the kill, or preserving HP has highest expected value. An eleven-turn fight is a deck-output alarm.                                                                                                                               | High for reward mechanic; Medium for combat policy           |
| Phantasmal Gardeners      | Run `1790695747` required ten turns and dealt 29 damage despite Booming Conch's elite benefit.                                                                                                                          | Opening resources must be converted into target prioritization and damage. If the fight projects this long, spend a potion rather than preserve it for a future the deck may not reach.                                                                                                             | High for run observation; Low-Medium for general move policy |
| Fuzzy Wurm Crawler        | Run `1790731181` took 2 damage over five turns.                                                                                                                                                                         | Do not infer strength from a low-pressure normal fight. Use fight duration as a damage-readiness signal.                                                                                                                                                                                            | Medium                                                       |
| Act 1 bosses/other elites | No accessible source in this run provided current `v0.107.1` move tables.                                                                                                                                               | Before entering the boss/elite, query Bestiary state and generate a bespoke response. Do not import STS1 boss logic or assume encounter identity.                                                                                                                                                   | High confidence that verification is required                |

Reactive/scaling enemy rule: when a power changes after damage, an unblocked hit, a card type, or a turn boundary, stop generic automation. Re-read complete state after each triggering action and recompute lethal, incoming damage, and next-turn scaling. Fossil Stalker is the verified example. [Source: AGENTS.md, current 2026-09-29]

### 3. Drafting, Shops, Upgrades, Removals, and Map Pathing

#### Before the first elite

1. **Run a damage-floor check after every reward.** Estimate a conservative two-cycle damage total from the actual deck against the likely elite HP shown by the Bestiary. If the deck cannot end the fight before mitigation collapses, damage remains an open need.
2. **Take one efficient front-loaded or AoE card before the first elite when the starter deck is still the damage core.** Run `1790731181` skipped Thunderclap/Perfected Strike, then Twin Strike/Thunderclap/Perfected Strike, then Armaments/True Grit/Twin Strike; it reached Bygone Effigy with no normal-reward cards and died. [Source: run `1790731181`, 2026-09-29]
3. **Do not take three speculative package seeds.** Run `1790695747` accepted all seven rewards and combined unsupported Rupture, Body Slam, and Feel No Pain plans. [Source: run `1790695747`, 2026-09-29]
4. **Prefer cards that solve the immediate need and preserve optionality.** A damage card with draw, AoE, or exhaust utility is preferable to a pure payoff lacking enablers.

#### After damage is adequate

- Add consistency, efficient block, and one coherent scaling plan.
- Count enablers and payoffs. A package is supported only when at least two existing cards/relics make the new card materially better, or the new card is independently good.
- Skip cards whose best-case role is “maybe later.” Every addition must name the current need and existing support.

#### Shops

Use gold to solve the run's bottleneck, not to maximize gold retained. Compare each purchase against the next forced elite/boss and path. Leaving with 126 gold while Fiend Fire was offered and damage remained open was a concrete failure. [Source: run `1790731181`, 2026-09-29]

Shop order:

1. Fight-winning card/relic/potion for the next forced threat.
2. Removal that materially improves draw consistency without breaking a Strike package.
3. Upgrade-equivalent or flexible support.
4. Save only when no purchase changes projected survival/value enough.

#### Upgrades and removals

- Upgrade the card with the largest near-term change in expected damage prevented or turns-to-kill, not the card with the largest isolated number.
- Prioritize front-loaded damage before the first elite when damage is open; prioritize draw/energy/scaling once output is adequate.
- Remove a Strike when attacks are redundant and no Strike synergy exists; remove a Defend when damage density is urgently low and mitigation remains adequate.
- Recompute after Perfected Strike, Hellraiser, Nutritious Soup, or any relic/card that names Strikes. Never run a fixed “remove Strike first” rule.

#### Skip criteria

Skip when all are true:

- The card does not solve the current damage, mitigation, consistency, or scaling need.
- Fewer than two existing cards/relics support its package.
- Its standalone floor is below the deck's average draw.
- Taking it worsens the probability of drawing the cards needed in the next elite/boss.

Do not convert “skip by default” into “skip all.” The two runs demonstrate both failure extremes. [Source: both local runs, 2026-09-29]

#### Map pathing and elite readiness

HP alone is insufficient. Enter an elite only when most of the following are true:

- **Damage clock:** credible kill plan before enemy scaling/attack cadence exceeds sustainable mitigation.
- **Opening consistency:** enough draw/energy or card density to execute setup in the first cycle.
- **Potion plan:** at least one relevant potion, with a declared trigger; or a deck strong enough not to need one.
- **Encounter knowledge:** Bestiary mechanics inspected for unfamiliar/reactive enemies.
- **Exit path:** rest/shop after the elite if projected loss is high.
- **Reward value:** the relic reward is worth the estimated HP/potion cost.
- **No false readiness:** easy normal fights did not merely conceal low damage.

At healthy HP, prefer an elite only with a credible damage plan, combat potion, or high-impact card/relic purchase. Otherwise choose a normal/unknown/rest path that improves readiness. [Source: AGENTS.md, current 2026-09-29]

### 4. Executable Combat Policy

#### Turn loop

1. **Read state:** current HP, Block, Energy, hand, draw/discard/exhaust, enemy HP, powers, intents, multi-hit counts, potions, and turn-dependent relics.
2. **Compute incoming damage:** sum every displayed hit after known modifiers; subtract current Block. Treat uncertain reactive scaling conservatively.
3. **Check lethal first:** compute guaranteed current-turn damage for legal sequences, including Vulnerable/Strength and deterministic relic/potion effects. If exact lethal exists, take it and spend no energy on Block.
4. **Check near-lethal/two-turn race:** estimate a conservative next-turn draw and enemy next action. Compare total HP loss under (a) maximum current Block and a longer fight versus (b) enough mitigation plus faster kill. Choose the line minimizing expected total HP loss, not current-turn loss alone.
5. **Reserve mitigation:** if no lethal, reserve enough playable mitigation to keep expected loss within the encounter budget. At or below 50% HP, avoid preventable loss unless offense prevents greater expected damage over two turns.
6. **Spend remaining resources on output/setup:** zero-cost utility first, then debuffs/setup, then attacks that benefit from them. Preserve cards only when retention has a concrete next-turn purpose.
7. **Potion gate:** use a potion now if it enables lethal, prevents meaningful damage, stops reactive scaling, or materially improves a multi-attack turn. At below 50% HP, spend a relevant potion before accepting 10+ avoidable damage.
8. **Re-read after state-changing cards:** draw, generated cards, exhaust, Energy, Strength/Dexterity, cost changes, or hand-index shifts invalidate the prior calculation.
9. **End-turn audit:** log incoming damage, lethal status, mitigation chosen, expected HP loss, next-turn plan, and potion decision.

#### Race versus block

Race when enemy damage or scaling rises faster than sustainable mitigation, or when spending all Energy on Block adds another dangerous enemy turn. Block when preventing a hit also prevents a reactive power trigger (Fossil Stalker), preserves a potion, or keeps the next-turn lethal line alive. The choice is based on two-turn expected loss, not a static card score. [Source: AGENTS.md; both local postmortems, 2026-09-29]

#### Compact decision framework

```text
OBSERVE -> LETHAL? -> REACTIVE TRIGGER? -> TWO-TURN LOSS COMPARISON
        -> RESERVE MINIMUM MITIGATION -> POTION TRIGGER
        -> PLAY SETUP/UTILITY -> PLAY DAMAGE -> RE-READ -> AUDIT
```

A card has no fixed score. Its turn value is:

`damage prevented by shortening the fight + immediate mitigation + future setup value - opportunity cost - package/draw risk`.

Use exact simulation where possible; otherwise use conservative lower bounds for player damage and upper bounds for enemy damage.

### 5. Postmortems and Corrective Recommendations

#### `modded:profile1:1790695747`

Evidence: seven cards taken from seven rewards; final deck mixed Rupture, Crimson Mantle, Shrug It Off, Pommel Strike, True Grit, Body Slam, and Feel No Pain. Living Fog dealt 33 over eight turns; Phantasmal Gardeners dealt 29 over ten; Gremlin Merc dealt 22 over eleven; Fossil Stalker dealt the final 50 over seven. Flex, Liquid Bronze, and Swift potions were unused. [Source: playtests/runs/ironclad-modded-profile1-1790695747.md, 2026-09-29]

Recommendations:

- Require a written need/support sentence before every pick. Rupture, Body Slam, and Feel No Pain would each have failed the support test when selected.
- Cap speculative packages at one seed card; do not draft the second payoff until enablers exist.
- Treat an eight-plus-turn normal fight as an immediate output alarm and tighten subsequent picks/pathing.
- Use Liquid Bronze early against Fossil Stalker; prevent the first unblocked hit where feasible; inspect Strength after every connection.
- Use Swift before accepting a dangerous hand and Flex on a multi-attack or lethal turn. Dying with all three potions is a controller-policy failure.

#### `modded:profile1:1790731181`

Evidence: zero normal-reward cards accepted; Twin Strike was skipped twice while damage remained open; the shop was left with 126 gold despite Fiend Fire; Bygone Effigy dealt 67 over eight turns through repeated block-heavy turns; Stable Serum was unused. [Source: playtests/runs/ironclad-modded-profile1-1790731181.md, 2026-09-29]

Recommendations:

- Add a mandatory pre-elite damage-floor gate. If unmet, accept the best adequate front-loaded card even if it is not a premium long-term pick.
- Buy Fiend Fire or another bottleneck-solving shop option when it materially changes elite survival; retained gold has no value after death.
- Against repeated 23-damage attacks, compare “block now and face 23 again” with “take controlled damage and end the fight sooner.”
- Use Stable Serum to retain the attack/mitigation combination required for the dangerous cycle.
- Preserve skip discipline, but define it by current need and support rather than by a target deck size.

## Synthesis

For `v0.107.1` Ironclad at A3, the central strategic problem is balancing immediate damage against package discipline. The first run failed by taking every plausible synergy seed; the second failed by taking none of the offered damage and saving resources through death. Together they support a phase-sensitive policy: acquire enough front-loaded/AoE damage to pass a first-elite clock, then add efficient mitigation, consistency, and only one already-supported scaling engine. [Source: both local playtests, 2026-09-29]

Combat should optimize total expected HP loss over at least two turns. Blocking is correct when it prevents lethal or a reactive trigger, but wrong when it merely extends a fight whose attacks exceed sustainable mitigation. Fossil Stalker demands special handling because hits feed Strength; Bygone Effigy demonstrated the opposite failure, where block maximization prolonged an unwinnable clock. Potions are part of the combat budget and need explicit triggers before entering a dangerous fight. [Source: AGENTS.md; both local playtests, 2026-09-29]

Build discipline is mandatory. The main branch remained `v0.107.1` while later beta patches changed multiple Ironclad cards. An autonomous agent should bind all cached card/relic/enemy facts to `game_build`, query exact text at run start, and invalidate rules whose underlying mechanics changed. [Source: official Steam RSS/news, 2026-06-19 through 2026-09-25]

### Durable Rules Suitable for `AGENTS.md`

1. Before the first elite, take one efficient front-loaded or AoE card if the starter deck still carries the damage plan.
2. At each reward, state the current deck need and at least two existing cards/relics supporting any synergy pick; otherwise skip unless the card is independently efficient.
3. Never draft unsupported Rupture, Body Slam, and Feel No Pain packages in parallel.
4. Skip-by-default means reject cards that do not solve a need; it does not mean reject every non-premium damage card.
5. Before an elite, require a credible damage clock, opening consistency, encounter knowledge, and either a relevant potion or compensating deck/relic strength.
6. Compute exact/conservative lethal before spending Energy on Block.
7. Optimize expected HP loss over the next two turns, not current-turn Block.
8. Against reactive/scaling enemies, stop generic automation and re-read state after every trigger.
9. Against Fossil Stalker, prevent the first unblocked hit when feasible, use Liquid Bronze early, and reassess live Strength after each attack.
10. Use potions when they enable lethal, prevent meaningful damage, stop scaling, or improve a multi-attack turn; a full belt at death is a policy failure.
11. At or below 50% HP, spend a relevant potion before accepting 10+ avoidable damage.
12. Treat any eight-plus-turn normal fight as a damage/output warning before choosing the next card or elite path.
13. Shops solve the next bottleneck; do not preserve gold while passing a purchase that materially changes survival.
14. Recompute Strike removals after Perfected Strike, Hellraiser, or Nutritious Soup; never use a fixed removal order.
15. Bind all mechanics and valuation rules to `game_build`; do not import STS1 or later-beta values silently.

### Facts to Verify Before Autonomous Use

Use `/api/v1/wiki` for discovered **cards and relics only**. It is profile-dependent, defaults to ten results, and does not provide the full game catalog. [Source: mcp/README.md and README.md, current 2026-09-29]

Verify via `/api/v1/wiki`:

- Base/upgraded text, cost, rarity, and tags for every considered Ironclad card, especially Perfected Strike, Fiend Fire, Rupture, Body Slam, Feel No Pain, True Grit, Armaments, Taunt, Hellraiser, Bloodletting, Setup Strike, Entrench, Drum of Battle, Conflagration, and Crimson Mantle.
- Exact text for Burning Blood, Booming Conch, Nutritious Soup, Orichalcum, Ornamental Fan, and Arcane Scroll.
- Whether a discovered entry corresponds exactly to `v0.107.1`; reject cached values from later beta builds.

Do **not** expect `/api/v1/wiki` to verify monsters or potions. Verify these through `/api/v1/compendium` Bestiary/Potion Lab or live state:

- Bygone Effigy HP, complete move sequence, powers, and A3 values.
- Fossil Stalker Strength trigger, amount, attack sequence, and A3 values.
- Living Fog, Nibbit, Slimes, Gremlin Merc, Phantasmal Gardeners, Fuzzy Wurm Crawler, all other elites, and Act 1 bosses.
- Flex Potion, Liquid Bronze, Swift Potion, and Stable Serum exact effects.

## Confidence Assessment

| Claim                                                                                | Confidence                                 | Basis                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------ | ------------------------------------------------------------------------------ |
| `v0.107.1` is the relevant main-branch build and later beta values must be separated | High                                       | Official dated patch feed and matching local run metadata                      |
| First-elite damage readiness is mandatory                                            | High                                       | Opposite local policy failures converge on the same gate                       |
| Unsupported Rupture/Body Slam/Feel No Pain packages are traps                        | High for these runs; Medium generally      | Direct deck/outcome evidence, but only one affected run                        |
| Fiend Fire was a strong missed purchase in run `1790731181`                          | Medium-High                                | Direct local postmortem; exact shop text/value not captured                    |
| Fossil Stalker requires hit-trigger/scaling handling                                 | High                                       | Official Strength-on-hit statement plus local guide/run evidence               |
| Bygone Effigy should often be raced rather than indefinitely blocked                 | Medium-High                                | Direct 23-damage/eight-turn observation; exact move table unavailable          |
| Potion trigger policy improves survival                                              | High as decision logic; Medium empirically | Three unused potions at one death and one at another; no controlled comparison |
| Individual card rankings beyond named roles                                          | Medium-Low                                 | Public wiki unavailable and no strong current guide retrieved                  |
| Boss-specific policy                                                                 | Low/Unverified                             | No current move-table source retrieved                                         |

## Missing Perspectives & Caveats

- The current STS2 wiki rejected programmatic access with `401`; Wayback had no archived Ironclad snapshot. Exact public wiki card/relic/monster pages could not be cited.
- Steam Community search returned three unrelated/adjacent guides and no substantive Ironclad guide. No strong expert guide or accessible transcript was found within the retrieval budget.
- The two local runs are both losses by the same autonomous policy and are not representative balance samples. They establish failure modes, not card win rates.
- Exact A3 enemy HP, damage, move probabilities, and boss identities were not verified. Those facts must be fetched from the current Bestiary/live state.
- Later beta notes demonstrate that many cards changed after `v0.107.1`; this report intentionally avoids back-porting those values.
- Agreement among the strongest sources mainly reflects shared local evidence plus official patch notes, not broad community consensus.

## Sources

1. [Mega Crit: Major Update #2 - v0.107.1](https://store.steampowered.com/news/app/2868840/view/710026912607505280) — primary official source, 2026-06-19.
2. [Official Slay the Spire 2 Steam News RSS](https://store.steampowered.com/feeds/news/app/2868840/?cc=US&l=english) — primary official source, generated 2026-09-29; includes later beta notes.
3. [Steam News Hub](https://store.steampowered.com/news/app/2868840) — primary official index, accessed 2026-09-29.
4. [Steam Community guide search: Ironclad](https://steamcommunity.com/app/2868840/guides/?searchText=Ironclad&browsefilter=trend&requiredtags%5B0%5D=English) — community aggregator, accessed 2026-09-29.
5. `playtests/runs/ironclad-modded-profile1-1790695747.md` — primary local run observation, 2026-09-29.
6. `playtests/runs/ironclad-modded-profile1-1790731181.md` — primary local run observation, 2026-09-29.
7. `AGENTS.md` — local operational guidance synthesized from playtests, current 2026-09-29.
8. `mcp/README.md` and `README.md` — primary local implementation documentation for wiki/compendium scope, current 2026-09-29.

## Self-Evaluation

- **Score**: 4.3/5
- **Date**: 2026-09-29T19:30:00-07:00
- **Dimension scores**: Pipeline Compliance 4, Source Diversity 3, Citation Completeness 4, Confidence Calibration 5, Scope Discipline 5, Red Team Depth 4, Depth Gate Accuracy 5
- **Lowest dimension**: Source Diversity (3) — official and local primary evidence was strong, but the public wiki was inaccessible and no substantive current Ironclad community guide was retrieved.
- **Improvements proposed**: none — none
