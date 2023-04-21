# Take in a few numbers from the user and place them in a list.
# If you want, you can instead use the provided randomly generated
# list called `randlist` to simulate the user input.
#
# Find the largest number in the list and print the result.
# Calculate the product of all of the numbers in the list.

from resources import randlist

user_input = randlist
randlist.sort()
print(
    randlist[-1]
)

# Other Approach
biggest_number = 0
for el in randlist:
    if type(el) == int or type(el) == float:
        if el > biggest_number:
            biggest_number = el
print(biggest_number)
