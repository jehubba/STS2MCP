# STS2 Multiplayer Playtest: Cyclops + Cyclops (Run 2)

## Run Context

| Field           | Value                                                               |
| --------------- | ------------------------------------------------------------------- |
| Characters      | Cyclops (host) + Cyclops (client)                                   |
| Game mode       | Two-player FastMP                                                   |
| Ascension       | 0                                                                   |
| Host            | Steam launch, MCP port 15526, player slot 0                         |
| Client          | Steam-disabled direct launch, MCP port 15527, player slot 1         |
| Outcome         | **ACT 1 CLEARED**; stopped at the Act 2 map                         |
| Final party HP  | Host 1/70; client 15/70                                             |
| Leadership rule | Take Leadership whenever offered unless that player already owns it |

## Test Questions

1. Can two independently controlled Cyclops players complete an extended multiplayer act through the real Steam-host/FastMP-client path?
2. Do synchronized combat actions, end-turn votes, map votes, per-player rewards, shops, relics, and rest choices remain operational for a full act?
3. Can play continue when one player is reduced to zero HP during the boss and then transition both players to rewards and the next act?
4. Does the agent consistently inspect every card reward for Leadership before choosing or skipping?

## Act 1 Summary

- Both endpoints remained independently controllable throughout the act.
- Map votes and both-player end-turn votes synchronized successfully.
- Rewards, shops, relics, decks, gold, potions, and rest choices remained player-specific.
- `Huddle Up+` successfully produced its cross-player card-draw effect.
- The party reached Soul Fysh at floor 16 after clearing the selected normal and Elite encounters and using the final rest site.
- No Leadership card was offered to either player during the run. Neither player owned Leadership, so the mandatory-pick exception never applied.

## Boss Evidence: Soul Fysh

| Field            | Observation                                                                                                                     |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| Starting HP      | 464                                                                                                                             |
| Combat length    | 13 rounds                                                                                                                       |
| Status pressure  | Repeated Beckon cards clogged both decks and dealt end-of-turn HP loss when retained                                            |
| Late-fight state | Soul Fysh at 57 HP; host 17 HP, client 25 HP                                                                                    |
| Round 12 line    | Host used Weak Potion, then played Strike+, Concussive Beam, and Defend; client cleared one Beckon, played Defend, and attacked |
| Round 12 result  | Soul Fysh fell to 22 HP; host fell to 0 HP during enemy/end-of-turn resolution; client survived at 15 HP                        |
| Lethal           | Client played Rapid Fire, reducing Soul Fysh from 22 to 6 HP, then Optic Breach for the kill                                    |
| Transition       | Both endpoints reached rewards; host was restored to 1 HP and both advanced to the Act 2 map                                    |

The host's apparent death did not deadlock voting or prevent the surviving client from acting. Boss defeat and reward progression propagated to both game processes.

## Boss Reward Decisions

| Player | Offered                                                   | Chosen                     | Leadership Check       |
| ------ | --------------------------------------------------------- | -------------------------- | ---------------------- |
| Host   | To Me, My X-Men; What People See; Doing Whatever It Takes | To Me, My X-Men            | Leadership not offered |
| Client | You Know What Must Be Done; Ruby Rage; Optic Dodge        | You Know What Must Be Done | Leadership not offered |

Each player then claimed 100 gold. Final gold at the Act 2 map was 155 for the host and 181 for the client.

## Operational Findings

### Confirmed

- Steam-host plus Steam-disabled FastMP client supports a complete two-player Act 1 run.
- Separate MCP ports prevent cross-control and expose the correct local-player perspective.
- A surviving player can finish combat after the other player reaches zero HP.
- The defeated player is restored to 1 HP for post-boss rewards and Act 2 progression.
- Card rewards can be inspected and resolved independently while enforcing the Leadership rule.

### Tooling and Coordination Notes

- Host and client can briefly report different transition phases. Poll each endpoint independently until its state settles before acting.
- Card indices shift after every play. Re-read state or play from higher indices to lower indices.
- Reward indices shift after claims. Claim from right to left and re-read before the next claim.
- During the boss transition, the named MCP tool surface temporarily disappeared from the controlling session. Direct requests to `/api/v1/multiplayer` restored read/action access without restarting either game.
- Two direct lethal-card POST requests did not return before the command wrapper was interrupted, although both actions resolved in game. A subsequent state read was required to verify each action.

## Assessment

The second two-Cyclops run validates the multiplayer workflow beyond a short smoke test. It exercised a complete Act 1 path, prolonged boss combat, synchronized voting, cross-player card effects, independent progression choices, a player defeat, survivor-only lethal, and synchronized transition into Act 2.

The workflow is operational for two-agent play, with two remaining orchestration risks: transient endpoint phase divergence and the lack of timeout/recovery when an agent stops before submitting its turn vote. Neither blocked this run.

## Guide Promotions

- Leadership remains mandatory when offered unless that player already owns it.
- Poll multiplayer endpoints independently during transitions.
- Re-read state after interrupted or timed-out action calls before retrying; the action may already have resolved.
