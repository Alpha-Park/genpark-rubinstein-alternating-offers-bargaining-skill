"""
Rubinstein Alternating-Offers Bargaining Skill Client
Pure Python Standard Library implementation of Rubinstein's infinite-horizon bargaining protocol.
Computes the unique Subgame Perfect Equilibrium (SPE) payoff partition between two negotiating agents
given their respective time discount factors delta1, delta2 in (0, 1).
"""

from typing import Dict, Any


class RubinsteinBargaining:
    def __init__(self, delta1: float = 0.9, delta2: float = 0.8, surplus: float = 100.0):
        if not (0.0 < delta1 < 1.0 and 0.0 < delta2 < 1.0):
            raise ValueError("Discount factors delta1 and delta2 must be strictly between 0 and 1.")
        self.d1 = delta1
        self.d2 = delta2
        self.surplus = surplus

    def compute_equilibrium_split(self) -> Dict[str, Any]:
        """Compute the unique Subgame Perfect Equilibrium (SPE) payoff split."""
        # Rubinstein theorem: Player 1 (first mover) gets x1* = (1 - delta2) / (1 - delta1 * delta2)
        share1 = (1.0 - self.d2) / (1.0 - self.d1 * self.d2)
        share2 = 1.0 - share1

        payoff1 = share1 * self.surplus
        payoff2 = share2 * self.surplus

        return {
            "player1_share": share1,
            "player2_share": share2,
            "player1_payoff": payoff1,
            "player2_payoff": payoff2,
            "immediate_agreement": True,
            "subgame_perfect": True,
            "patience_advantage": "Player 1" if self.d1 > self.d2 else ("Player 2" if self.d2 > self.d1 else "Equal")
        }
