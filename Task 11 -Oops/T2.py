#2.
"""
Create a base class Employee with attributes name and salary.
Derive a class Manager that adds the department attribute.
Write a method in Manager to display all details.
"""

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary        
         
class Manager(Employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department=department

    def display(self):
         print("Name:",self.name)
         print("Salary:",self.salary)
         print("Department:",self.department)


obj=Manager("abc",25000,"IT")
obj.display()
