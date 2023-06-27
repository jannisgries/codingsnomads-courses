# Go to https://stackoverflow.com/questions/tagged/python?tab=Newest
# and look through some of the newest questions tagged with "Python".

# Pick one of the questions that includes a code snippet and try to get
# it working in your local environment.

# Use your debugger to attempt to solve the challenge that the user ran into.
# If you can solve it, post your solution as an answer to the question.

def convert(x: str):
    if x.isalpha() == True:
        converted_value = x
    elif x.isnumeric() == True:
        converted_value = int(x)
    return converted_value

def splitValue(inp: list):
    inp_as_list = []
    element = ""
    for el in inp: 
        if el not in [" ", ",", ";"]:
            element += el
        else:
            if element != "": 
                inp_as_list.append(element)
                element = ""
    inp_as_list.append(element)
    return inp_as_list

def merge(list1,list2):
    merged_list,sorted_list=(list1+list2),[]
    while len(merged_list)>0 :
        sorted_list.append(min(merged_list))
        merged_list.remove(min(merged_list))
    return sorted_list

list1 = [convert(x) for x in splitValue(input("Enter the elements of list: "))]
list2 = [convert(x) for x in splitValue(input("Enter the elements of list: "))]
print(merge(list1,list2))