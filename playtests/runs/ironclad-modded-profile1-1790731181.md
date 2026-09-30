# STS2 Character Playtest: Ironclad Retry

## Run Context

| Field          | Value                        |
| -------------- | ---------------------------- |
| Date           | 2026-09-29                   |
| Game build     | v0.107.1                     |
| Character      | Base-game Ironclad           |
| Profile        | modded profile 1             |
| Run ID         | `modded:profile1:1790731181` |
| Seed           | `MDWX19YRRW`                 |
| Ascension      | 3                            |
| Runtime        | 1,395 seconds                |
| Outcome        | Loss, Act 1 floor 8          |
| Cause of death | Bygone Effigy elite          |

## Evidence

| ID  | Floor | Observation                                                                                                                                                                                   | Classification                              |
| --- | ----: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------- |
| E01 |     2 | Fuzzy Wurm Crawler dealt 2 damage in five turns; Burning Blood ended the fight at 68/80 HP. The agent skipped Thunderclap, True Grit, and Perfected Strike.                                   | Improved defense; questionable skip         |
| E02 |   3-4 | Sharp 2 was added to a Strike, and Taunt was selected from Brain Leech as immediate Block plus Vulnerable support.                                                                            | Coherent choice                             |
| E03 |     5 | Nibbit dealt 2 damage in four turns; the agent skipped Twin Strike, Thunderclap, and Perfected Strike.                                                                                        | Improved defense; damage need remained open |
| E04 |     6 | The Slimes encounter dealt 11 damage in five turns; the agent skipped Armaments, True Grit, and Twin Strike.                                                                                  | Agent misplay                               |
| E05 |     7 | The agent left a shop with 126 gold and bought nothing despite Fiend Fire being offered.                                                                                                      | Agent misplay                               |
| E06 |     8 | Bygone Effigy dealt 67 damage in eight turns. The agent repeatedly spent energy on Block while the elite attacked for 23, did not establish a damage race, and died with Stable Serum unused. | Agent misplay                               |

## Final State

- Deck (12): Strike x5, Defend x4, Bash, Hellraiser, Taunt. One Strike had Sharp 2.
- Relics: Burning Blood, Arcane Scroll.
- Potion: Stable Serum, unused.
- Cards accepted from normal rewards: 0 of 3.
- Event card accepted: Taunt.

## Assessment

The retry corrected the first run's indiscriminate drafting and reached floor 7 with substantially less chip damage. It then overcorrected: skip-by-default became refusal to add needed front-loaded damage, the shop policy ignored a high-impact Fiend Fire purchase, and threat budgeting became block maximization rather than damage minimization across future turns. Bygone Effigy's 23-damage attacks exceeded the deck's sustainable Block, so prolonging the fight was losing play.

This result is again dominated by agent policy and is not useful evidence about Ironclad balance. It was worse than `modded:profile1:1790695747` in progress, although it produced clearer evidence about the opposite failure mode.

## Next Experiment

Require a damage-floor check before the first Elite, value strong shop purchases against current deck needs, and optimize expected damage over the next two turns rather than current-turn Block alone. Potion policy must include utility potions such as Stable Serum when retention preserves offense or mitigation for a dangerous turn.
