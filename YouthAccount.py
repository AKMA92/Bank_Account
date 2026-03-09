from BankAccount import BankAccount


class YouthAccount(BankAccount):
    def __init__(self, iban: str, age, currency="CHF"):
        super().__init__(iban, currency)
        self.age = age
        if age > 25:
            pass

    def apply_interest(self):
        interest_rate = 0.02
        self.balance = self.balance + self.balance * interest_rate


    def monats_limit(self):
        pass


