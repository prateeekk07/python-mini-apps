print("🏦 ATM Machine Simulator - Day 30\n")

correct_pin = "1234"
balance = 10000
attempts = 3

# PIN Login
while attempts > 0:
    pin = input("Enter your 4-digit PIN: ")

    if pin == correct_pin:
        print("✅ Login Successful!\n")
        break
    else:
        attempts -= 1
        print(f"❌ Incorrect PIN. Attempts left: {attempts}")

if attempts == 0:
    print("🚫 Card Blocked.")
    exit()

# ATM Menu
while True:
    print("\nATM Menu:")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        print(f"💰 Your current balance: ₹{balance}")

    elif choice == "2":
        amount = float(input("Enter deposit amount: ₹"))
        if amount > 0:
            balance += amount
            print("✅ Deposit successful.")
        else:
            print("❌ Invalid amount.")

    elif choice == "3":
        amount = float(input("Enter withdrawal amount: ₹"))
        if amount > balance:
            print("❌ Insufficient balance.")
        elif amount <= 0:
            print("❌ Invalid amount.")
        else:
            balance -= amount
            print("✅ Withdrawal successful.")

    elif choice == "4":
        print("👋 Thank you for using the ATM.")
        break

    else:
        print("❌ Invalid option.")