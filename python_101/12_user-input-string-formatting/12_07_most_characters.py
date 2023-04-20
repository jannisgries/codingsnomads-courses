# Write a script that takes three strings from the user
# and prints the longest string together with its length.
#
# Example Input:
#     hello
#     world
#     greetings
#
# Example Output:
#     9, greetings

string1 = input("Write a string: ")
string2 = input("Write another string: ")
string3 = input("Write a third string: ")
string_length = ""

if len(string1) > len(string2) and len(string1) > len(string3):
    longest_string = string1
elif len(string2) > len(string1) and len(string2) > len(string3):
    longest_string = string2
elif len(string3) > len(string1) and len(string3) > len(string2):
    longest_string = string3
else:  # some strings are same length
    if len(string1) == len(string2) == string3:
        longest_string = string1 + " & " + string2 + " & " + string3
        string_length = len(string1)
    elif len(string1) == len(string2):
        longest_string = string1 + " & " + string2
        string_length = len(string1)
    elif len(string2) == len(string3):
        longest_string = string2 + " & " + string3
        string_length = len(string2)
    elif len(string1) == len(string3):
        longest_string = string1 + " & " + string3
        string_length = len(string1)

if string_length == "":
    string_length = len(longest_string)

print(f"{string_length}, {longest_string}")
