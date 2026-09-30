# STS2 Character Playtest: Ironclad Researched Retry

## Run Context

| Field          | Value                        |
| -------------- | ---------------------------- |
| Date           | 2026-09-29                   |
| Game build     | v0.107.1                     |
| STS2 MCP build | Mod 0.4.0 / server 0.1.0     |
| Character      | Base-game Ironclad           |
| Profile        | modded profile 1             |
| Run ID         | `modded:profile1:1790735201` |
| Seed           | `UUFHKVAL8S`                 |
| Ascension      | 3                            |
| Runtime        | 10,234 seconds               |
| Outcome        | **Win, Act 3 floor 48**      |
| Final combat   | Aeonglass, 7 turns           |

The immutable `.run` record has `win: true`, `was_abandoned: false`, and no death encounter or event. Aeonglass ended at 75/96 HP; the post-boss Architect narrative gateway then normalized the displayed game-over HP to 0.

## Evidence

| ID  | Floor | Observation                                                                                                                                                                                                                                              | Classification                    |
| --- | ----: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------- |
| E01 |   2-8 | Cinder+, Breakthrough+, Battle Trance+, Pommel Strike+, and Hellraiser+ supplied early damage, draw, and a supported Strike package before the first elite.                                                                                              | Coherent drafting                 |
| E02 |    11 | Terror Eel was cleared in 3 turns at 53/80 HP; Vulnerable Potion was spent rather than carried through the elite.                                                                                                                                        | Improved potion use               |
| E03 |    17 | Waterfall Giant was cleared in 7 turns at 53/96 HP after 36 damage taken and 6 Burning Blood healing.                                                                                                                                                    | Act 1 clear                       |
| E04 | 25-31 | Four Act 2 elite/monster combats used six potions, including renewable Potion-Shaped Rocks. Entomancer was the costliest at 33 damage; the run responded by resting before the boss.                                                                     | Resource discipline               |
| E05 |    33 | The Insatiable was cleared in 4 turns at 52/96 HP. Orobic Acid, Stable Serum, and Block Potion were all spent.                                                                                                                                           | Act 2 clear                       |
| E06 |    45 | Globe Head was killed on turn 1. Attack Potion generated a free Bludgeon; duplicated Offering enabled a full burst turn, ending at 89/96 after Burning Blood. Fire and Blood potions were preserved because lethal did not require them.                 | Sequencing and lethal calculation |
| E07 |    46 | Mecha Knight was cleared in 4 turns at 69/96. Duplicated Rupture+, Crimson Mantle+, and Inferno+ converted player-turn HP loss into recurring Strength, Block, and damage. Fysh Oil was used on turn 1.                                                  | Supported scaling engine          |
| E08 |    48 | Aeonglass was cleared in 7 turns at 75/96. Energy Potion funded Inferno+, a second Crimson Mantle, and Blood Wall on the same defensive turn. Fiend Fire later exhausted two Wither+1 cards and Breakthrough+ for 69 damage.                             | Boss execution                    |
| E09 |    48 | Aeonglass's Withering Presence counted down with cards played, then generated Wither. Its later buff generated Wither+1, which dealt 6 blockable end-turn damage. Second Wind+ removed generated statuses, but its exhaust animation resolved in stages. | Verified encounter mechanic       |
| E10 |    48 | Ruined Helmet doubled Fight Me!+'s first 4-Strength gain to 8. The Crimson Mantle/Rupture/Inferno engine then reduced Aeonglass from 166 to 46 between player turns before Fight Me!+ dealt lethal.                                                      | Relic-engine synergy              |
| E11 |   Run | The final deck had 31 cards and 15 relics. It was not lean, but its additions reinforced three connected packages: Ember Strikes/Hellraiser, player-turn HP loss/Rupture, and exhaust/Joss Paper/Fiend Fire.                                             | Supported large deck              |
| E12 |   Run | The two previous retries died on floors 14 and 8. This run cleared floor 48 after applying researched damage floors, two-turn threat budgeting, proactive potion triggers, shop spending, and late reward skips.                                         | Policy improvement                |

## Final State

- Deck (31): Strike x5, Defend x4, Bash, Cinder+, Breakthrough+, Headbutt, Pommel Strike+, Hellraiser+, Blood Wall, Setup Strike, Crimson Mantle+, Offering, Battle Trance+, Breakthrough, Unmovable, Fiend Fire, Fight Me!+, Crimson Mantle, Shrug It Off+, Inferno+, Rupture+, Tremble, Second Wind, Shrug It Off.
- Relics (15): Burning Blood, Silver Crucible, Joss Paper, Pear, Nutritious Soup, Lantern, Parrying Shield, Petrified Toad, Festive Popper, Lost Wisp, Tiny Mailbox, Throwing Axe, Razor Tooth, Sturdy Clamp, Ruined Helmet.
- Potions remaining: Fire Potion and Blood Potion.
- Gold: 81.
- Final boss result: 27 damage taken, 6 healed, 7 turns, Energy Potion used.

## Interaction and Anomaly Log

| ID  | Before State                                                      | Action                             | Result                                                                                                                  | Category                     |
| --- | ----------------------------------------------------------------- | ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ---------------------------- |
| A01 | Throwing Axe ready; Offering in hand                              | Played Offering as the first card  | Both 6-HP losses appeared before the duplicated energy and draws fully settled. Later polls exposed the second payload. | Asynchronous resolution      |
| A02 | Razor Tooth active; base cards displayed upgraded text after play | Played Setup Strike and Blood Wall | The current play used the pre-upgrade value; Razor Tooth upgraded the card only for later plays that combat.            | Display/timing clarification |
| A03 | Aeonglass hand contained Wither/Wither+1                          | Played Second Wind/Second Wind+    | Status exhaust and Block gains completed across multiple state polls rather than one acknowledgment.                    | Asynchronous resolution      |
| A04 | Aeonglass defeated at 75/96                                       | Completed The Architect event      | Live state reported `game_over` and HP 0, while the immutable run recorded `win: true`.                                 | Result-state ambiguity       |

## Assessment

The researched policy change succeeded. The deck solved its early damage requirement, spent gold and potions against immediate threats, and built around interactions already present rather than collecting isolated packages. The decisive late engine was player-turn HP loss: Crimson Mantle and Inferno supplied repeatable triggers, Rupture converted them to Strength, and Unmovable/Sturdy Clamp made the Block side sustainable. Fiend Fire and Second Wind gave the same deck status cleanup against Aeonglass instead of serving as speculative exhaust picks.

This run does not establish that a 31-card deck is generally optimal. Relic support was unusually broad, and the Ancient transitions supplied substantial healing. It does show that deck size alone is a poor quality proxy when additions are independently useful and reinforce existing engines.

## Comparison With Failed Runs

| Run                          | Result                  | Main policy failure                                                                                                                 |
| ---------------------------- | ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| `modded:profile1:1790695747` | Loss, Act 1 floor 14    | Drafted every reward, mixed unsupported packages, and died with three potions unused.                                               |
| `modded:profile1:1790731181` | Loss, Act 1 floor 8     | Skipped all normal rewards and a strong shop card, then overblocked against unsustainable damage and died with Stable Serum unused. |
| `modded:profile1:1790735201` | **Win, Act 3 floor 48** | Balanced immediate damage, supported scaling, mitigation, and proactive consumable use; skipped redundant late rewards.             |

## Balance Conclusions

- No card or relic nerf is justified from one winning run. Relic density and event healing are major confounders.
- The Crimson Mantle/Rupture/Inferno package had a high ceiling, but required three specific cards and recurring HP payment before becoming decisive.
- Fiend Fire was strong both as burst and status cleanup, but its value depended on exact hand composition and energy.
- Ruined Helmet plus Fight Me!+ was a powerful late pickup interaction; evidence is insufficient to separate relic strength from the complete engine around it.

## Next Experiment

Repeat Ironclad Ascension 3 with the same policy but track reward acceptance by deck need and test whether the HP-loss engine remains reliable without Throwing Axe, Sturdy Clamp, or Ruined Helmet. Preserve exact before/after state around Razor Tooth to distinguish displayed upgraded text from the value used on the current play.
