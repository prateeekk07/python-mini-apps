print("🔐 PIN Setup & Login System - Day 24\n")

# -------- PIN SETUP --------
while True:
    new_pin = input("Set your 4-digit PIN: ")

    if new_pin.isdigit() and len(new_pin) == 4:
        print("✅ PIN set successfully!\n")
        break
    else:
        print("❌ Invalid PIN. Please enter exactly 4 digits.\n")

# -------- LOGIN SYSTEM --------
attempts = 3

while attempts > 0:
    user_pin = input("Enter your PIN to login: ")

    if user_pin == new_pin:
        print("✅ Access Granted! Welcome.")
        break
    else:
        attempts -= 1
        print(f"❌ Incorrect PIN. Attempts left: {attempts}")

if attempts == 0:
    print("🚫 Account Locked. Too many failed attempts.")