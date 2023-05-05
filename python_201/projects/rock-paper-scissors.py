import random

def get_hand(number: int) -> str:
    # 0 = scissor, 1 = rock, 2 = paper
    if number == 0:
        hand = "scissor"
    elif number == 1:
        hand = "rock"
    elif number == 2:
        hand = "paper"
    return hand

def determine_winner(user_number: int, comp_number:int) -> str:
    if user_number == 0:
        if comp_number == 0:
            winner = "tie"
        elif comp_number == 1:
            winner = "comp"
        else: 
            winner = "user"
    elif user_number == 1:
        if comp_number == 0:
            winner = "user"
        elif comp_number == 1:
            winner = "tie"
        else: 
            winner = "comp"
    else:
        if comp_number == 0:
            winner = "comp"
        elif comp_number == 1:
            winner = "user"
        else: 
            winner = "tie"
    return winner

record = {
    "user_wins": 0,
    "comp_wins": 0,
    "ties": 0
}

# take in a number 0-2 from the user that represents their hand
print("Welcome to a new game of Rock-Paper-Scissors! \n\nYou´ll have to choose your hand now: ", end="\n\n")
while True:
    user_input = input("Please type in '0' for scissor, '1' for rock, '2' for paper or 'exit' to quit: ")
    if user_input.lower() ==  "exit":
        break
    elif user_input.isnumeric() == True and int(user_input) < 3 and int(user_input) > -1:
        user_number = int(user_input)
        comp_number = random.randint(0,2)
        user_hand = get_hand(user_number)
        comp_hand = get_hand(comp_number)
        winner = determine_winner(user_number = user_number, comp_number = comp_number)
        print("\n")
        if winner == "tie":
            record["ties"] += 1
            print(f"Ah, you both took {user_hand}, let´s try again")
            print(f"Your current record: Your wins: {record['user_wins']}, Computer wins: {record['comp_wins']}, Ties: {record['ties']}", end="\n\n")
        elif winner == "user":
            record["user_wins"] += 1
            print(f"Congrats, you took {user_hand}, the computer chose {comp_hand} - you have won the game. Let´s go again.")
            print(f"Your current record: Your wins: {record['user_wins']}, Computer wins: {record['comp_wins']}, Ties: {record['ties']}", end="\n\n")
        elif winner == "comp":     
            record["comp_wins"] += 1
            print(f"I am sorry, you chose {user_hand}, your opponent went for {comp_hand} - you lost this round. Let´s go again.")
            print(f"Your current record: Your wins: {record['user_wins']}, Computer wins: {record['comp_wins']}, Ties: {record['ties']}", end="\n\n")
    else:
        print("I am sorry, but you have to type in an appropriate number.", end="\n")
        
print("Thanks for playing!", end="\n\n")
# generate a random number 0-2 to use for the computer's hand
# call the function get_hand to get the string representation of the user's hand
# call the function get_hand to get the string representation of the computer's hand
# call the function determine_winner to figure out who won
# print out the player hand and computer hand
# print out the winner
