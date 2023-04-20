# Write a program that takes a number between 1 and 1,000,000,000
# from the user and determines whether it is divisible by 3 using an `if` statement.
# Print the result.

number = int(input("Please provide a numver between 1 and 1 000 000"))
if number % 3 == 0:
    print(f"Congrats, this number is divisable through 3. The result than is {number / 3}")
else:
    print("Sorry, this number is not divisable through 3.")