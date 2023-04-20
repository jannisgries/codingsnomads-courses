# get a random word in german language from module
import zufallsworte as zufall
word_to_be_guessed = zufall.zufallswoerter(1)[0]
#Initialize Game Variables 
guessed_characters = []
remaining_tries = 10
word_to_display = ""
for letter in word_to_be_guessed:
    word_to_display += "_"
#Start Game
user_name = input("\nWelcome to a new game of hangman! What is your name: ")
print(f"\n\nPerfect, {user_name}! Let me explain the rules to you…", end="\n")
print(
    f"You have to guess the German word I chose for you. For this task you can ask any character of the alphabet – if it is in my word, i will tell you. But don´t run out of your total {remaining_tries} attempts to guess. Otherwise, you will loose. As a first hint, I will provide you the length of my word:", end="\n\n")
print(word_to_display, end="\n\n\n")
print("You may now make your first guess!", end="\n")
while remaining_tries > 0:
    # Input Validation in order to check if only one letter has been typed
    while True:
        guessed_character = input("\n\nType in any letter to make a guess: ").lower()
        if len(guessed_character) > 1:
            print("Sorry mate, but you are only allowed to type in ONE letter at a time, try again.", end="\n")
        elif len(guessed_character) == 0:
            print(
                "Sorry mate, but it seems you forgot to type in a letter, try again.", end="\n")
        elif guessed_character.isalpha() == False:
            print(
                "Sorry mate, but you are only allowed to type in letters, try again.", end="\n")
        else: 
            break  
    #Check if Character has been guessed befor 
    if guessed_character in guessed_characters:
        print("Looks like you already discovered tried this letter, try another one.")
        continue        
    #Add character to list of guessed ones
    guessed_characters.append(guessed_character)
    #Check if Guess is contained in word and diplay the word with the not guessed letters replaced
    if guessed_character in word_to_be_guessed:
        word_to_display = ""
        for letter in word_to_be_guessed:
            if letter in guessed_characters:
                word_to_display += letter
            else:
                word_to_display += "_"
        if word_to_be_guessed == word_to_display:
            print(
                f"\n\nCongratulations, you won the game with {remaining_tries} remaining tries! My word was: {word_to_be_guessed}")
            break
        else:
            print(
                f"\n\nCongratulations, you have found a character of my word. \n My word now looks like this: '{word_to_display}'", end="\n")
    elif guessed_character not in word_to_be_guessed:
        remaining_tries -= 1
        print(
            f"\n\nI am sorry mate, but this letter is not part of my word. You still have {remaining_tries} remaining tries and my word looks like this: '{word_to_display}'", end="\n")
if remaining_tries == 0:
    print(f"\n\nI am sorry, {user_name}, but you have lost the game!")


