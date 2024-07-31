#4.
"""
Implement a class Shape with a method area.
Create subclasses Rectangle and Circle that override
the area method to calculate areas of a rectangle and a circle, respectively.
"""

class Shape:

    def area(self,l,b):
        pass
class Rectangle(Shape):
    def area(self,l,b):
        print(l*b)

class Circle(Shape):
    def area(self,b):
        a=3.14*b*b
        print("%.2f" % a)

obj=Rectangle()
obj1=Circle()

obj.area(5,4)
obj1.area(3)

