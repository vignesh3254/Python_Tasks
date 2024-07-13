#2
"""
create a base class "Vechile" with attributes 'make' and 'model' then create
a derived class "Car", that inherits from "Vechile",and adds an attribute 'year'
use super() in the "Car" class constructer to initialize the 'make' and 'model'
attributes.create an object of the 'car' print its details
"""

class Vechile:
    def __init__(self,make,model):
        self.make=make
        self.model=model

    def Vehicle_d(self):
        print(f"Make:{self.make} \nModel:{self.model}")
class Car(Vechile):
    def __init__(self,make,model,year):
        super().__init__(make,model)
        self.year=year

    def Car_d(self):
        super().Vehicle_d()
        print(f"Year:{self.year}")
obj=Car(2012,"Rolce",2020)
obj.Car_d()
