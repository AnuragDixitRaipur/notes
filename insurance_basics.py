# Insurance Basics - Notes
# Author: Anurag Dixit

def insurance_types():
    return ["Life Insurance", "Health Insurance", "Motor Insurance", "Fire Insurance"]

def commission_example(premium):
    # Example: 15% commission
    return premium * 0.15

if __name__ == "__main__":
    print("Types of Insurance:", insurance_types())
    print("Commission on ₹10,000 premium:", commission_example(10000))
