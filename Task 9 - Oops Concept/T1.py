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

    def cal_age(self,current_year):

        age=current_year - self.dob
        return age
    
    def display(self):
        print(f"Name:{self.name}\nCountry:{self.country}\nDate of Birth:{self.dob}")

obj=Person("Bala","India",1997)
obj.display()

age=obj.cal_age(2024)
print("Age is :",age)
