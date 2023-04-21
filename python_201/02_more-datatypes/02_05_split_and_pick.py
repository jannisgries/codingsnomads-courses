# Write a script that takes in a string from the user.
# Using the `split()` method, create a list of all the words in the string
# and print back the most common word in the text.

user_input = input("Type something: ")
list_of_words = user_input.lower().split()
count_of_words = {}
highest_counted_word = ""
highest_count = 0

# Apporach without using count() method
for word in list_of_words:
    if word in count_of_words:
        count_of_words[word] += 1
    else:
        count_of_words[word] = 1
for word, counter in count_of_words.items():
    if counter > highest_count:
        highest_counted_word = word
        highest_count = counter
    elif counter == highest_count:
        highest_counted_word += ", " + word

# Approch with using count() method
for word in set(list_of_words):
    counter = list_of_words.count(word)
    if counter > highest_count:
        highest_count = counter
        highest_counted_word = word
    elif counter== highest_count:
        highest_counted_word += ", " + word

# Print result
print(f"The word(s) '{highest_counted_word}' is / are occuring {highest_count} times in the string.", end="\n\n")
