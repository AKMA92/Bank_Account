from SavingAccount import SavingsAccount
from YouthAccount import YouthAccount
from TaxReport import TaxReport

class BankApplication:

    def __init__(self):
        self.accounts_list = []
        self.current_account = None

    def create_account(self):
        iban = input("Enter IBAN: ")

        currency = input("Enter Currency (CHF, EUR, USD): ").upper().strip()
        if currency not in ["CHF", "EUR", "USD"]:
            print("Invalid currency")
            return

        account_type = input("Choose account type (1 = Savings, 2 = Youth): ")

        if account_type == "1":
            account_object = SavingsAccount(iban, currency)
            self.current_account = account_object

        elif account_type == "2":
            age = int(input("Enter age: "))
            account_object = YouthAccount(iban, age, currency)
            self.current_account = account_object
            self.current_account = account_object

        else:
            print("Invalid account type")
            return

        self.accounts_list.append(account_object)
        print("Account created successfully")


    def select_account(self):
        iban = input("Enter IBAN of account to select: ")

        for account_object in self.accounts_list:
            if account_object.iban == iban:
                self.current_account = account_object
                print("Account selected successfully")
                return

        print("Account not found")



if __name__ == "__main__":
    app = BankApplication()

    while True:
        print()
        print("==== E-BANKING | HOME ====")
        print("1. Create Account     ")
        print("2. Select Account     ")
        print("3. Deposit        ")
        print("4. Withdraw        ")
        print("5. Show Balance      ")
        print("6. Generate Tax Report  ")
        print("0. Exit          ")
        print()

        print("All accounts:")
        for account_object in app.accounts_list:
            print(account_object.iban)

        if len(app.accounts_list) > 0:
            print()
            print("Current selected account:" f"{app.current_account.iban}")

        print()
        choice = input("Choose an option: ")

        if choice == "1":
            app.create_account()

        elif choice == "2":
            app.select_account()

        elif choice == "3":
            if app.current_account:
                amount = float(input("Enter amount to deposit: "))
                print(app.current_account.deposit(amount))
            else:
                print("No account selected.")

        elif choice == "4":
            if app.current_account:
                amount = float(input("Enter amount to withdraw: "))
                print(app.current_account.withdraw(amount))
            else:
                print("No account selected.")

        elif choice == "5":
            if app.current_account:
                print(app.current_account.get_balance())
            else:
                print("No account selected.")

        elif choice == "6":
            report = TaxReport()
            report.generate(app)

        elif choice == "0":
            print("Exiting application...")
            break

        else:
            print("Invalid input. Please try again.")
