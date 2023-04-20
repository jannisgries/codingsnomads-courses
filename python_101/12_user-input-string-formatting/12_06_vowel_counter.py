# Write a script that takes a string input from a user
# and prints a total count of how often each individual vowel appeared.

text = input("Please provide the text, you want to count the vowels of: ")
a_count = 0
e_count = 0
i_count = 0
o_count = 0
u_count = 0
for letter in text:
    if letter == "a":
        a_count += 1
    elif letter == "e":
        e_count += 1
    elif letter == "i":
        i_count += 1
    elif letter == "o":
        o_count += 1
    elif letter == "u":
        u_count += 1

print(f"In your text,\nletter a appears {a_count} times \nletter e appears {e_count} times \nletter i appears {i_count} times \nletter o appears {o_count} times \nletter u appears {u_count} times.")