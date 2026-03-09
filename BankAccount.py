class BankAccount:
    limit = 100000
    balance = 0.0
    active = True

    def __init__(self, iban: str, currency="CHF", withdraw_limit: float = 10000):
        self.iban = iban
        self.currency = currency
        self.withdraw_limit = withdraw_limit

#variable activ true setzen
    def open_account(self):
        self.active = True
        print("Account set to active")
#erhaltet als parameter Betrag
    def deposit(self, amount: float):
        if not self.active:
            print("Account is inactive")
            return False
        if amount <= 0:
            print("Amount must be positive")
            return False

        if amount + self.balance > self.limit:
            print("Limit exceeded")
            return False
        # aktueller Kontostand + Einzahlung
        self.balance += amount
        print(f"New balance: {self.balance} {self.currency}")
        return True

    def withdraw(self, amount: float):
        if not self.active:
            print("Account is inactive")
            return False
        if amount <= 0:
            print("Amount must be positive")
            return False
        if amount > self.balance:
            print("Insufficient balance")
            return False
        #Geld wird von konto abgezogen
        self.balance -= amount
        #neuer Kontostand
        print(f"New balance: {self.balance} {self.currency}")
        return True

    def get_balance(self):
        if not self.active:
            print("Access denied")
            return False
        print(f"Balance: {self.balance} {self.currency}")
        return self.balance

    def close_account(self):
        self.active = False
        print("Account set to inactive")


if __name__ == "__main__":

    # Objekt erstellen
    my_bankaccount = BankAccount("CH55555555555555555")

    # Methoden testen
    my_bankaccount.deposit(1000)
    my_bankaccount.withdraw(200)
    my_bankaccount.get_balance()
    my_bankaccount.close_account()

    print()

    # Versuch Einzahlung bei geschlossenem Konto
    my_bankaccount.deposit(50)
    my_bankaccount.open_account()
    my_bankaccount.deposit(50)
    my_bankaccount.get_balance()