from BankAccount import BankAccount


class YouthAccount(BankAccount):
    monthly_withdraw_limit = 2000

    def __init__(self, iban: str, age, currency="CHF"):
        super().__init__(iban, currency)
        self.withdrawn_this_month = 0
        self.age = age
        if age > 25:
            raise ValueError("Error: Youth accounts are only allowed for people aged 25 or below")

    def apply_interest(self):
        interest_rate = 0.02
        self.balance = self.balance + self.balance * interest_rate

    def check_monthly_withdraw_limit(self, amount):
        if self.withdrawn_this_month + amount > self.monthly_withdraw_limit:
            print("The monthly withdrawal limit is $2,000.")
            return False
        else:
            return True

    def withdraw(self, amount):
        if not self.active:
            return "Account is inactive"
        if amount <= 0:
            return "Amount must be positive"
        if not self.check_monthly_withdraw_limit(amount):
            return "Monthly withdrawal limit exceeded"
        self.balance -= amount
        self.withdrawn_this_month += amount
        return f"Withdraw {amount} {self.currency} succeeded"