# Write code that creates a list of all unique values in a list.
# For example:
#
# list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
# unique_list = [55, 'hi', 4, 13]

list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
unique_els =  []
for el in list_:
    if el not in unique_els:
        unique_els.append(el)
    else:
        unique_els.remove(el)

print(unique_els)