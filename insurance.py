# Basic Insurance Advisor Script

def premium_advice(amount):
    commission = amount * 0.12
    return f"For a premium of ₹{amount}, expected commission is ₹{commission:.2f}"

if __name__ == "__main__":
    print("Insurance Advisor Tool 🛡️")
    premium = int(input("Enter premium amount: "))
    print(premium_advice(premium))
