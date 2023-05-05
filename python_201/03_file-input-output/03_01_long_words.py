# Write a program that reads in `words.txt` and prints only the words
# that have more than 20 characters (not counting whitespace).
import pathlib

file_path = pathlib.Path('/Users/jannisgries/Documents/codingnomads/courses/python_201/03_file-input-output').joinpath("words.txt")
with file_path.open() as file:
    str = file.read()
# Create List out of string
list_of_words = str.split()

# Loop through list to filter
filtered_list_of_words = []
for word in list_of_words:
    if len(word) > 20:
        filtered_list_of_words.append(word)

# Print result
print(*filtered_list_of_words, sep="\n")