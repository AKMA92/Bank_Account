from time import sleep
from SavingAccount import SavingsAccount
from YouthAccount import YouthAccount

sleeptime: int = 10

# Saving Account testen
print("=== Saving Account Simulation ===")
saving = SavingsAccount("CH111111111111111111")
print(saving.deposit(1000))
print("Balance:", saving.get_balance())
print("Waiting 10 seconds (1 simulated month)...")

sleep(sleeptime)

saving.apply_interest()
print("Balance after 1 month:", saving.get_balance())
print("Waiting 20 seconds (2 more months)...")

sleep(sleeptime+sleeptime)

saving.apply_interest()
saving.apply_interest()
print("Balance after 3 months:", saving.get_balance())


# Youth Account testen
print("\n=== Youth Account Simulation ===")
youth = YouthAccount("CH222222222222222222", age=20)
print(youth.deposit(3000))
print("Balance:", youth.get_balance())
print(youth.withdraw(100))
print(youth.withdraw(200))  # sollte Limit überschreiten
print("Waiting 10 seconds (new month)...")

sleep(sleeptime)

# Monatslimit manuell resetten für neue Periode
youth.reset_withdrawn_this_month()
print(youth.withdraw(2500))
print("Balance:", youth.get_balance())
print(youth.withdrawn_this_month)
