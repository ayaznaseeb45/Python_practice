expense_list = []

print("Welcome to Expense Tracker")

while True:
    print("\n==== Expense Menu ====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Expense")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    # Add Expense
    if choice == 1:
        date = input("Enter expense date: ")
        category = input("Expense category (food, travel, shopping, fun): ")
        description = input("Expense description: ")
        amount = float(input("Enter amount: "))

        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expense_list.append(expense)
        print("Expense added successfully!")

    # View All Expenses
    elif choice == 2:
        if len(expense_list) == 0:
            print("No expenses added yet")
        else:
            print("\nAll Expenses:")
            count = 1
            for expense in expense_list:
                print(f"\n {count}. {expense['date']} => {expense['category']} => {expense['description']} => {expense['amount']}")
                count += 1

    # View Total Expense
    elif choice == 3:
        total = 0
        for expense in expense_list:
            total = total + expense["amount"]
        print("Total Expense:", total)

    # Exit
    elif choice == 4:
        break

    else:
        print("Invalid choice")
