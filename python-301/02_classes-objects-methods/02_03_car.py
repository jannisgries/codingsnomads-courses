# The classic OOP example: Write a class to model a car. The class should:
#
# 1. Set the attributes model, year, and max_speed in the `__init__()` method.
# 2. Have a method that increases the `max_speed` of the car by 5 when called.
# 3. Have a method that prints the details of the car.
#
# Create at least two different objects of this `Car()` class and demonstrate
# changing the objects' attributes.

class Car:
    def __init__(self, model, year, max_speed) -> None:
        self.model = model
        self.year = year
        self.max_speed = max_speed

    def __str__(self) -> str:
        return f"{self.model}, {self.year}, {self.max_speed} km/h"
    
    def tune_car(self):
        self.max_speed += 5


volvo = Car("Volvo XC60", 2016, 160)
porsche = Car("Porsche 911", 2020, 320)
porsche.tune_car()
print(volvo)
print(porsche)