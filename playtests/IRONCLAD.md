# Ironclad Playbook

This playbook targets Slay the Spire 2 `v0.107.1` and Ascension 3. Exact card and relic text below was verified against the active profile's local `/api/v1/wiki` registry on 2026-09-29. Re-verify after a game update.

The full cited research is in `research/2026-09-29-sts2-ironclad-a3-strategy.md`.

## Run Plan

### Before the First Elite

The starter deck's open need is damage. Five Strikes, four Defends, and Bash do not justify an elite path by HP alone.

1. Take one independently efficient front-loaded or area-damage card before the first elite.
2. Reassess after every fight. A normal fight lasting eight turns is a damage alarm even when Burning Blood restores the lost HP.
3. Enter an elite only with a credible damage clock plus one of:
   - a relevant combat potion with a declared trigger;
   - a high-impact relic or card purchase;
   - opening draw or energy strong enough to execute the plan consistently.
4. Prefer a path with a rest or shop after a costly elite.
5. Do not preserve gold while a purchase solves the next forced fight.

Adequate early damage is not the same as a perfect long-term card. Twin Strike, Pommel Strike, Headbutt, Rampage, Thunderclap, Perfected Strike, or Fiend Fire can satisfy different versions of the immediate need.

### After Damage Is Adequate

Add efficient mitigation, consistency, and one coherent scaling package. A synergy pick needs at least two existing enablers or payoffs unless its standalone output already solves a current need.

Do not seed Rupture, Body Slam, and Feel No Pain packages in parallel. One speculative seed is the maximum; the next package card must be independently useful or complete real support.

## Verified Card Roles

| Card             | `v0.107.1` base text                                           | Operational rule                                                                                                                                                                                                               |
| ---------------- | -------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Twin Strike      | 1 energy: deal 5 twice                                         | Reliable early 10 damage. Take when first-elite damage is open. Multi-hit benefits twice from Strength.                                                                                                                        |
| Pommel Strike    | 1 energy: deal 9, draw 1                                       | Strong early damage plus consistency. Re-read state after it draws.                                                                                                                                                            |
| Headbutt         | 1 energy: deal 9, put a discard card on top of draw pile       | Good standalone damage with deterministic next-turn setup. Name the retrieval target before playing it.                                                                                                                        |
| Rampage          | 1 energy: deal 9; gain 5 damage this combat                    | Scaling attack for fights long enough to redraw it. Headbutt improves it. Do not value future redraws in a fight likely to end first.                                                                                          |
| Thunderclap      | 1 energy: deal 4 and apply 1 Vulnerable to all                 | Area setup, not premium single-target damage. Play before attacks that exploit Vulnerable.                                                                                                                                     |
| Perfected Strike | 2 energy: deal 6 plus 2 for every card containing "Strike"     | The untouched starter deck makes this at least 16 damage. Recount Strike-tag cards after every addition or removal; do not use a fixed score.                                                                                  |
| Fiend Fire       | 2 energy: exhaust hand; deal 7 per exhausted card              | Compute exact hand count. Four exhausted cards deal 28. It provides front-loaded damage and exhaust support, but can consume future resources. Play setup/draw first only when the resulting hand and energy improve the line. |
| Iron Wave        | 1 energy: gain 5 Block and deal 5                              | Flexible but low output. Useful when both halves matter; not a substitute for a damage solution by itself.                                                                                                                     |
| Taunt            | 1 energy: gain 7 Block and apply 1 Vulnerable                  | Efficient mitigation plus setup. Target the enemy that subsequent attacks will hit.                                                                                                                                            |
| Shrug It Off     | 1 energy: gain 8 Block, draw 1                                 | Efficient mitigation and consistency. Re-read after the draw.                                                                                                                                                                  |
| True Grit        | 1 energy: gain 7 Block, exhaust a random card                  | Standalone Block with risky base exhaust. Do not call it controlled exhaust until upgraded.                                                                                                                                    |
| Armaments        | 1 energy: gain 5 Block, upgrade a hand card                    | Low immediate Block. Take when temporary upgrades materially improve repeated cards, not as generic defense.                                                                                                                   |
| Shockwave        | 2 energy: apply 3 Weak and Vulnerable to all, exhaust          | High-value mitigation and damage amplification in fights long enough to exploit the debuffs.                                                                                                                                   |
| Offering         | 0 energy: lose 6 HP, gain 2 energy, draw 3, exhaust            | Recalculate after use. Spend HP only when the new energy/cards produce lethal, prevent more than 6 damage, or establish decisive scaling.                                                                                      |
| Bloodletting     | 0 energy: lose 3 HP, gain 2 energy                             | A real Rupture enabler, but the play still needs to gain more than the 3 HP cost. Recalculate lethal and mitigation after use.                                                                                                 |
| Setup Strike     | 1 energy: deal 7, gain 2 Strength this turn                    | Sequence before multi-hit attacks. Its Strength expires, so count only attacks playable this turn.                                                                                                                             |
| Crimson Mantle   | 1 energy Power: each turn lose 1 HP and gain 8 Block           | Repeatable self-damage plus mitigation. Supports Rupture, but increases urgency and must not be played when the fight will end before recouping its cost.                                                                      |
| Rupture          | 1 energy Power: when HP is lost on your turn, gain 1 Strength  | Skip without repeatable self-damage that the deck already wants to play.                                                                                                                                                       |
| Body Slam        | 1 energy: damage equal to current Block                        | Skip unless ordinary turns create substantial Block before the attack is played. It is a payoff, not a Block engine.                                                                                                           |
| Feel No Pain     | 1 energy Power: gain 3 Block whenever a card exhausts          | Skip without meaningful repeatable exhaust. One True Grit is not an engine.                                                                                                                                                    |
| Drum of Battle   | 1 energy: draw 2; when exhausted, gain 2 energy                | Draw support with an exhaust payoff. Re-read after drawing; do not assume the energy occurs when played.                                                                                                                       |
| Hellraiser       | 2 energy Power: drawn Strike cards play against a random enemy | Strong Strike package enabler. Random targeting is risky in multi-enemy fights. Auto-played Strikes reduce hand size, which can reduce a later Fiend Fire.                                                                     |

### Strike Package

Hellraiser, Perfected Strike, and Nutritious Soup require explicit Strike accounting.

- Hellraiser converts future Strike draws into free random-target attacks.
- Perfected Strike counts every card containing "Strike", not only basic Strikes.
- Nutritious Soup enchants all Strikes with Tezcatara's Ember; official patch notes describe the result as 0-cost, Eternal, and +3 damage.
- Reconsider Strike removal after acquiring any of these. Never apply a fixed "remove Strike first" rule.
- In multi-enemy fights, Hellraiser's random targeting can waste damage or break target priority. Inspect remaining enemy HP before relying on it.

## Turn Policy

Use this loop every player turn:

1. **Observe:** read HP, Block, Energy, every hand card, piles, enemy HP/Block/powers/intents, potions, and deterministic relic effects.
2. **Calculate lethal:** enumerate legal current-turn sequences. Include Vulnerable, Strength, multi-hit scaling, Fiend Fire hand count, and deterministic auto-plays.
3. **Check reactive triggers:** identify powers that change after an unblocked hit, damage, card type, or turn boundary. Stop generic automation when unfamiliar.
4. **Compare two turns:** compare maximum-Block play with a faster kill line. Minimize expected total HP loss, not current-turn loss.
5. **Reserve minimum mitigation:** block enough to survive and preserve the best next-turn line. Spend remaining resources on damage or decisive setup.
6. **Use potions:** spend one when it enables lethal, prevents meaningful damage, stops scaling, or bridges to a dangerous next turn.
7. **Sequence:** zero-cost setup, debuffs, scaling, then attacks that exploit them. Exceptions require an explicit reason.
8. **Re-read:** poll after every draw, exhaust, energy, Strength, cost, generation, auto-play, or hand-index change.
9. **Audit before end turn:** record incoming, expected loss, lethal/near-lethal, next-turn plan, and potion decision.

Duplicated cards and multi-card exhaust effects can resolve in stages. Throwing Axe plus Offering showed both HP losses before the second energy-and-draw payload appeared; Second Wind status exhausts also completed across multiple polls. Do not act on an intermediate hand or energy value. Poll until the relevant hand, energy, HP, Block, and power changes are all stable.

### Race Versus Block

Race when the enemy's repeated damage or scaling exceeds sustainable mitigation. If maximum Block still leaves substantial loss and creates another identical enemy turn, spending all energy on Block is usually losing play.

Block when it prevents lethal, preserves a concrete next-turn lethal line, or prevents a reactive trigger such as Fossil Stalker's Strength gain. Do not call current-turn damage prevention successful if it increases two-turn damage.

## Potions

- **Flex Potion:** use before multiple attacks or exact lethal; multi-hit cards gain the Strength bonus per hit.
- **Liquid Bronze:** use early against multi-hit enemies or fights expected to last several attacking rounds.
- **Swift Potion:** use when the hand cannot cover a dangerous attack, when three draws can expose lethal, or before accepting double-digit avoidable damage.
- **Stable Serum:** use when retaining offense or mitigation creates the required next-turn hand. Do not carry it through repeated unsustainable attacks.
- **Energy Potion:** spend it when 2 energy completes a decisive multi-card turn, not merely to empty the slot. In run `modded:profile1:1790735201`, it funded Inferno+, Crimson Mantle+, and Blood Wall together, preventing boss damage while completing the scaling engine.
- At or below 50% HP, use a relevant potion before accepting 10 or more avoidable damage.

## Known Act 1 Threats

### Fossil Stalker

Unblocked hits trigger Strength scaling in observed play. Prevent the first trigger when feasible, use Liquid Bronze early, and re-read Strength plus intent after every connecting attack. Once its damage exceeds sustainable mitigation, calculate the shortest safe race rather than blindly continuing to Block.

### Bygone Effigy

Observed attacking for 23 repeatedly in run `modded:profile1:1790731181`. The starter-heavy deck could not sustain that Block requirement and died after eight turns. Enter only with a credible damage clock. If blocking this turn merely schedules another 23-damage turn, preserve only enough HP for the fastest kill line and attack.

### Long Normal Fights

Living Fog, Gremlin Merc, and Fuzzy Wurm Crawler exposed weak damage clocks in prior runs. Treat any normal fight lasting eight or more turns as a mandatory deck-output warning before the next reward or elite path.

### Multi-Enemy Fights

Slimes and Phantasmal Gardeners reward area damage and target discipline. Kill an attacker when that prevents more damage than spreading attacks. Against Minions, kill the leader when leader death removes them.

## Known Act 3 Threats

### Mecha Knight

Observed alternating among a heavy attack, a status turn that adds four Burns, and a Block-plus-Buff turn. Use the non-attacking turns for scaling and offense. Burns deal end-turn damage but can be absorbed by Block. A supported Crimson Mantle/Rupture/Inferno engine cleared it in four turns; generic blocking without a damage clock would have allowed its later 40-damage attack.

### Globe Head

Galvanic caused 6 damage whenever a Power was played in run `modded:profile1:1790735201`. Reprice every Power as HP loss and prefer immediate burst when lethal is available. Attack Potion into Bludgeon plus an Offering-enabled hand produced a turn-one kill without playing a Power.

### Aeonglass

Withering Presence counts down as cards are played and adds a Wither at zero. Base Wither dealt 3 blockable end-turn damage; after Aeonglass buffed, Wither+1 dealt 6. Treat status damage plus the displayed attack as total incoming damage. Fiend Fire can convert Withers into damage, and Second Wind can exhaust them, but wait for the multi-exhaust animation to settle before trusting the hand or Block total.

Aeonglass alternated attack/defense turns with status/buff turns in the observed seven-turn win. Use status/buff turns to establish Powers or strip Artifact. Its three Artifact charges made early Tremble/Bash setup inefficient until the fight's engine was already stable.

## Build-Bound Relics

| Relic          | Verified effect                                                                                                                                                          |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Burning Blood  | Heal 6 HP after combat. Never include this future healing in current lethal margin.                                                                                      |
| Booming Conch  | At elite combat start, draw 2 additional cards and gain 1 energy. Convert the opening burst into damage or setup.                                                        |
| Orichalcum     | End a turn with no Block to gain 6 Block. Compare this with playing a low-value Defend.                                                                                  |
| Ornamental Fan | Every third Attack in one turn grants 4 Block. Count attacks before reserving separate Block energy.                                                                     |
| Arcane Scroll  | Adds a random Rare card on pickup. Rebuild the deck plan around the actual card, not its rarity.                                                                         |
| Throwing Axe   | The first card each combat is played an extra time. Duplicated effects may settle asynchronously; wait for both copies before calculating the turn.                      |
| Razor Tooth    | Played Attacks and Skills upgrade for later uses that combat. The current play can still use the pre-upgrade value even when the post-play state displays upgraded text. |
| Sturdy Clamp   | Retains up to 10 Block. Combine retained Block with recurring sources before deciding how much new Block the turn requires.                                              |
| Ruined Helmet  | Doubles the first Strength gain each combat. Sequence the largest reliable permanent Strength gain first; Fight Me!+ gained 8 instead of 4 in the winning run.           |

## Evidence Limits

The local wiki covers discovered cards and relics, not complete enemy move tables or potion text. The compendium confirms encounter histories and potion discovery but not mechanics. For unfamiliar enemies, inspect live powers and intents; do not import Slay the Spire 1 behavior or later beta values.
