from SavingAccount import SavingsAccount
from YouthAccount import YouthAccount
from TaxReport import TaxReport

class BankApplication:

    def __init__(self):
        self.accounts_list = []
        self.current_account = None

    def create_account(self):
        iban = input("Enter IBAN: ")
        account_type = input("Choose account type (1 = Savings, 2 = Youth): ")

        if account_type == "1":
            account_object = SavingsAccount(iban)

        elif account_type == "2":
            age = int(input("Enter age: "))
            account_object = YouthAccount(iban, age)

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

    # Zwei Accounts über die App erstellen
    print("Create first account:")
    app.create_account()

    print("\nCreate second account:")
    app.create_account()

    # Konto auswählen
    app.select_account()

    # Aktionen ausführen
    print(app.current_account.deposit(1000))
    print(app.current_account.get_balance())

    print(app.current_account.withdraw(200))
    print(app.current_account.get_balance())

    report = TaxReport()
    report.generate(app)