# Ask your user for a number between 0 and 1,000,000,000.
# Use a `while` loop to find the number. When the number is found,
# exit the loop and print the number to the console.

number = int(input("Please provide a number between 1 and 1000000000: "))
tried_number = 0
found_number = ""
while found_number == "":
    if tried_number == number:
        found_number = number
    else:
        tried_number += 1
print(found_number)