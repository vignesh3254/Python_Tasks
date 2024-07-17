#1
"""
create an abstract base "Vechicle" with abstract methods for starting.stopping,
and displaying vechicle information.

then create concrete classes 'Car' and 'Bike' that inherit from 'Vechicle'.
"""

from abc import ABC,abstractmethod

#abstract  class
class Vechicle(ABC):

    @abstractmethod #decrat
    def car(self,a,Model,V_number):
        pass

    @abstractmethod
    def bike(self,a,Model,V_number):
        pass

#concrete class / sub class

class Wheeler(Vechicle):
    def car(self,a,Model,V_number):
        if a=="start":
           print("Car is Starting")
        else:
            print("Car is Stopping")
        print("Model:",Model)
        print("Car number:",V_number)
        print()

    def bike(self,a,Model,V_number):
        if a=="start":
           print("Bike is Starting")
        else:
            print("Bike is Stopping")
        print("Model:",Model)
        print("Bike number:",V_number)

obj=Wheeler()


obj.car("","Rolce","TN41 A5432")
obj.bike("start","FZ","TN32 DB3254")
