# Write a function that prints out nicely formatted information about a
# real estate advertisement. The information can vary for every advertisement, which
# is why your function should be able to take an arbitrary amount of
# keyword arguments, and display them all in a list form with some 
# introductory information.

def print_information(**kwargs):
    print("This is the perfect time to search for a new home. A new place to live and feel safe. Maybe this is something for you ? Have a look:", end="\n\n")
    for key, value in kwargs.items():
        print(f"{key:<15} {value}")

print_information(name="Hawaiian place", place="hamburg", rooms=5)