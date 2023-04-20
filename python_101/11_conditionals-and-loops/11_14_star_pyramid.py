# Write a script that prints a star pyramid of flexible size
# If the `stars` variable is `5`, your code will output:
#
# *
# * *
# * * *
# * * * *
# * * * * *
#
# There should be five rows in total:
# 1. the 1st row will have 1 star,
# 2. the 2nd row will have 2 stars,
# 3. the 3rd row will have 3 stars,
# 4. the 4th row will have 4 stars,
# 5. the 5th row will have 5 stars
#
# Another example: if you set the `stars` variable tp `3`,
# your code will output:
#
# *
# * *
# * * *
#
# HINT: Think of nested for loops!

stars = 5

for star in range(1, stars + 1):
    # print row
    row = star
    for number_of_stars in range(1, row + 1):
        print("*", end=" ")
    print("", end="\n")

# Alternative
# var = int(input('Insert pyramid number'))
# x='*'
# for i in range(var+1):
#    print(i*x)