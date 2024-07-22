#1.
"""
Write a Python program to create a person class. Include  attributes like
name,country and date of birth.Implement a method to determine the person's age
"""

class Person:
    def __init__(self,name,country,dob):
        self.name=name
        self.country=country
        self.dob=dob

    def display(self,age=25):
        print(f"Name:{self.name}\nCountry:{self.country}\nDate of Birth:{self.dob}\nAge:{age}")

obj=Person("Bala","India","25-Jun-1997")
obj.display()
