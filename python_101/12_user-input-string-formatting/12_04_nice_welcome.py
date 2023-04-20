# Ask the user to input their name. Then print a nice welcome message
# that welcomes them personally to your script.
# If a user enters more than one name, e.g. "firstname lastname",
# then use only their first name to overstep some personal boundaries
# in your welcome message.

full_name = input("Please provide your name: ")
first_name = ""
if " " in full_name:
    for letter in full_name:
        if letter != " ":
            first_name += letter
        else:
            break
else:
    first_name = full_name
print(f"Welcome, {first_name}!")
