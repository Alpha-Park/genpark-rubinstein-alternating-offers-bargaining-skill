# GenPark Rubinstein Alternating-Offers Bargaining Skill

Infinite-horizon Rubinstein alternating-offers bargaining protocol determining Subgame Perfect Equilibrium payoff splits.

Discover more at [GenPark](https://genpark.ai) and the [GenPark MCP Catalog](https://genpark.ai/mcp).

```mermaid
graph TD
    Round0[Round 0: P1 Proposes x1* to P2] --> Decision{P2 Accepts Immediately?}
    Decision -->|Yes: In SPE Equilibrium| Split[Immediate Division: P1 gets x1*, P2 gets x2*]
    Decision -->|No: Off-Equilibrium Delay| Delay[Surplus discounted by delta1 and delta2]
    style Round0 fill:#e1f5fe
    style Decision fill:#fff9c4
    style Split fill:#c8e6c9
    style Delay fill:#ffcdd2
```

## Features
- Closed-form Subgame Perfect Equilibrium (SPE) calculation.
- First-mover advantage and asymmetric patience (discount factor) modeling.
- Zero external dependencies.
