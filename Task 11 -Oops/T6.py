#6.
"""
Create an abstract class Animal with an abstract method sound.
Implement subclasses Dog and Cat with their specific
implementations of the sound method.
"""

from abc import ABC,abstractmethod

class Animal:

    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Bow Bow")

class Cat(Animal):
    def sound(self):
        print("Meow")

obj=Dog()
obj.sound()

obj1=Cat()
obj1.sound()
