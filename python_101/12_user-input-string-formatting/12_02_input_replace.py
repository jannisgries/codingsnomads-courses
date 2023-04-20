# Write a script that takes a string of words and a symbol from the user.
# Replace all occurrences of the first letter with the symbol. For example:
#
# String input: more python programming please
# Symbol input: §
# Result: §ore python progra§§ing please

text = input("Please write any kind of text: ")
symbol = input("Please now provide the symbol, you want to replace the first letter with.")
first_letter = text[0]
for letter in text:
    if letter == first_letter:
        letter = symbol
    print(letter, end="") 
print("", end="\n")
