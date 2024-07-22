#4.
"""
Create a Bus class that inherits from the Vehicle class.
Give the capacity argument of Bus.seating_capacity() a default value of 50.
"""

class Vehicle:
    def __init__(self):
        self.capacity=50
    def seating_capacity(self):
        print(f"default seat capacity {self.capacity}")

class Bus(Vehicle):
    pass

Bus=Bus()
Bus.seating_capacity()
