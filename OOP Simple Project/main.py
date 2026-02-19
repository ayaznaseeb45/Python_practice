class BankAccount:
    def __init__(self, balance=0):
        self.__account_holder = ''
        self.__balance = balance
        self.menu()

    def menu(self):
        print("""
=== Choose an option ===
1. Deposit
2. Withdraw
3. Check Balance
4. Get Account Holder Name
5. Exit
        """)

        name = input("Enter your name: ")
        self.__account_holder = name
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            # Deposit function
            self.deposit()

        elif choice == "2":
            # Withdraw function
            self.withdraw()

        elif choice == "3":
            # Check Balance
            self.check_balance()

        elif choice == "4":
            # Get Account Holder Name
            self.get_holder()
        
        elif choice == "5":
            print("Thank you for using the Bank System. Goodbye!")
        else:
            print("Invalid choice! Please enter 1-5.")
            self.menu()

    def get_holder(self):
        print(f"Holder name is {self.__account_holder}")
    
    def check_balance(self):
        print(f"Your balance is {self.__balance}")

    def deposit(self):
        
        amount = int(input("Enter the amount you want to deposit: "))
        if amount > 0:
            self.__balance += amount
            print(f"Deposit {amount} successful! New balance: {self.__balance}")
            self.menu()
        else:
            print("Error: Deposit amount must be positive!")
            self.menu()

    def withdraw(self):
        amount = int(input("Enter the amount you want to withdraw: "))

        if amount <= 0:
            print("Invalid amount! Must be positive.")
        elif amount > self.__balance:
            print("Insufficient Balance!")
        else:
            self.__balance -= amount
            print(f"You have withdrawn {amount}. Remaining balance is {self.__balance}")





obj = BankAccount()
