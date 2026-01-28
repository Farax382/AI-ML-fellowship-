# bank_account.py

class BankAccount:
    def __init__(self, holder_name, balance=0):
        self.holder_name = holder_name
        self._balance = balance   # encapsulation (protected)

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self._balance

    def __str__(self):
        return f"Account Holder: {self.holder_name}, Balance: {self._balance}"


# Inheritance
class SavingsAccount(BankAccount):
    def __init__(self, holder_name, balance=0, interest_rate=0.05):
        super().__init__(holder_name, balance)
        self.interest_rate = interest_rate

    # Polymorphism
    def apply_interest(self):
        interest = self._balance * self.interest_rate
        self._balance += interest
        print("Interest added")


# Testing
if __name__ == "__main__":
    acc = BankAccount("Faraz", 1000)
    acc.deposit(500)
    acc.withdraw(300)
    print(acc)

    sav = SavingsAccount("Faraz", 2000)
    sav.apply_interest()
    print(sav)
