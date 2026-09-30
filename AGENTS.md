# STS2 MCP — AI Gameplay Guide

## MCP Tool Calling Tips

### State Polling

- After `combat_end_turn`, the state may show `is_play_phase: false` or `turn: enemy`. Call `get_game_state` again to advance to the next player turn.
- Sometimes you need to call `get_game_state` twice — once to see enemy turn results, once to see your new hand.
- Use `format: "json"` during combat for structured data; `format: "markdown"` for map/event overview.

### Card Index Shifting

- **CRITICAL**: Playing a card removes it from hand and shifts all indices. Play cards from RIGHT to LEFT (highest index first) to keep lower indices stable, or re-check state between plays.
- When targeting, always provide `target` for single-target cards. Entity IDs are UPPER_SNAKE_CASE with a `_0` suffix (e.g. `KIN_PRIEST_0`).

### Event & Reward Flow

- Events: `event_choose_option`. After choosing, there's often a "Proceed" option at index 0.
- Rest sites: `rest_choose_option`, then `proceed_to_map`.
- Rewards: claim from right-to-left (highest index first) to avoid index shifting. Card rewards open a sub-screen; use `rewards_pick_card` or `rewards_skip_card`.

### Potions

- `use_potion(slot=N)` — slot is the potion slot index, not a card index.
- `discard_potion(slot=N)` — discard a potion to free up the slot when full.
- Potions don't cost energy or count as card plays. Use buff potions BEFORE playing cards.

---

## General Strategy

### Core Principles

1. **HP is a resource, not a score.** Take calculated damage to deal more. Don't waste energy on block when enemies aren't attacking.
2. **Deck quality > deck size.** Skip card rewards if nothing synergizes. A lean deck draws key cards more often.
3. **Front-load damage.** Killing enemies faster means less total damage taken.
4. **Read intents carefully.** Sleep/Buff = go all-out offense. Attack = balance block and damage. Debuff = usually no damage, offense turn.
5. **Leadership is mandatory for this playtest.** If a card reward offers Leadership, take it unless that player already owns a copy.

### Combat Sequencing (General)

1. Play 0-cost utility/setup cards first.
2. Play skills before attacks when possible — many mechanics reward this order (e.g. Slow debuff on enemies stacks per card played).
3. Play biggest attacks last to benefit from accumulated buffs/debuffs.
4. Check enemy HP — if you can kill this turn, skip blocking entirely.

### Autonomous Turn Quality Gate

Do not drive combat with a static per-card score. Before every player turn:

1. Sum all displayed incoming attack damage, including multi-hit counts, then subtract current Block.
2. Check exact or conservative lethal before spending energy on Block. If lethal is available, take it.
3. If lethal is not available, reserve enough playable Block or mitigation to keep expected HP loss within the encounter budget, then spend remaining energy on damage or scaling. Do not repeatedly maximize Block against an enemy whose next attacks exceed the deck's sustainable mitigation; shorten the fight instead. At or below 50% HP, treat avoidable HP loss as unacceptable unless offense is required to prevent greater expected damage over the next two turns.
4. Re-read state after every card that draws, generates, exhausts, changes energy, changes Strength/Dexterity, or shifts hand indices.
5. Use potions before ending a turn when they prevent meaningful damage, enable lethal, or improve a multi-attack turn. A full potion belt at death is an agent-policy failure.
6. Stop automation and inspect the full state when an enemy has an unfamiliar scaling/status power; do not continue applying generic scores.

For generated runners, log per turn: incoming damage, lethal available, chosen mitigation, expected HP loss, and potion decision. A runner that cannot compute these values is suitable only for state polling, not card play.

### Map Pathing

- **Elites** give relics — fight them when healthy (>70% HP).
- Do not enter an Elite based on HP alone. Require either a credible damage plan, a combat potion, or a high-impact card/relic purchase; otherwise choose a safer path.
- **Rest before Boss** — heal if below 80% HP. Boss fights are long and punishing.
- **Unknown nodes** are safer than Elites. Good at medium HP.
- **Shops** — visit with 100+ gold.
- **Deck quality matters more than quantity** — don't add cards just because they're offered.

### Card Reward Discipline

- Skipping is the default when a reward does not solve an immediate deck need or strengthen an engine already supported by at least two cards/relics.
- Before the first Elite, the starter deck has an immediate damage need. Take one efficient front-loaded or area-damage card rather than skipping every merely non-premium reward.
- Do not draft a speculative package one card at a time. Examples: Rupture without repeatable self-damage, Body Slam without reliable high Block, or Feel No Pain without meaningful exhaust density.
- After each pick, state the deck need and the cards/relics that support the choice. If that sentence is weak, skip.

### Boss Fights

- **Kill the leader, not the minions.** Enemies with "Minion" power flee when their leader dies.
- Use potions aggressively in boss fights — they don't carry between acts.
- Boss fights are wars of attrition. The longer they go, the more enemies scale with Strength buffs.

### Potion Usage

- Don't hoard potions. Dying with full potions is the worst outcome.
- Use permanent-value potions (Fruit Juice = +5 Max HP) early in any combat.
- Use buff potions (Flex Potion) on turns with multiple attacks.
- Use Liquid Bronze early against multi-hit enemies or fights expected to last at least three attacking rounds.
- Use Swift Potion when the current hand cannot meet a dangerous attack, when three draws could reveal lethal, or before accepting double-digit unblocked damage.
- At less than 50% HP, spend a relevant potion before accepting 10 or more expected damage.

### Common Mistakes

- Blocking when enemies are sleeping/buffing — waste of energy.
- Not checking card indices after playing — indices shift left.
- Taking too long to kill bosses — enemies scale every turn.
- Adding mediocre cards that dilute the deck before boss fights.
- Using a static card score that ignores incoming damage, enemy scaling, energy reservation, and potion value.
- Drafting every reward. In `modded:profile1:1790695747`, the agent took 7 cards from 7 rewards, assembled three unsupported mini-packages, and died on Act 1 floor 14 with all three potions unused.
- Skipping every reward and shop purchase. In `modded:profile1:1790731181`, the agent rejected all three normal card rewards and Fiend Fire at a shop, then spent eight turns overblocking against Bygone Effigy and died on Act 1 floor 8 with Stable Serum unused.

### Ironclad (base game)

- Before starting or resuming an Ironclad run, read `playtests/IRONCLAD.md`. Its card text and interactions are build-bound; re-verify local wiki facts after a game update.
- Burning Blood heals after combat, not during it. Do not spend future healing in advance by taking avoidable damage now.
- Prioritize one coherent early plan: efficient front-loaded damage plus enough Block, or a clearly supported exhaust/self-damage engine. Do not mix speculative Rupture, Body Slam, and Feel No Pain picks without their enablers.
- Before the first Elite, explicitly name the deck's damage card, opening plan, potion trigger, and projected race. If any is missing, choose a safer path or solve the gap at the next reward/shop.
- Treat an eight-turn normal fight as a mandatory damage-output warning. Reassess drafting, shopping, and Elite pathing even if Burning Blood restored most of the HP.
- At shops, compare purchases against the next forced threat. Retaining gold is not a plan when a card, relic, or potion materially changes projected survival.
- Recount Strike-tag cards after Perfected Strike, Hellraiser, Nutritious Soup, or any Strike removal; never apply a fixed Strike valuation or removal order.
- Against Fossil Stalker, unblocked hits trigger its Strength scaling. Prevent the first unblocked hit when possible, use Liquid Bronze early, and reassess its live Strength and next intent after every attack. Generic damage racing is unsafe once it starts scaling.
- Against Bygone Effigy or another enemy whose repeated attacks exceed sustainable Block, optimize total expected loss over two turns. Do not spend every turn maximizing Block if offense ends the fight sooner.
