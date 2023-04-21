# Write a script that takes a text input from the user
# and creates a dictionary that maps the letters in the string
# to the number of times they occur. For example:
#
# user_input = "hello"
# result = {"h": 1, "e": 1, "l": 2, "o": 1}

user_input = input("please provide a string: ")
dict_of_letters = {}
for char in user_input:
    if char.isalpha():
        if char not in dict_of_letters.keys():
            dict_of_letters.update({char: 1})
        else:
            dict_of_letters[char] += 1
print(dict_of_letters)