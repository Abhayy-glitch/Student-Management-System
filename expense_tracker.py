expenses = []

while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        item = input("Enter Expense Name: ")
        amount = float(input("Enter Amount: "))
        expenses.append((item, amount))
        print("Expense Added!")

    elif choice == "2":
        if len(expenses) == 0:
            print("No Expenses Found")
        else:
            print("\nExpenses:")
            for item, amount in expenses:
                print(item, "-", amount)

    elif choice == "3":
        total = sum(amount for item, amount in expenses)
        print("Total Expense =", total)

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice")