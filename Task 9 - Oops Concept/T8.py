#8.
"""
Define a class Person with private attributes name and age.
Provide public methods to get and set the values of these attributes
(Use getter and setter)
"""

class Person:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age

    def get_data(self):
        print("Name:",self.__name)
        print("Age:",self.__age)

    def set_data(self,names,ages):
        self.__name=names
        self.__age=ages

obj=Person("Ajay",20)

obj.get_data()

obj.set_data("Anbu",27)

obj.get_data()
