# Write a script that reads in the contents of `words.txt`
import pathlib

file_path = pathlib.Path('/Users/jannisgries/Documents/codingnomads/courses/python_201/03_file-input-output').joinpath("words.txt")
new_file_path = pathlib.Path('/Users/jannisgries/Documents/codingnomads/courses/python_201/03_file-input-output').joinpath("words_reversed.txt")
with file_path.open() as file:
    str = file.read()

# and writes the contents in reverse to a new file `words_reverse.txt`.
reversed_str  = str[::-1]

with open(new_file_path, "w") as file:
    file.write(reversed_str)
