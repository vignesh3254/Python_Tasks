class Animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        print("animal speaks")
class Dog(Animal):
    def speak(self):
        print("dog barks")

obj=Dog("doggy")
obj.speak()
