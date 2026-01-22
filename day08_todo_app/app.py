def add_task(task):
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")
    print("✅ Task added successfully!")

def view_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()

        if not tasks:
            print("📭 No tasks found.")
        else:
            print("\n📋 Your Tasks:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task.strip()}")
    except FileNotFoundError:
        print("📭 No tasks found.")


print("📝 To-Do App")
print("1. Add Task")
print("2. View Tasks")
print("3. Exit")

while True:
    choice = input("\nChoose an option (1/2/3): ")

    if choice == "1":
        task = input("Enter a task: ")
        add_task(task)

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        print("👋 Exiting To-Do App. Bye!")
        break

    else:
        print("❌ Invalid choice. Try again.")