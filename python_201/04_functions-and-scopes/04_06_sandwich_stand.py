# Write a function called `make_sandwich()` that sticks to the following:
# - takes a type of bread as its first, required argument
# - takes an arbitrary amount of toppings
# - returns a string representing a sandwich with the bread on top
#   and bottom, and the toppings in between.

def make_sandwich(type_of_bread: str, *args:str) -> str:
    length_of_bread_type = len(type_of_bread)
    variable_bread_representation = "_" * length_of_bread_type
    toppings = ", ".join(args)
    length_of_bread = length_of_bread_type + 10
    length_of_sandwich = len(toppings) + 10
    whitespace_filler = " " * int((length_of_sandwich - length_of_bread) / 2)
    sandwich = f"""
    {whitespace_filler} ____{variable_bread_representation}____
    {whitespace_filler}/____{type_of_bread}____\\
    
    |    {toppings}    |
    {whitespace_filler} ____{variable_bread_representation}___
    {whitespace_filler}\\____{type_of_bread}____/

    """
    return sandwich
make_sandwich("wheat", "salad", "meat")