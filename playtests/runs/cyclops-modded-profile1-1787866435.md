# STS2 Character Playtest: Cyclops

## Run Context

| Field               | Value                       |
| ------------------- | --------------------------- |
| Date                | 2026-08-28                  |
| Game build          | unknown                     |
| Mod/character build | unknown                     |
| STS2 MCP build      | 0.4.0 (local mod manifest)  |
| Profile             | modded profile 1            |
| Run ID              | modded:profile1:1787866435  |
| Seed                | 0UEASR0A8L                  |
| Ascension           | 0                           |
| Outcome             | Defeat - Act 1 floor 11     |
| Cause of death      | Two Nibbits, round 3: 22 combined incoming damage exceeded 8 available Block at 7 HP; the best attack line left the second attacker at 5 HP. |

### Starting State

- Deck: unknown. This session adopted the run at Act 1 floor 2 post-combat rewards; the reward-state endpoint did not expose the deck.
- Relic: exact pre-floor-2 pickup sequence unknown. At adoption, Phoenix Force Visor and Neow's Talisman were present; Neow's Talisman had upgraded one Strike and one Defend.
- Character resources/mechanics: Phoenix Force Visor makes Strikes deal Breach damage; breaking enemy Block applies Vulnerable and grants 1 temporary Strength. Other startup details are unknown.
- Test questions: How consistently does Breach convert blocked enemies into offensive tempo? Which offered cards provide a defensible floor without dedicated support? How costly are Cyclops setup and resource constraints in normal routing?
- Telemetry limitations: Opening context is partially observed. Pre-floor-2 startup choices, the first combat, its encounter, card actions, turn count, and HP transition are unknown/missing evidence and are not inferred. This is a tooling/session confounder. The metadata-free bootstrap succeeded with 58 total records, 20 eligible runs, 0 wins, 20 losses, and 38 abandoned runs. The active endpoint did not expose game or Cyclops-mod build versions. STS2 MCP 0.4.0 is taken from the local mod manifest rather than a runtime self-report.

## Reward Decisions

| Evidence ID | Floor | Offered | Chosen/Skipped | Deck Need | Hypothesis | Result |
| ----------- | ----: | ------- | -------------- | --------- | ---------- | ------ |
| E01 | 2 | Optic Breach; Give Them the Forecast; Rally | Optic Breach | Low-cost offense that directly exercises the Visor's Block-broken trigger. | A 1-energy non-Strike Breach attack should have a defensible floor at 7 damage and reveal whether repeated Breach access reliably creates Vulnerable/temporary Strength tempo against blocked enemies. | E04-E05: played twice in floor 5 combat; each play dealt 10 to a Vulnerable target and triggered Visor at 0 enemy Block. |
| E02 | 3 shop | Maximum Optic Blast; Give Them the Forecast; Exploit Weakness; Tactical Recovery; Field Commander; Mind Blast; Gold Axe | Field Commander (50 gold); Exploit Weakness (38 gold) | Recurring defensive retention support plus 0-cost offense setup when enemies have no Block. | Field Commander's two Tactical Mastery per turn should improve defensive consistency enough to justify a 1-energy setup turn; Exploit Weakness should distinguish unconditional Vulnerable tempo from Visor-dependent setup. | E04: Exploit Weakness enabled 2 Vulnerable for 0 energy; Swift Field Commander drew 2 immediately. Defensive retention was not exercised because the enemy died before another attack. |
| E03 | 4 event | Sharp 2 on an Attack; Nimble 2 on a Skill; Swift 2 on a Power | Swift 2 on Field Commander | Offset Field Commander's setup cost without adding another card. | Drawing two cards on Field Commander's first play should materially reduce its tempo loss while preserving its recurring defensive value. | E04: event auto-targeted the only Power. First play consumed 1 energy, drew exactly 2 cards, and left 2 energy; enchantment confounds evaluation of the base form. |
| E06 | 5 | Trust Yourself; Plan 2; Concussive Beam | Plan 2 | Flexible conversion among Block, Train, and Breach to support both defensive retention and Visor offense. | Mode flexibility should repay the 1-energy setup and consumed hand card when temporary stats need training or an enemy presents Block; otherwise it may be an awkward two-card action. | E11/E17: converted three hand cards into free Shield 5 tokens; each was played, but only the defensive mode was observed. |
| E09 | 6 | Optic Breach; Countermeasures; Exploit Weakness | Countermeasures | Persistent defense that tests an unfamiliar card without adding a third Optic Breach or a redundant second Exploit Weakness. | Two Thorns should have a defensible floor against multi-hit or longer encounters, but its 1-energy setup may compete awkwardly with Field Commander. | E11/E14: returned 2 damage after attacks and reduced Inklet from 3 to 1 while retained Block prevented damage; setup competition remains a confounder. |
| E12 | 8 elite | Break Their Guard; Rapid Punch; Optic Explosion | Break Their Guard | Convert the deck's frequent Breach triggers into energy and draw while avoiding another low-output attack or a 3-energy attack that consumes the full turn. | Triggering the Power once per turn should repay its setup cost quickly and reduce the hand/energy bottleneck observed against Bygone Effigy; its floor depends on drawing a Breach attack afterward. | E17: after setup, Optic Breach against zero Block refunded its energy, forced a reshuffle, and drew Defend+; the defense was still insufficient against 22 incoming damage. |
| E13 | 8 elite | 43 gold; Orichalcum | Claimed both | Immediate survivability at 15 HP plus enough gold for a future shop. | Orichalcum should reduce damage on offense/setup turns that end at 0 Block, though generated Block can make it redundant. | Acquired Orichalcum and 43 gold; 105 gold after rewards. |
| E15 | 9 | Suppressive Breach; Evasive Maneuvers; We Don't Lose, We Regroup | Evasive Maneuvers | Immediate survival at 11 HP without consuming energy. | Zero-cost Block should combine efficiently with Defends and Field Commander retention, but playing it alone may be worse than ending at 0 Block because it suppresses Orichalcum's 6 Block. | E17: combined with Defend for 9 Block at 1 total energy and prevented all 6 incoming damage; no lone-card Orichalcum conflict was observed. |
| E16 | 10 treasure | 44 gold; Pantograph | Claimed both | Preserve the critically low-HP run through the Act 1 boss. | Pantograph's 25 boss-start healing should materially improve survival if Cyclops reaches the boss, while the gold supports a later shop. | Acquired Pantograph; 165 gold after the chest. |

## Combat Evidence

| Evidence ID | Floor | Encounter | Turns | HP Before/After | Notable Plays | Constraint or Dead Draw | Classification |
| ----------- | ----: | --------- | ----: | --------------- | ------------- | ----------------------- | -------------- |
| E00 | 2 | unknown (completed before adoption) | unknown | unknown/69 | All card actions and combat details unavailable. | unknown | tooling |
| E04 | 5 | Fuzzy Wurm Crawler | 2 | 69/65 | Turn 1 Exploit Weakness applied 2 Vulnerable for 0 energy; Optic Breach dealt 10 and triggered Visor; Call Storm generated Chain Lightning. Turn 2 Swift Field Commander drew 2; a second Optic Breach dealt 10 and triggered Visor; Chain Lightning killed from 36 HP. | Call Storm consumed the remaining 2 energy on turn 1, so 4 incoming damage was accepted. Field Commander's Tactical Mastery did not receive a defensive test before lethal. | balance (exploratory) |
| E07 | 6 | Twig Slime (M) | 4 | 65/65 | Session resumed on round 3 with the enemy at 27 HP and status-only intent. Optic Breach dealt 7 at 0 Block and applied 1 Vulnerable; Call Storm generated Chain Lightning, which dealt 21 to the lone enemy for round-4 lethal. | Rounds 1-2 actions are unknown. Three Slimed statuses entered the deck during the combat; no resumed-session damage was taken. | tooling; balance (exploratory) |
| E11 | 8 | Bygone Effigy (elite) | 8 | 65/15 | Session resumed on round 4 at 65 HP, 6 Block, and 0 energy. Round 5 used two Defends then base Optic Breach for 12 damage. Rounds 6-7 each used Plan 2 to convert a hand card into Shield 5, then paired the free Shield with Defend+ and an attack; Optic Breach+ dealt 19 on round 6 and Strike+ dealt 17 on round 7. Optic Breach+ dealt lethal from 13 HP on round 8. Thorns returned 2 after each resumed enemy attack. | Rounds 1-3 actions, draws, and playable opportunities are unknown. The enemy had 10 Strength and attacked for 23 every resumed round; defensive conversion still cost 50 HP across the full combat. | tooling; balance (exploratory) |
| E14 | 9 | Inklet | 4 | 15/11 | The round-3 resume state showed Break Their Guard, Thorns from Countermeasures, and Field Commander active. At 0 energy, 8 Block covered the 3-damage intent; Thorns reduced Inklet from 3 to 1. Round 4 base Strike dealt lethal. | Rounds 1-2 ordering, draws, and playable opportunities are unknown. Persistent-power setup cost 4 HP before resume, but retained Block plus Thorns made round 3 damage-free. | tooling; balance (exploratory) |
| E17 | 11 | Two Nibbits | 3 | 11/0 | Round 1 Evasive Maneuvers plus Defend gained 9 Block for 1 energy, then Swift Field Commander and Break Their Guard were installed. Round 2 Plan 2 converted Strike into Shield 5; Shield plus Defend gained 10 Block against 14. Round 3 Optic Breach triggered Visor and Break Their Guard at zero Block, refunded 1 energy, forced a reshuffle, and drew Defend+. Optic Breach, Strike+, and Strike dealt 10, 15, and 12 to the Vulnerable attacker, leaving it at 5 HP. | The enemies alternated buffs and attacks, scaling to 22 combined damage on round 3. Defend+ was the only defensive draw after the trigger and provided 8 Block; no line could block 16 or kill either enemy before the attacks. | game variance; balance (exploratory) |

## Card Play Counts

Counts reflect this agent's successful `combat_play_card` actions, not cards merely drawn or generated. A playable opportunity is an observed draw where the card could legally be played and could plausibly advance the turn's objective. Use `unknown` when telemetry cannot establish a count. Counts begin after adoption at the floor 2 reward screen; first-combat plays are unknown and excluded.

| Card ID | Form | Acquired Floor | Upgraded Floor | Copies | Draws Observed | Playable Opportunities | Plays | Dead/Awkward Draws | Evidence IDs |
| ------- | ---- | -------------: | -------------: | -----: | -------------: | ---------------------: | ----: | -----------------: | ------------ |
| CYCLOPSMOD-OPTIC_BREACH | Upgraded, inherited copy | unknown (before adoption) | 7 | 1 | 2 after upgrade | 2 after upgrade | 2 after upgrade | 0 observed after upgrade | E00, E04, E05, E07, E10-E11 |
| CYCLOPSMOD-OPTIC_BREACH | Base, adopted-session copy | 2 | N/A | 1 | unknown | unknown | 5 aggregate base-form plays across both copies | 0 observed aggregate | E01, E04, E05, E07, E11, E17 |
| CYCLOPSMOD-FIELD_COMMANDER | Base + Swift 2 | 3 | N/A | 1 | at least 3 | at least 3 | 3 | 0 observed | E02-E04, E14, E17 |
| CYCLOPSMOD-EXPLOIT_WEAKNESS | Base | 3 | N/A | 1 | at least 2 | at least 2 | 2 | 0 | E02, E04, E17 |
| CYCLOPSMOD-PLAN_2 | Base | 5 | N/A | 1 | 3 post-resume | 3 post-resume | 3 post-resume | 0 post-resume | E06, E11, E17 |
| CYCLOPSMOD-COUNTERMEASURES | Base | 6 | N/A | 1 | at least 1 | at least 1 | 1 | 0 observed | E09, E14 |
| CYCLOPSMOD-CALL_STORM | Base | unknown (before adoption) | N/A | 1 | 2 | 2 | 2 | 0 | E04, E07 |
| CYCLOPSMOD-CHAIN_LIGHTNING | Generated token | 5 | N/A | 0 | 2 | 2 | 2 | 0 | E04, E07 |
| CYCLOPSMOD-CYCLOPS_DEFEND | Base starter | before adoption | N/A | 2 | 4 post-resume | 4 post-resume | 4 post-resume | 0 post-resume | E11, E17 |
| CYCLOPSMOD-CYCLOPS_DEFEND | Upgraded starter | before adoption | before adoption | 1 | 3 post-resume | 3 post-resume | 3 post-resume | 0 post-resume | E11, E17 |
| CYCLOPSMOD-CYCLOPS_STRIKE | Upgraded starter | before adoption | before adoption | 1 | 2 post-resume | 2 post-resume | 2 post-resume | 0 post-resume | E11, E17 |
| CYCLOPSMOD-CYCLOPS_STRIKE | Base starter | before adoption | N/A | 2 | at least 2 post-resume | at least 2 post-resume | 2 post-resume | 0 post-resume | E14, E17 |
| CYCLOPSMOD-SHIELD_FIVE | Generated token | 8 | N/A | 0 | 3 post-resume | 3 post-resume | 3 post-resume | 0 post-resume | E11, E17 |
| CYCLOPSMOD-BREAK_THEIR_GUARD | Base | 8 | N/A | 1 | at least 2 | at least 2 | 2 | 0 observed | E12, E14, E17 |
| CYCLOPSMOD-EVASIVE_MANEUVERS | Base | 9 | N/A | 1 | 1 | 1 | 1 | 0 | E15, E17 |
| CYCLOPSMOD-FIELD_TRAINING | Base, inherited | before adoption | N/A | 1 | at least 2 | 0 observed | 0 post-adoption | at least 2 | E14, E17 |
| CYCLOPSMOD-CALL_WOLVERINE | Base, inherited | before adoption | N/A | 1 | at least 2 | 0 observed | 0 post-adoption | at least 2 | E14, E17 |

## Upgrade Comparisons

| Card ID | Before Evidence | After Evidence | Observed Delta | Confounders | Confidence |
| ------- | --------------- | -------------- | -------------- | ----------- | ---------- |
| CYCLOPSMOD-OPTIC_BREACH | E04, E07, E11: base form cost 1 and dealt 7 before Vulnerable, 10 with Vulnerable, or 12 after two Slow-building cards plus Vulnerable. | E11: upgraded form cost 1; dealt 19 after three Slow-building cards plus Vulnerable and 15 for unamplified Vulnerable lethal. | Base damage increased from 7 to 10 at unchanged cost; direct same-state damage comparison was not observed. | The 12-versus-19 observed hits had different Slow stacks, so the practical damage delta is not isolated. | low |

## Checkpoints

### Adoption: Act 1 Floor 2 Post-Combat Rewards

- Floor and HP: Act 1 floor 2, 69/70 HP.
- Deck and upgrades: deck unknown from current endpoint; Neow's Talisman states that one Strike and one Defend were upgraded.
- Relics and potions: Phoenix Force Visor; Neow's Talisman; no potions; 99 gold before claiming rewards.
- Central engine: Breach Strikes triggering Phoenix Force Visor on blocked enemies.
- Scaling speed: unknown.
- Defensive consistency: unknown.
- Current balance flags: none; insufficient observed evidence.

### Rest Site: Act 1 Floor 7

- Floor and HP: Act 1 floor 7, 65/70 HP.
- Deck and upgrades: 13 cards; Strike+, Defend+, and the inherited Optic Breach+ after smithing. Base Optic Breach evidence existed before the upgrade; the preview showed 7 to 10 damage at unchanged 1-energy cost.
- Relics and potions: Phoenix Force Visor; Neow's Talisman; Speed Potion.
- Central engine: Breach attacks and Visor Vulnerable tempo, with Swift Field Commander for recurring Tactical Mastery.
- Scaling speed: Exploit Weakness or a Breach hit establishes Vulnerable immediately; persistent powers still require setup energy.
- Defensive consistency: Field Commander retained 2 Block into the resumed floor 6 turn, but no damaging turn has yet isolated its prevented damage.
- Current balance flags: `E05`/`E08` zero-Block Visor trigger remains surprising; Optic Breach upgrade comparison opened as `E10`.

### Elite: Act 1 Floor 8

- Floor and HP: Act 1 floor 8, 15/70 HP after Bygone Effigy.
- Deck and upgrades: 13 cards; Strike+, Defend+, and inherited Optic Breach+.
- Relics and potions: Phoenix Force Visor; Neow's Talisman; Orichalcum acquired from the elite; no potions after the pre-combat Speed Potion was consumed during unobserved rounds 1-3.
- Central engine: repeated Breach triggers maintained Vulnerable; Plan 2 converted low-value hand cards into free Shield 5 twice after resume.
- Scaling speed: damage scaled strongly with the elite's Slow debuff, but the deck required eight turns to deal 127 HP.
- Defensive consistency: two Plan 2-to-Shield conversions plus Defend+ produced 13 Block on consecutive turns, reducing each 23-damage attack to 10; total combat loss was still 50 HP.
- Current balance flags: zero-Block Visor trigger reproduced with base and upgraded Optic Breach and Strike+; Plan 2 showed a useful defensive mode but required a two-step selection flow and another hand card.

### Run End: Act 1 Floor 11

- Floor and HP: Act 1 floor 11, 0/70 HP after entering at 11 HP.
- Deck and upgrades: 17 cards; Strike+, Defend+, Optic Breach+, and 14 base cards. The full combat pile exposed inherited Field Training and Call Wolverine that earlier reward-state endpoints had hidden.
- Relics and potions: Phoenix Force Visor; Neow's Talisman; Orichalcum; Pantograph; no potions.
- Central engine: Swift Field Commander supplied recurring Tactical Mastery; Break Their Guard converted the first zero-Block Breach each turn into energy and draw; Plan 2 converted attacks into emergency Shield 5.
- Scaling speed: two setup Powers consumed 2 energy on floor-11 round 1. By round 3, repeated Breach triggers produced 37 observed damage from three attacks but missed lethal by 5 HP.
- Defensive consistency: Evasive Maneuvers plus Defend efficiently covered round 1, and Plan 2 plus Defend limited round 2 to 4 damage. The round-3 reshuffle produced only Defend+ against 22 incoming damage.
- Current balance flags: zero-Block Visor/Break Their Guard triggers are highly consistent and powerful; setup-heavy hands and low absolute Block remain severe failure modes at critical HP.

## Interaction and Anomaly Log

| Evidence ID | Floor | Before State | Action | Resulting State | Category | Reproduced? |
| ----------- | ----: | ------------ | ------ | --------------- | -------- | ----------- |
| E05 | 5 | Fuzzy Wurm Crawler had 0 Block and 2 Vulnerable; player had no Strength. | Played Optic Breach. Repeated next turn with enemy again at 0 Block and 2 Vulnerable. | Each play dealt 10, raised Vulnerable from 2 to 3, and granted 1 temporary Strength despite 0 enemy Block. | interaction; potentially surprising wording, not established as bug | Yes, twice in one combat. |
| E08 | 6 | Twig Slime (M) had 0 Block and no status; player had no temporary Strength. | Played Optic Breach. | Dealt 7, applied 1 Vulnerable, and granted temporary Strength despite 0 enemy Block. | interaction; potentially surprising wording, not established as bug | Yes; third directly observed trigger across two combats when combined with E05. |
| E17 | 11 | Break Their Guard was active; draw pile was empty; Nibbit had 0 Block and 1 Vulnerable; Cyclops had 3 energy and no Block cards in hand. | Played Optic Breach for 1 energy. | Dealt 10, raised Vulnerable to 2, granted temporary Strength, restored energy from 2 to 3, reshuffled the discard pile, and drew Defend+. | interaction | Yes; reproduces zero-Block Visor and Break Their Guard triggers. |

## Card Evaluation

| Card | Evidence IDs | Floor | Ceiling | Consistency | Cost | Upgrade | Failure Mode | Confidence |
| ---- | ------------ | ----- | ------- | ----------- | ---- | ------- | ------------ | ---------- |
| Optic Breach | E04-E05, E07-E08, E10-E11, E17 | High: reliable damage plus Vulnerable and temporary Strength even at zero Block. | With Break Their Guard, the first trigger can refund energy and draw; Vulnerable and Strength raised later attacks to 15 and 12 at E17. | Played whenever observed and useful; zero-Block trigger reproduced across four combats. | 1 energy. | Base damage rose 7 to 10; no same-state comparison. | Does not provide defense, and the strong trigger package still could not overcome E17's incoming damage. | medium for value; high for interaction |
| Field Commander | E02-E04, E14, E17 | Swift 2 offsets the first 1-energy setup by drawing two cards. | Recurring Tactical Mastery supports Block retention in longer fights. | Three successful plays; enchantment confounds the base card. | 1 energy Power and an opening draw slot. | Not observed. | Setup competes with immediate damage or Block; retained Block did not solve E17's burst. | low |
| Plan 2 | E06, E11, E17 | Flexible emergency defense; three Shield 5 conversions reduced damage in two combats. | Can convert an otherwise low-value card into Block without further energy. | Played in all three observed post-resume opportunities. | 1 energy plus another hand card and a two-step selection. | Not observed. | Requires a disposable card; 5 Block is insufficient against large multi-enemy bursts. | medium |
| Countermeasures | E09, E11, E14 | Two Thorns supplied chip damage while blocking, including reducing Inklet from 3 to 1. | Better against repeated or multi-hit attacks. | One proven setup; no isolated comparison. | 1 energy Power. | Not observed. | Slow against high single-hit pressure and can compete with other setup Powers. | low |
| Break Their Guard | E12, E14, E17 | First Breach each turn can become effectively free and draw a card. | E17 forced a reshuffle and found Defend+ from an otherwise attack-only hand. | Triggered at zero Block when observed after setup. | 1 energy Power before any return. | Not observed. | Late setup or a weak follow-up draw can fail to prevent lethal. | medium |
| Evasive Maneuvers | E15, E17 | Four Block for 0 energy combined with Defend to cover a 6-damage attack efficiently. | May support setup turns and Tactical Mastery without consuming energy. | One draw and one play. | 0 energy and one draw slot. | Not observed. | Four Block is low in isolation and can suppress Orichalcum's 6 Block if played alone. | low |

## Run Assessment

### Character Thesis

Cyclops is a setup-tempo character whose Breach attacks reliably activate Phoenix Force Visor and Break Their Guard even against zero Block. This produces Vulnerable, temporary Strength, energy, and draw for strong attack chains. Field Commander and Plan 2 provide a defensive model based on retained Block and flexible hand conversion, but installing several Powers costs early tempo and the observed Block values were too small to absorb scaled multi-enemy pressure after the elite reduced the run to critical HP.

### Strongest Evidence

- Observation: E05, E08, E11, and E17 repeatedly showed Breach attacks and Visor-enhanced Strikes triggering Block-broken effects against zero Block. At E17, Optic Breach restored its energy and drew Defend+ through Break Their Guard.
- Interpretation: The Breach engine is highly consistent and does not require enemies to present positive Block, making Break Their Guard much less conditional than its wording suggests.
- Observation: E17 showed Evasive Maneuvers plus Defend cover 6 incoming damage for 1 energy, and Plan 2 plus Defend limit 14 damage to 4; the next hand could produce only 8 Block against 22.
- Interpretation: Cyclops's flexible defense has a useful floor but lacks compact burst protection when multiple enemies scale together.

### Balance Flags

| Subject | Flag | Observation IDs | Interpretation | Confounders | Recommendation | Tradeoff | Confidence |
| ------- | ---- | --------------- | -------------- | ----------- | -------------- | -------- | ---------- |
| Phoenix Force Visor and Break Their Guard | Potentially over-consistent zero-Block engine | E05, E08, E11, E17 | Effects worded around breaking Block triggered repeatedly when targets had no Block, supplying Vulnerable, temporary Strength, energy, and draw. | This may be the intended definition of Breach and the character's baseline engine; one partial run cannot establish power level. | None; next experiment: compare positive-Block, zero-Block, and Artifact targets while recording all trigger outputs. | Requiring positive Block would sharply weaken ordinary-encounter consistency. | low for balance; high for observed interaction |
| Setup burden | Potential survivability weakness | E11, E14, E17 | Field Commander, Countermeasures, and Break Their Guard require separate Power plays; the engine became strong, but the run repeatedly lost HP before or during setup. | E11 was a scaling elite, E14 began before resume, and floor 11 started at only 11 HP. | None; next experiment: compare first-two-turn HP loss with one versus multiple setup Powers across fresh runs. | Cheaper setup could make the high Breach ceiling too automatic. | low |
| Plan 2 | Useful flexibility with low absolute output | E11, E17 | Three Shield 5 conversions were always playable and reduced damage, but each required 1 energy plus a hand card and could not cover burst alone. | Only defensive mode was tested; upgrade and offensive/Train modes remain unobserved. | None; next experiment: test all three modes and compare Plan 2+card against a direct 1-energy card. | Increasing token values could make flexible conversion dominate specialized cards. | low |
| Evasive Maneuvers | Efficient floor, Orichalcum tension | E15, E17 | Four free Block enabled a 9-Block one-energy line, but a lone play would prevent Orichalcum's larger 6-Block trigger. | One draw and no lone-card turn were observed. | None; next experiment: measure useful versus awkward draws with and without Orichalcum. | Raising Block improves zero-cost defense and may remove the relic sequencing tradeoff. | low |

### Confounders

- Agent misplays: none identified in the resumed floor-9 or fully observed floor-11 segments. Floor-11 round 1 prioritized two setup Powers over 10 immediate damage; this was a strategic tradeoff, not a proven error, because Break Their Guard later produced the only defensive draw on the lethal turn.
- Game variance: the floor-11 Nibbits alternated buffs into 14 and 22 incoming damage. The lethal reshuffle drew only Defend+; the 37-damage attack line missed killing the 42-HP attacker by 5. The run entered floor 11 at 11 HP after losing 50 HP to the prior elite.
- Relic or encounter dependence: Orichalcum improved empty-Block turns but conflicts with small Block plays. Pantograph was acquired but never activated because the run did not reach the boss. Phoenix Force Visor defined the observed offensive engine.
- Tooling limitations: the session began after the first combat and resumed floors 6, 8, and 9 mid-combat, so startup choices, several early rounds, exact draw counts, and some card actions are unknown. Earlier reward endpoints hid the inherited Field Training and Call Wolverine. Game and Cyclops-mod versions were not exposed.
- Suspected bugs: zero-Block targets triggering effects described as breaking Block is surprising and repeatedly reproduced, but may be intended Breach semantics; no definitive bug is claimed.

### Next Experiments

1. Compare Breach and Strike triggers against positive Block, zero Block, and Artifact to establish intended Phoenix Force Visor and Break Their Guard semantics.
2. Test Plan 2's Shield, Train, and Breach modes in one run and compare each conversion against direct 1-energy alternatives.
3. Draft Evasive Maneuvers with and without Orichalcum, recording lone-card awkward draws and prevented damage.
4. Limit early setup to one Power in a fresh run and compare first-two-turn HP loss, combat length, and engine payoff against this run's multi-Power openings.
5. Re-test Optic Breach's upgrade in matched Vulnerable and Slow states to isolate the practical 7-to-10 base-damage increase.

## Guide Promotions

None. All findings remain exploratory from one partial run.