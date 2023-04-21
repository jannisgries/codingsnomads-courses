# Write a script that takes a sentence from the user and returns:
# the number of lower case letters
# the number of uppercase letters
# the number of punctuations characters
# the total number of characters
import string 

user_input = input("Type in any sentence: ")
sentence = {
    "lower_case": 0,
    "upper_case": 0,
    "punctuation": 0,
    "total_letters": 0 
}
for char in user_input:
    if char != " ":
        sentence["total_letters"] += 1
        if char in string.punctuation:
            sentence["punctuation"] += 1
        elif char.isupper() == True:
            sentence["upper_case"] += 1
        elif char.islower() == True:
            sentence["lower_case"] += 1

for key, value in sentence.items():
    print(f"{key:<20} {value}", end="\n")