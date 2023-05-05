# Write a script where you complete the following tasks:
# - define a function that determines whether the number is
#   divisible by 4 OR 7 and returns a boolean
# - define a function that determines whether a number is
#   divisible by both 4 AND 7 and returns a boolean
# - take in a number from the user between 1 and 1,000,000,000
# - call your functions, passing in the user input as the arguments,
#   and set their output equal to new variables
# - print your the result variables with descriptive messages

def is_devisible_or(number: int):
    if number % 4 == 0 or number % 7 == 0:
        return True
    else:
        return False
def is_devisible_and(number: int):
    if number % 4 == 0 and number % 7 == 0:
        return True
    else:
        return False

while True:
    user_input = input("Please provide a number between 1 and 1.000.000.000: ")
    if user_input.isnumeric() and int(user_input) > 0 and int(user_input) < 1000000001:
        number_input = int(user_input)
        break
    else: 
        print("\nSorry, but you didn´t provide a sufficient number.\n\n")


devisible_or = is_devisible_or(number_input)
devisible_and = is_devisible_and(number_input)

print(f"""
Your number is devisible through 4 and 7: {devisible_and}
Your number is devisible through 4 or 7: {devisible_or}
""")
