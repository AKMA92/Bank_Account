class BankAccount:
    limit = 100000
    balance = 0.0
    active = True

    def __init__(self, iban: str, currency="CHF", withdraw_limit: float = 10000):
        self.iban = iban
        self.currency = currency
        self.withdraw_limit = withdraw_limit

    def open_account(self):
        self.active = True
        return "Account set to active"

    def deposit(self, amount: float):
        if not self.active:
            return "Account is inactive"
        if amount <= 0:
            return "Amount must be positive"
        if amount + self.balance > self.limit:
            return "Limit exceeded"
        self.balance += amount
        return f"Deposit {amount} {self.currency} succeeded"

    def withdraw(self, amount: float):
        if not self.active:
            return "Account is inactive"
        if amount <= 0:
            return "Amount must be positive"
        if amount > self.balance:
            return "Insufficient balance"
        self.balance -= amount
        return f"Withdraw {amount} {self.currency} succeeded"

    def get_balance(self):
        if not self.active:
            return "Access denied"
        return f"{self.balance} {self.currency}"

    def close_account(self):
        self.active = False
        return "Account set to inactive"


if __name__ == "__main__":

    # Objekt erstellen
    my_bankaccount = BankAccount("CH55555555555555555")

    # Methoden testen
    print(my_bankaccount.deposit(1000))
    my_bankaccount.withdraw(200)
    my_bankaccount.get_balance()
    my_bankaccount.close_account()

    print()

    # Versuch Einzahlung bei geschlossenem Konto
    my_bankaccount.deposit(50)
    my_bankaccount.open_account()
    my_bankaccount.deposit(50)
    my_bankaccount.get_balance()