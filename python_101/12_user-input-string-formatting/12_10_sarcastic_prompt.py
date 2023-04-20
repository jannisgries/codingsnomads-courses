# Create a sarcastic program that asks a user for their honest opinion,
# then prints the same sentence back to them in aLtErNaTiNg CaPs.
text = input("Please provide your opionion now: ")
counter = 0
for letter in text:
        if letter != " ":
            counter += 1
            if counter % 2 == 0:
                letter = letter.upper()
            else:
                letter = letter.lower()
        print(letter, end="")
print("", end="\n")