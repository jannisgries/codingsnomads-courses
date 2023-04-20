# Write the necessary code calculate the volume and surface area
# of a cylinder with a radius of 3.14 and a height of 5.
# Print out the result.
import math
radius = 3.14
height = 5
surface_bottom = radius ** 2 * math.pi
scope_bottom = radius * 2 * math.pi
volume = surface_bottom * height
surface = (scope_bottom * height) + 2 * surface_bottom
print("volume: " + str(volume) + "; surface area: " + str(surface))
