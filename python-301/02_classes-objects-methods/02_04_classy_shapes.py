# Create two classes that model a rectangle and a circle.
# The rectangle class should be constructed by length and width
# while the circle class should be constructed by radius.
#
# Write methods in the appropriate class so that you can calculate
# the area of both the rectangle and the circle, the perimeter
# of the rectangle, and the circumference of the circle.

from math import pi

class Rectangle:
    def __init__(self, length, width) -> None:
        self.length = length
        self.width = width
    def get_area(self):
        return self.length * self.width
    def get_circumference(self):
        return 2 * (self.length + self.width)

    
class Circle:
    def __init__(self, radius) -> None:
        self.radius = radius
    def get_area(self):
        return pi * self.radius**2
    def get_circumference(self):
        return 2 * self.radius * pi
    

r1 = Rectangle(5, 2)
print(r1.get_area(), r1.get_circumference())
c1 = Circle(3)
print(c1.get_area(), c1.get_circumference())