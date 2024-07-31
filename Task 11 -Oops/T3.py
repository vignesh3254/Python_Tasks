#3.
"""
Create two base classes Person and Employee,
each with their own attributes and methods.
Create a derived class Manager that inherits
from both and displays details from both base classes.
"""

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display_p(self):
        print("Name:",self.name)
        print("Age:",self.age)

class Employee:
    def __init__(self,idn,salary):
        self.id_n=idn
        self.salary=salary

    def display_e(self):
        print("ID Number:",self.id_n)
        print("Salary:",self.salary)

class Manager(Person,Employee):
    def __init__(self,name,age,idn,salary):
        Person.__init__(self,name,age)
        Employee.__init__(self,idn,salary)

    def displays(self):
        self.display_p()
        self.display_e()

obj=Manager("abc",28,101,32500)
obj.displays()
