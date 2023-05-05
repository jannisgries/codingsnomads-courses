# Read in all the words from the `words.txt` file.
import pathlib

file_path = pathlib.Path('/Users/jannisgries/Documents/codingnomads/courses/python_201/03_file-input-output').joinpath("words.txt")
with file_path.open() as file:
    str = file.read()
# Create List out of string
list_of_words = str.split()


# Then find and print:
# Loop through list to filter
current_highest_length = 0
current_shortest_length = 10000
longest_word = []
shortest_word = []
word_count = 0
for word in list_of_words:
    # 1. The shortest word (if there is a tie, print all)
    if len(word) < current_shortest_length:
        shortest_word = [word]
        current_shortest_length = len(word)
    elif len(word) == current_shortest_length:
        shortest_word.append(word)
    
    # 2. The longest word (if there is a tie, print all)
    if len(word) > current_highest_length:
        longest_word = [word]
        current_highest_length = len(word)
    elif len(word) == current_highest_length:
        longest_word.append(word)
    
    # 3. The total number of words in the file.
    word_count += 1

# Print result
# 1. Shortest Word
print(f"1. Shortest Word ({current_shortest_length})")
print(*shortest_word, sep=", ", end=" \n\n")

# 2. Longest Word
print(f"2. Longest Word ({current_highest_length})")
print(*longest_word, sep=", ", end=" \n\n")

# 3. Number of Words
print(f"3. Total number of words: {word_count}")
