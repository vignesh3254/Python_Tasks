#2
"""
create an abstract base class 'Employee' , with abstract methods for
"calculating salary" and "display employee information"

then create concrete classes "FulltimeEmployee",and "ParttimeEmployee" that
inherit from "Employee"

"""
from abc import ABC,abstractmethod

class Employee(ABC):

    @abstractmethod
    def fulltime(self,name,age):
        pass

    @abstractmethod
    def parttime(self,name,age):
        pass

class Company(Employee):
    def __init__(self):
        self.full=700
        self.part=350
        

    def fulltime(self,name,age):
        
        a=int(input("Working Days:"))
        print()
        print("Salary:",a*self.full)
        print("Employee name:",name)
        print("Age:",age)
        print()
    def parttime(self,name,age):
        a=int(input("Working Days:"))
        print()
        print("Salary",a*self.part)
        print("Employee name:",name)
        print("Age:",age)

obj=Company()
print("Full Time Job")
name=input("Enter Your Name:")
age=int(input("Enter Your Age:"))
obj.fulltime(name,age)

print("Part Time Job")
name1=input("Enter Your Name:")
age1=int(input("Enter Your Age:"))
obj.parttime(name1,age1)



        
