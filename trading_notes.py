# Trading Notes - Anurag Dixit
# Author: Anurag Dixit

trading_principles = [
    "Discipline",
    "Patience",
    "Resilience",
    "Relentless adaptation",
    "Consistency"
]

def risk_reward_ratio(risk, reward):
    return reward / risk if risk > 0 else None

if __name__ == "__main__":
    print("Trading Principles:", trading_principles)
    print("Risk-Reward ratio (100 risk / 250 reward):", risk_reward_ratio(100, 250))
