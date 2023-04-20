# Re-create the guess-my-number game from scratch. Don't peek!
# This time, give your players only a certain amount of tries
# before they lose.

import random

number_to_guess = random.randint(1, 1)
guessed_number = ""
remaining_tries = 3
print("Hello! You may guess my number, which can be any number between 1 and 10.")
while number_to_guess != guessed_number:
    if remaining_tries == 0:
        break
    while True:
        guessed_number = input("Guess my number: ")
        if guessed_number.isnumeric() == False:
            print("Please provide a number, not a character")
        else:
            guessed_number = int(guessed_number)
            if guessed_number > 10 or guessed_number < 1:
                print("Sorry, only numbers between 1 and 10 are allowed")
            else:
                break
    if number_to_guess != guessed_number:
        print("Sorry mate, try again!")
    remaining_tries -= 1
    
if number_to_guess == guessed_number:
    print(f"Congratualations, you found my number, it was {number_to_guess}!")
else:
    print(f"Sorry mate, but you run out of tries! My number was {number_to_guess}!")