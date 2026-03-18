from BankAccount import BankAccount

class SavingsAccount(BankAccount):
    interest_rate = 0.001

    def __init__(self, iban: str, currency="CHF"):
        super().__init__(iban, currency)

    def apply_interest(self):
        self.balance = self.balance + self.balance * self.interest_rate

    def withdraw(self, amount):
        if not self.active:
            return "Account is inactive"
        if amount <= 0:
            return "Amount must be positive"
        if self.balance < 0:
            fee = amount * 0.02
            amount += fee
            self.balance -= amount
            return f"Withdraw {amount} {self.currency}  succeeded"
        else:
            self.balance -= amount
            return f"Withdraw {amount} {self.currency}  succeeded"
