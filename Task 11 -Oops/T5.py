#5.
"""
Create a class BankAccount with private attributes balance
and methods to deposit, withdraw, and check the balance.
"""

class BankAccount:
    def __init__(self,balance=0):
        self.__balance=balance

    def deposit(self,amount):
        self.__balance=self.__balance+amount
        print("Deposit Amount :",self.__balance)

    def withdraw(self,amount):
        if self.__balance > amount:
            print("Withdraw Amount:",amount)
            self.__balance=self.__balance-amount

        else:
            print("Insufficent Balance")

    def checkbalance(self):
        print("Amnt:",self.__balance)

obj=BankAccount()
obj.deposit(10000)
obj.withdraw(5000)
obj.checkbalance()
