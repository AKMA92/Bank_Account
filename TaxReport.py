from SavingAccount import SavingsAccount
from YouthAccount import YouthAccount


class TaxReport:

    def generate(self, bank_app):
        savings_total = 0.0
        youth_total = 0.0

        for account_object in bank_app.accounts_list:
            if isinstance(account_object, SavingsAccount):
                savings_total += account_object.balance
            elif isinstance(account_object, YouthAccount):
                youth_total += account_object.balance
        print()
        print("Tax report 2021 for fiscal year 2020")
        print(f"** Savings Account ** {savings_total:.2f} Fr")
        print(f"** Youth Account ** {youth_total:.2f} Fr")