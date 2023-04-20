# Write a script that takes a string of words and a letter from the user.
# Find the index of first occurrence of the letter in the string. For example:
#
# String input: hello world
# Letter input: o
# Result: 4

text = input("Please write any kind of text: ")
letter = input("Please now provide the letter, you want to search for in the text.")
index = text.find(letter)
result = f"The letter '{letter}' is firstly contained in the provided text on {index}."
print(result)