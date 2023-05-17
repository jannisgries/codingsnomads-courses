# Demonstrate how to create a generator object.
# Print the object to the console to see what you get.
# Then iterate over the generator object and print out each item.
gen = (x**2 for x in range(1, 11))
for el in gen:
    print(el)