from abc import ABC, abstractmethod

# Abstract Class
class ATM(ABC):

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def check_balance(self):
        pass


# Concrete Class
class SBIATM(ATM):
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Insufficient balance.")

    def deposit(self, amount):
        self.balance += amount
        print(f"₹{amount} deposited successfully.")

    def check_balance(self):
        print(f"Available Balance: ₹{self.balance}")


# Creating object
atm = SBIATM(10000)

atm.check_balance()
atm.deposit(2000)
atm.withdraw(5000)
atm.check_balance()