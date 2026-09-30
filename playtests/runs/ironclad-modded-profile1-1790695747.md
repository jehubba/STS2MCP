# STS2 Character Playtest: Ironclad

## Run Context

| Field          | Value                        |
| -------------- | ---------------------------- |
| Date           | 2026-09-29                   |
| Game build     | v0.107.1                     |
| Character      | Base-game Ironclad           |
| Profile        | modded profile 1             |
| Run ID         | `modded:profile1:1790695747` |
| Seed           | `2NYE7EAE52`                 |
| Ascension      | 3                            |
| Runtime        | 557 seconds                  |
| Outcome        | Loss, Act 1 floor 14         |
| Cause of death | Fossil Stalker               |

## Evidence

| ID  | Floor | Observation                                                                                                                                        | Classification |
| --- | ----: | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- |
| E01 |  2-12 | The agent selected a card at all seven card rewards: Rupture, Crimson Mantle, Shrug It Off, Pommel Strike, True Grit, Body Slam, and Feel No Pain. | Agent misplay  |
| E02 |     6 | Living Fog dealt 33 damage in eight turns, reducing Ironclad from 48 to 21 HP before Burning Blood.                                                | Agent misplay  |
| E03 |    11 | Phantasmal Gardeners took ten turns and dealt 29 damage despite Booming Conch's elite bonus.                                                       | Agent misplay  |
| E04 |    12 | Gremlin Merc took eleven turns and dealt 22 damage.                                                                                                | Agent misplay  |
| E05 |    14 | Fossil Stalker dealt the final 50 damage in seven turns. Flex Potion, Liquid Bronze, and Swift Potion were all unused at death.                    | Agent misplay  |

## Final State

- Deck (17): Strike x5, Defend x4, Bash, Rupture, Crimson Mantle, Shrug It Off, Pommel Strike, True Grit, Body Slam, Feel No Pain.
- Relics: Burning Blood, Booming Conch, Orichalcum, Ornamental Fan.
- Potions: Flex Potion, Liquid Bronze, Swift Potion.
- Total recorded combat damage: 178 before post-combat healing.

## Assessment

This run is not useful evidence that Ironclad is weak at Ascension 3. The result is dominated by agent policy: static card scoring, no coherent draft thesis, no potion usage, and no explicit threat/lethal calculation. The deck mixed self-damage, Block scaling, and exhaust payoffs without enough support for any one package.

## Next Experiment

Repeat Ironclad A3 with turn-level threat budgeting, skip-by-default card rewards, explicit potion triggers, and a mandatory full-state inspection for unfamiliar scaling enemies. Compare Act 1 HP loss, average combat turns, cards accepted, and potion usage against E01-E05.

## Guide Promotions

None. The durable changes belong to agent execution policy rather than Ironclad balance strategy.
