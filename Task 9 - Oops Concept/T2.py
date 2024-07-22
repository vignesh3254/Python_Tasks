#2.
"""
Write a Python program to create a calculator class.
Include methods for basic arithmetic operations.
(Addition, Subtraction, Multiplication,  Division )
"""

class Calculater:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def addition(self):
        print("Addition:",self.a+self.b)

    def subtraction(self):
        print("Subtraction:",self.a-self.b)

    def multiplication(self):
        print("Multiplication:",self.a*self.b)

    def division(self):
        print("Division:",self.a/self.b)

obj=Calculater(10,2)

obj.addition()
obj.subtraction()
obj.multiplication()
obj.division()
