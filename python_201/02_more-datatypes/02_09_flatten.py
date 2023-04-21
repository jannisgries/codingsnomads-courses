# Write a script that "flattens" a shallow list. For example:
#
# starter_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
# flattened_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# Note that your input list only contains one level of nested lists.
# This is called a "shallow list".
#
# CHALLENGE: Do some research online and find a solution that works
# to flatten a list of any depth. Can you understand the code used?

starter_list = [[1, 2, [3, [7,8,9]], 4], [5, 6], [7, 8, 9]]
while True:
    end_list = []
    contains_list = False
    for el in starter_list:
        if type(el) == list:
            end_list += el
            contains_list = True
        else:
            end_list.append(el)
    starter_list = end_list
    if contains_list == False:
        break
print(end_list)
