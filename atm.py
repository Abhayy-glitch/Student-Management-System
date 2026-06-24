balance = 1000

while True:
    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        print("Current Balance =", balance)

    elif choice == "2":
        amount = float(input("Enter Amount to Deposit: "))
        balance += amount
        print("Deposit Successful!")
        print("New Balance =", balance)

    elif choice == "3":
        amount = float(input("Enter Amount to Withdraw: "))

        if amount <= balance:
            balance -= amount
            print("Withdrawal Successful!")
            print("Remaining Balance =", balance)
        else:
            print("Insufficient Balance!")

    elif choice == "4":
        print("Thank You For Using ATM")
        break

    else:
        print("Invalid Choice")