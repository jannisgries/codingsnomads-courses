# MEMORY GAME WITH SETS
# Continuously collect number input from a user with a `while` loop.
# Confirm that the input can be converted to an integer,
# then add it to a Python `set()`.
# If the element was already in the set, notify the user that their
# their input is a duplicate and deduct a point.
# If the user loses 5 points, quit the program.
# They win if they manage to create a set that has more than 10 items.

points = 5
set_of_numbers = set()
while points != 0:
    while True:
        number = input("Please provide a number: ")
        if number.isnumeric() == True:
            number = int(number)
            break
        else:
            print("Sorry mate, you have to provide a number", end="\n\n")
    if number not in set_of_numbers:
        set_of_numbers.add(number)
        print("Ok,I saved this number", end="\n\n")

    else: 
        points -= 1
        print(f"Sorry, this number is already in your set of numbers, as you´ve lost a point you have reamaing {points} points", end="\n\n")
memorized_items = len(set_of_numbers)
if memorized_items <= 10:
    print(f"Sorry, but you have lost. You were able to memorize {memorized_items} numbers!", end="\n\n")
else:
    print(f"Congrats, you have won. You were able to memorize {memorized_items} numbers!", end="\n\n")