# Create a `Planet()` class that models attributes and methods of
# a planet object.
# Use the appropriate dunder method to get informative output with `print()`

class Planet():
    def __init__(self, name, weight, color, primary_element, diameter, distance_to_sun, amount_of_moons) -> None:
        self.name = name
        self.weight = weight
        self.color = color
        self.primary_element = primary_element
        self.diameter = diameter
        self.distance_to_sun = distance_to_sun
        self.amount_of_moons = amount_of_moons
    def __str__(self) -> str:
        return f"{self.name}, {self.weight} kg, {self.color}, {self.primary_element}, {self.diameter}, {self.distance_to_sun}, {self.amount_of_moons}"


