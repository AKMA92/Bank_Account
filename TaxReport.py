from SavingAccount import SavingsAccount
from YouthAccount import YouthAccount
import requests


class TaxReport:

    def __init__(self):
        url = "https://api.frankfurter.dev/v1/latest?base=CHF&symbols=USD,EUR"
        data = requests.get(url).json()
        print()
        print(data)
        print()

        self.usd = 1 / data["rates"]["USD"]  # USD → CHF
        self.eur = 1 / data["rates"]["EUR"]  # EUR → CHF

    def generate(self, app):

        savings_total = 0.0
        youth_total = 0.0

        accounts_list = app.accounts_list
        for account in accounts_list:
            if account.get_currency() == "USD" and isinstance(account, SavingsAccount):
                savings_total += account.get_balance() * self.usd

            elif account.get_currency() == "EUR" and isinstance(account, SavingsAccount ):
                savings_total += account.get_balance() * self.eur

            elif account.get_currency() == "CHF" and isinstance(account, SavingsAccount):
                savings_total += account.get_balance()

            elif account.get_currency() == "USD" and isinstance(account, YouthAccount):
                youth_total += account.get_balance() * self.usd

            elif account.get_currency() == "EUR" and isinstance(account, YouthAccount):
                youth_total += account.get_balance() * self.eur

            elif account.get_currency() == "CHF" and isinstance(account, YouthAccount):
                youth_total += account.get_balance()

        print()
        print("Tax report 2021 for fiscal year 2020")
        print(f"** Savings Account ** {savings_total:.2f} Fr")
        print(f"** Youth Account ** {youth_total:.2f} Fr")