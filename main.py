class BankAccount:


    def __init__(self, account_nr, iban, balance, currency):
        self.account_no = account_nr
        self.iban = iban
        self.currency = currency
        self.balance = balance


    def open_account(self):
        # Logik implementieren
        pass

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def show_balance(self):
        # Logik implementieren
        pass

    def close_account(self):
        # Logik implementieren
        pass






if __name__ == '__main__':
    # objekt erstellen
    my_bankaccount = BankAccount()

    # Methoden aufrufen
    my_bankaccount.deposit(100)
    my_bankaccount.withdraw(100)
    my_bankaccount.show_balance()
    my_bankaccount.open_account()
    my_bankaccount.close_account()

