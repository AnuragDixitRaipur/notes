# Policy Calculator - Anurag Dixit
# Author: Anurag Dixit

def calculate_premium(amount, years):
    """Simple premium calculation with 5% yearly growth"""
    return amount * (1 + 0.05) ** years

def calculate_commission(premium, rate=0.15):
    """Commission on premium at given rate"""
    return premium * rate

if __name__ == "__main__":
    base_amount = 10000
    years = 3
    premium = calculate_premium(base_amount, years)
    commission = calculate_commission(premium)
    print(f"Premium after {years} years: ₹{premium:.2f}")
    print(f"Commission earned: ₹{commission:.2f}")
