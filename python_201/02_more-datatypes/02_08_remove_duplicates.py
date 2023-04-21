# Write code that removes all duplicates from a list.
# Solve this challenge in two ways:
# 1. Convert to a different data type
# 2. Use a loop and a second list to solve it more manually

list_ = [1, 2, 3, 4, 3, 4, 5]
second_list = list(set(list_))
third_list = []
for el in list_:
    if el not in third_list:
        third_list.append(el)
print(second_list, third_list)
