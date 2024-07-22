#3.
"""
Create a child class Bus that will inherit all of the variables and methods
of the Vehicle class(Parent class).
"""

class Vehicle:
    
    def bus(self,company):
        print("Bus Company Name:",company)

class Bus(Vehicle):
    pass
        
obj=Bus()
obj.bus("Eicher")
