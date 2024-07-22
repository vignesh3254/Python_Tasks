#10.
"""
Define an abstract base class Payment with an abstract method pay.
Create two subclasses CreditCardPayment and PayPalPayment that implement 
the pay method.
"""

from abc import ABC,abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self):
        pass

class CreditCardPayment(Payment):

    def pay(self):
        print("CreditCardPayment Method")

class PayPalPayment(Payment):
    def pay(self):
        print("PayPalPayment Method")

obj = CreditCardPayment()
obj.pay()

obj1= PayPalPayment()
obj1.pay()
