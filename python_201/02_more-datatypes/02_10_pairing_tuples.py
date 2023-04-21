# The import below gives you a new random list of numbers,
# called `randlist`, every time you run the script.
#
# Write a script that takes this list of numbers and:
#     - sorts the numbers
#     - stores the numbers in tuples of two in a new list
#     - prints each tuple
#
# If the list has an odd number of items,
# add the last item to a tuple together with the number `0`.
#
# Note: This lab might be challenging! Make sure to discuss it 
# with your mentor or chat about it on our forum.

# Write your code below here
from resources import randlist
sorted_list = randlist
sorted_list.sort()
counter = 0
list_of_tuples = []
for el in sorted_list:
    if counter % 2 == 0 and counter + 1 < len(sorted_list):
        tuple_ = tuple([sorted_list[counter], sorted_list[counter + 1]])
        list_of_tuples.append(tuple_)
    counter += 1
print(sorted_list)
print(list_of_tuples)

