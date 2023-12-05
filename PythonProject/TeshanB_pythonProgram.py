#def bank():
    # this program will do 3 things:
    #1. view balance
    #2. deposit money 
    #3. withdraw money
#    print('welcome to your virtual banker. How can I help you?')
#    selection =int(input('press 1 for view balance, 2 for deposit...'))

#    if(selection==1):
#        print('heres your balance')

#bank()
class BankAccount:
    def __init__(self, account_holder, balance=7112.77):
        self.account_holder = account_holder
        self.balance = balance
        self.statement = []

    def display_card(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: ${self.balance:.2f}")

    def display_statement(self):
        print("Transaction History:")
        for transaction in self.statement:
            print(transaction)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.statement.append(f"Deposit: +${amount:.2f}")
            print("Deposit successful.")
        else:
            print("Invalid amount for deposit.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.statement.append(f"Withdrawal: -${amount:.2f}")
            print("Withdrawal successful.")
        else:
            print("Invalid amount for withdrawal.")

# ________________________________________________________________________________________________________________ #

def main():
    user_name = input("Enter your name: ")
    account = BankAccount(user_name)

    while True:
        print("\n1. View Card\n2. View Statements\n3. Make a Deposit\n4. Make a Withdrawal\n5. Exit")
        choice = input("Welcome back. What will you like to do today? (1-5): ")

        if choice == "1":
            account.display_card()
        elif choice == "2":
            account.display_statement()
        elif choice == "3":
            amount = float(input("Great! How much will you like to deposit?: $"))
            account.deposit(amount)
        elif choice == "4":
            amount = float(input("Great! How much would you like to withdrawal?: $"))
            account.withdraw(amount)
        elif choice == "5":
            print("Exiting bank simulation. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()