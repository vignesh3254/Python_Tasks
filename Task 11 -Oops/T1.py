#1.
"""
Create a Student class with attributes like name, age, and marks.
Include methods to display the student’s information.
"""
class Student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Marks:",self.marks)


obj=Student("abc",21,271)
obj.display()
