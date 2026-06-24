tasks = []

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        task = input("Enter Task: ")
        tasks.append(task)
        print("Task Added!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No Tasks Available")
        else:
            print("\nTasks:")
            for i, task in enumerate(tasks, start=1):
                print(i, ".", task)

    elif choice == "3":
        if len(tasks) == 0:
            print("No Tasks to Delete")
        else:
            for i, task in enumerate(tasks, start=1):
                print(i, ".", task)

            num = int(input("Enter Task Number to Delete: "))
            if 1 <= num <= len(tasks):
                tasks.pop(num - 1)
                print("Task Deleted!")
            else:
                print("Invalid Number")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice")