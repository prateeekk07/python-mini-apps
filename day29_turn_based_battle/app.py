print("💰 EMI Calculator - Day 28\n")

# Input
principal = float(input("Enter Loan Amount: ₹"))
annual_rate = float(input("Enter Annual Interest Rate (%): "))
years = int(input("Enter Loan Duration (in years): "))

# Convert values
monthly_rate = annual_rate / 12 / 100
months = years * 12

# EMI Calculation
emi = (principal * monthly_rate * (1 + monthly_rate) ** months) / \
      ((1 + monthly_rate) ** months - 1)

total_payment = emi * months
total_interest = total_payment - principal

# Output
print("\n📊 Loan Summary")
print(f"Monthly EMI       : ₹{emi:.2f}")
print(f"Total Payment     : ₹{total_payment:.2f}")
print(f"Total Interest    : ₹{total_interest:.2f}")