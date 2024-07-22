#9.
"""
Create an abstract base class BankAccount with abstract methods deposit,
withdraw, and get_balance. Implement these methods in a subclass SavingsAccount.
"""


from abc import ABC,abstractmethod

class BankAccount(ABC):

    def __init__(self,get_balance=0):
        self.get_balance=get_balance
    @abstractmethod
    def deposit(self,amount):
        pass
    @abstractmethod
    def withdraw(self,amount):
        pass
    @abstractmethod
    def balance(self):
        pass

class SavingsAccount(BankAccount):

    def deposit(self,amount):
        self.get_balance=self.get_balance+amount
        print("Deposit Amoubt :",self.get_balance)
        
    def withdraw(self,amount):
        if amount<self.get_balance:
            print("Withdraw Amount :",amount)
            self.get_balance=self.get_balance-amount
        else:
            print("Insufficent Balance")

    def balance(self):
        print("Account Balance :",self.get_balance)

obj=SavingsAccount()

obj.deposit(100000)
obj.withdraw(10000)
obj.balance()
