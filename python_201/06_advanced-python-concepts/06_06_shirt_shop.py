# Using a list comprehension, create a *cartesian product* (google this!)
# of the given lists. Then open up your online shop ;)

colors = ["neon orange", "spring green"]
sizes = ["S", "M", "L"]

cartesian_list = [color + " in size " + size for color in colors for size in sizes]
print(cartesian_list)
