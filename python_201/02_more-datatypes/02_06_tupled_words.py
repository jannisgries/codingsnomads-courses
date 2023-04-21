# Write a script that takes a string from the user
# and creates a list that contains a tuple for each word.
# For example:

# input = "hello world"
# result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

user_input = input("Please provide a string: ")
words = user_input.split()
result_list = []
for word in words:
    tuple_of_word = []
    for letter in word:
        tuple_of_word.append(letter)
    tuple_of_word = tuple(tuple_of_word)
    result_list.append(tuple_of_word)

print(result_list)