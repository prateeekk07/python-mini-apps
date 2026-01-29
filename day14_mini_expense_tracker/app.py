def add_expense(amount, note):
    with open("expenses.txt", "a") as file:
        file.write(f"{amount},{note}\n")
    print("✅ Expense added successfully!")

def view_expenses():
    try:
        with open("expenses.txt", "r") as file:
            expenses = file.readlines()

        if not expenses:
            print("📭 No expenses found.")
            return

        total = 0
        print("\n💰 Expense List:")
        for i, expense in enumerate(expenses, start=1):
            amount, note = expense.strip().split(",", 1)
            total += float(amount)
            print(f"{i}. ₹{amount} - {note}")

        print(f"\n🧾 Total Expense: ₹{total}")

    except FileNotFoundError:
        print("📭 No expenses found.")

print("💰 Mini Expense Tracker")
print("1. Add Expense")
print("2. View Expenses")
print("3. Exit")

while True:
    choice = input("\nChoose an option (1/2/3): ")

    if choice == "1":
        amount = float(input("Enter amount: ₹"))
        note = input("Enter expense note: ")
        add_expense(amount, note)

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        print("👋 Exiting Expense Tracker. Bye!")
        break

    else:
        print("❌ Invalid choice. Try again.")