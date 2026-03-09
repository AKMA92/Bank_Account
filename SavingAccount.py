from BankAccount import BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, iban: str, currency="CHF"):
        super().__init__(iban, currency)

    def apply_interest(self):
        interest_rate = 0.001
        self.balance = self.balance + self.balance * interest_rate
        pass

    def withdraw_negative(self, amount):
        if self.balance < 0:
            fee = amount * 0.02
        pass
