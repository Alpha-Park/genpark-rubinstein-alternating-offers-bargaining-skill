"""
Demonstration of Rubinstein Alternating-Offers Bargaining Skill
"""

from client import RubinsteinBargaining

def main():
    print("=== Rubinstein Infinite-Horizon Alternating-Offers Bargaining ===")

    # Scenario 1: Equal patience (delta1 = delta2 = 0.9, Surplus = $100.0)
    rb_symmetric = RubinsteinBargaining(delta1=0.9, delta2=0.9, surplus=100.0)
    res_sym = rb_symmetric.compute_equilibrium_split()

    print("Scenario 1: Symmetric Patience (delta1 = delta2 = 0.9):")
    print(f"  Player 1 (First Mover) Share: {res_sym['player1_share']*100:.2f}% (${res_sym['player1_payoff']:.2f})")
    print(f"  Player 2 (Second Mover) Share: {res_sym['player2_share']*100:.2f}% (${res_sym['player2_payoff']:.2f})")

    # When delta1 = delta2 = 0.9: share1 = (1 - 0.9) / (1 - 0.81) = 0.1 / 0.19 = 52.63%
    assert abs(res_sym["player1_share"] - (1.0 / 1.9)) < 1e-5
    assert abs(res_sym["player1_payoff"] + res_sym["player2_payoff"] - 100.0) < 1e-6

    # Scenario 2: Asymmetric patience (Player 1 very patient delta1=0.95, Player 2 impatient delta2=0.5)
    rb_asym = RubinsteinBargaining(delta1=0.95, delta2=0.5, surplus=100.0)
    res_asym = rb_asym.compute_equilibrium_split()
    print("\nScenario 2: Asymmetric Patience (Patient P1=0.95, Impatient P2=0.50):")
    print(f"  Player 1 Share: {res_asym['player1_share']*100:.2f}% (${res_asym['player1_payoff']:.2f})")
    print(f"  Patience Advantage: {res_asym['patience_advantage']}")

    assert res_asym["player1_share"] > 0.90  # Patient player captures over 90% of surplus

    print("\nRubinstein Bargaining Verification PASS!")

if __name__ == "__main__":
    main()
