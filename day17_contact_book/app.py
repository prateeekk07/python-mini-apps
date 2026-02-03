def add_contact(name, phone):
    with open("contacts.txt", "a") as file:
        file.write(f"{name},{phone}\n")
    print("✅ Contact added successfully!")

def view_contacts():
    try:
        with open("contacts.txt", "r") as file:
            contacts = file.readlines()

        if not contacts:
            print("📭 No contacts found.")
            return

        print("\n📒 Contact List:")
        for i, contact in enumerate(contacts, start=1):
            name, phone = contact.strip().split(",")
            print(f"{i}. {name} - {phone}")

    except FileNotFoundError:
        print("📭 No contacts found.")

print("📒 Contact Book App")
print("1. Add Contact")
print("2. View Contacts")
print("3. Exit")

while True:
    choice = input("\nChoose an option (1/2/3): ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        add_contact(name, phone)

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        print("👋 Exiting Contact Book. Bye!")
        break

    else:
        print("❌ Invalid choice. Try again.")