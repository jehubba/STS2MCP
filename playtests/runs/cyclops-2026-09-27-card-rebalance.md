# STS2 Character Playtest: Cyclops

## Run Context

| Field               | Value                                      |
| ------------------- | ------------------------------------------ |
| Date                | 2026-09-27 to 2026-09-28                   |
| Game build          | v0.107.1                                   |
| Mod/character build | `current-local-card-rebalance-2026-09-27`  |
| STS2 MCP build      | 0.4.0 (local mod manifest)                 |
| Profile             | modded profile 1                           |
| Run ID              | `modded:profile1:1790578081`               |
| Seed                | `R8T2B2GRX2`                               |
| Ascension           | 3                                          |
| Runtime             | 4,871 seconds                              |
| Outcome             | Loss, Act 3 floor 48                       |
| Cause of death      | Test Subject boss, final life at 20/300 HP |

### Starting State

- Deck: Strike x4, Defend x4, Optic Breach, Field Training.
- Relic: Cyclops Battle Visor (whenever you break an enemy's Block, apply Vulnerable and gain 1 temporary Strength).
- Resources: 56/70 HP, 99 gold, 3 energy, 3 potion slots.
- Leadership was never offered, so the mandatory-pick rule was not triggered.
- Test focus: live changed-card values, standalone card floors, setup tempo, defensive consistency, and Leadership value if offered.
- Tooling: FastMCP trusted environment proxies and could not reach localhost. The same mod API was exercised directly at `/api/v1/singleplayer`, with polling after animation-sensitive actions.

## Run Chronology

| Checkpoint     | Result                                                                                                                                                                                                            |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Act 1          | Beat Byrdonis in 4 turns (67/70), Bygone Effigy in 3 turns (70/70), and Phrog Parasite in 7 turns (54/70). Beat Ceremonial Beast in 10 turns at 21/70.                                                            |
| Act 2          | Added the Plan/Tactical Mastery package. Beat Infested Prisms in 2 turns (64/70) and Decimillipede in 2 turns (63/70). Beat Knowledge Demon in 8 turns at 60/70.                                                  |
| Act 3 setup    | Entered at 68/70 and reached full HP. Added Wide Angle Blast+, You Know What Must Be Done+, Crippling Breach+, Mad Science+, What People See+, and Optic Blast.                                                   |
| Floor 42 elite | Beat Knights Elite in 5 turns, taking 8 damage and ending at 62/70. Chose What People See+; Leadership was not offered. Claimed Strike Dummy.                                                                     |
| Floors 43-45   | Upgraded Mad Science+. Reflections downgraded 2 random cards and upgraded 4. Sold one Foul Potion for 125 gold, then bought Bag of Preparation and Optic Blast; the merchant did not accept a second Foul Potion. |
| Floor 46       | Beat Fabricator on turn 1 at 70/70.                                                                                                                                                                               |
| Floor 47       | Upgraded You Know What Must Be Done+.                                                                                                                                                                             |
| Floor 48       | Test Subject took 13 turns. Defeated its 100-HP and 200-HP lives, then lost to its 300-HP Nemesis life with 20 HP remaining.                                                                                      |

## Reward Decisions

| Evidence ID | Floor | Source                                                 | Chosen                                                                                                                  | Result                                                                                         |
| ----------- | ----: | ------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| E01         |     1 | Neow                                                   | Phial Holster                                                                                                           | Added a fourth potion slot, Fire Potion, and Skill Potion without curse or transform variance. |
| E02         |     2 | Suppression Plan; Evasive Maneuvers; Tactical Recovery | Evasive Maneuvers                                                                                                       | The 0-energy defensive floor remained useful through the final boss.                           |
| E05         |     8 | Tactical Recovery; Plan 2; Trust Yourself              | Plan 2                                                                                                                  | Upgraded at floor 9; Plan 2+ costs 0 and kept the same transformations.                        |
| E09         | 12-17 | Combat rewards                                         | Point-Blank Shot, No Permission, Optic Explosion, Ricochet Beam, Break Their Guard                                      | Established cheap damage, multi-hit Breach, and the energy/draw engine before Act 2.           |
| E10         | 20-23 | Rewards, event, and shop                               | Suppression Plan, Bombardment, Kingly Punch, Celestial Might, Tactical Retreat, Intense Focus, Calculated Angle, Orrery | Increased flexibility and defense, but materially increased deck size.                         |
| E11         | 29-33 | Combat rewards                                         | The Art of War, Point-Blank Shot, Intense Focus, Let's Finish This                                                      | Supported the Tactical Mastery/Breach plan and cleared Knowledge Demon.                        |
| E12         | 35-40 | Rewards and events                                     | Wide Angle Blast, You Know What Must Be Done, Happy Flower, 3 Foul Potions, Crippling Breach, Mad Science               | Added draw, burst, and mitigation, but Foul Potions became unusable at 1 HP.                   |
| E13         |    42 | What People See; Evasive Maneuvers; Precision Shot     | What People See                                                                                                         | Frozen Egg upgraded it immediately. No Leadership was offered.                                 |
| E14         |    45 | Merchant                                               | Bag of Preparation and Optic Blast                                                                                      | Improved opening draw and added a free attack after selling one Foul Potion.                   |

## Changed-Card Evidence

| Evidence ID | Card or Interaction                | Live Behavior                                                                                                                                                                   | Assessment                                                                                    |
| ----------- | ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| E03         | Field Training                     | Base produced 4 Block, 5 Tactical Mastery, then either Train 1 or 1 temporary Strength and Dexterity. Field Training+ raised the base values to 6 Block and 7 Tactical Mastery. | Useful immediate floor plus setup. Reproduced in normal and elite combats.                    |
| E04         | Evasive Maneuvers                  | Remained 0 energy for 6 base Block. With 6 Dexterity during the final boss it granted 12 Block.                                                                                 | `GUIDE.md` remains current.                                                                   |
| E06         | Plan 2+                            | Costs 0. Transforms a selected hand card into Shield 5, Train 2, or Breach 5. A final-boss Wound became Shield 5 and granted 11 Block with 6 Dexterity plus 5 Tactical Mastery. | Strong status conversion and emergency defense; directly prevented death on round 11.         |
| E07         | Ricochet Beam                      | Each Breach hit independently triggered Battle Visor and Crippling Breach. The first hit also triggered Break Their Guard's once-per-turn energy refund and draw.               | Reinforces existing durable per-hit guidance.                                                 |
| E08         | Break Their Guard                  | The first Breach each turn refunded 1 energy and drew 1 card even against 0 Block.                                                                                              | Existing core-engine guidance remains accurate.                                               |
| E15         | What People See+                   | Dealt 6 damage to the lowest-HP enemy whenever any card was played. It resolved after the played card and was reduced to 1 by Intangible.                                       | Excellent with 0-cost skills and draw; made defensive turns offensive.                        |
| E16         | Suppression Plan+ / Offensive Plan | Offensive Plan cost 0, dealt 9 damage, and temporarily removed enemy Strength equal to unblocked damage.                                                                        | Reduced a `10x6` intent to `1x6`, preventing likely defeat during Test Subject's second life. |
| E17         | Mad Science+                       | Cost 1 and dealt 12 damage 3 times before Strength/Vulnerable scaling.                                                                                                          | Very efficient burst; displayed 19 damage 3 times after final-life Breach setup.              |
| E18         | You Know What Must Be Done+        | Cost 0, gained 1 energy, drew 3 cards, and Exhausted.                                                                                                                           | Strong immediate acceleration.                                                                |
| E19         | Reflections                        | Downgraded 2 random cards and upgraded 4 random cards.                                                                                                                          | Positive net upgrade count, but random results complicate card-level conclusions.             |

## Final Boss Evidence

Test Subject had sequential 100-HP, 200-HP, and 300-HP lives. The final life had Nemesis and alternated Intangible turns.

- Offensive Plan was the decisive second-life survival tool, reducing `10x6` to `1x6`.
- The player survived a later 45-damage hit at exactly 1 HP and remained at 1 HP.
- Round 10: The Art of War+ into Mad Science+ reduced the final life from 178 to 98 while preserving enough energy to block `12x3`.
- Round 11: Plan 2+ converted a Wound into Shield 5. Point-Blank Shot+, Calculated Angle+, and Shield 5 produced 56 Block against 47 damage while chipping through Intangible.
- Round 12: Optic Breach opened Vulnerable and drew Field Training+. Let's Finish This plus two skills reduced the boss from 68 to 31 while building 35 Block on a non-attacking turn.
- Round 13: the boss had Intangible and intended `14x3`. Wide Angle Blast+ drew Ricochet Beam; Ricochet Beam drew Defend+. The best line reached 34 Block and reduced the boss from 31 to 20, but could neither block 42 nor kill through Intangible. The player took 8 unblocked damage from 1 HP.
- Two remaining Foul Potions were unusable because each would deal 12 damage to the player.

## Final Snapshot

### Deck (32 cards)

- Defend+ x3; Defend x1.
- Optic Breach; Field Training+; Evasive Maneuvers; Point-Blank Shot+ x2; No Permission+.
- Optic Explosion; Ricochet Beam; Break Their Guard; Suppression Plan+; Plan 2+.
- Bombardment+; Celestial Might+; Tactical Retreat+; Intense Focus+ x2.
- Calculated Angle+; Tactical Mastery; Ultimate Strike; Master of Strategy+.
- The Art of War+; Let's Finish This; Wide Angle Blast+; You Know What Must Be Done+.
- Crippling Breach+; Mad Science+; What People See+; Optic Blast.

All four starting Strikes were removed or combined by events and shops. The Amalgamator combined two into Ultimate Strike; later removals eliminated the remaining two.

### Relics (19)

Cyclops Battle Visor, Phial Holster, Planisphere, Ember Tea, Blood Vial, Akabeko, War Paint, Very Hot Cocoa, Orrery, Gorget, Anchor, Ringing Triangle, Frozen Egg, Bowler Hat, Choices Paradox, Happy Flower, Whetstone, Strike Dummy, and Bag of Preparation.

### Potions and Resources

- 0/70 HP, 27 gold.
- Foul Potion in slots 0 and 2; 4 total potion slots.

## Run Assessment

The rebalance build cleared two acts, the Act 3 elite, Fabricator, and the first two Test Subject lives. The final loss was close: 20 boss HP remained after 13 turns.

The strongest changed-card evidence is positive. Field Training had a real defensive floor, Plan 2+ converted status pollution into emergency defense, What People See+ made defensive and free-card turns offensive, Offensive Plan prevented a lethal multi-hit sequence, and Mad Science+ delivered unusually efficient burst. These cards improved both setup tempo and defensive flexibility.

The run did not demonstrate consistent late-boss defense. The final deck reached 32 cards, Test Subject added Wounds and Burns, and critical Break Their Guard draws could still find statuses or insufficient Block. Strong individual defensive tools did not guarantee access on alternating Intangible attack turns. Potion quality also collapsed at 1 HP.

### Confounders

- Agent play: no known lethal targeting or index error affected the terminal fight. The final round's maximum available Block was 34 against 42, and Intangible capped each damage instance at 1. Earlier reward discipline was loose; reaching 32 cards likely reduced access to key defense and setup.
- Game variance: Reflections, Choices Paradox, boss status insertion, and final draw order materially affected the result.
- Relic dependence: Frozen Egg upgraded What People See; Bag of Preparation, Very Hot Cocoa, Anchor, Ringing Triangle, and Battle Visor materially improved combat starts.
- Tooling: direct HTTP was required. Some actions required polling through delayed damage, draw, revival, and transition animations.
- Ambiguous interaction: only one Foul Potion could be sold at the floor 45 merchant. This may be a per-merchant rule rather than a bug.

### Next Experiments

1. Repeat What People See+ with a smaller deck and track damage per draw cycle, especially on defensive turns.
2. Re-test Suppression Plan into Offensive Plan against multi-hit bosses and record exact pre/post intent.
3. Compare Mad Science+'s 1-energy burst against other rare attacks without Battle Visor/Vulnerable support.
4. Track Plan 2+ status conversions over a full run, including how often Shield 5 prevents damage.
5. Preserve the mandatory Leadership pick rule. This run supplied no Leadership offer and no evidence for or against its value.
6. Apply stricter late-run skip discipline and avoid carrying self-damaging potions into a low-HP boss when replacement or sale is available.

## Telemetry

- Ledger record: `modded:profile1:1790578081`.
- Eligibility: eligible; `development_test=false`; not abandoned.
- Cohort: Cyclops, Ascension 3, game build v0.107.1, mod version `current-local-card-rebalance-2026-09-27`.
- Cohort totals: 1 eligible run, 0 wins, 1 loss; win rate 0/1 (Wilson 95% interval 0.000-0.793).
- Report path: `playtests/runs/cyclops-2026-09-27-card-rebalance.md`.

## Guide Promotions

No `GUIDE.md` change is warranted from this single run.

- Evasive Maneuvers remains 0 energy for 6 base Block.
- Shield 5 remains 5 base Block plus 5 Tactical Mastery.
- Ricochet Beam's per-hit Breach triggering is reinforced, not contradicted.
- What People See+, Offensive Plan, Mad Science+, You Know What Must Be Done+, and Plan 2+ need another run or repeated controlled encounters before becoming durable guidance.
