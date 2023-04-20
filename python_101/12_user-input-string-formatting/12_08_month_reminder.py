# Take in a number between 1 and 12 from the user
# and print the name of the associated month:
# "January", "February", ... "December"
# Print "Error" if the number from the user is not between 1 and 12.
# Use a nested `if` statement. > Nö 
# Use of List qould be way easier, but not introduced yet
month_number = ""
month = ""
while month_number == "":
    month_number = int(input("Please provide a number between 1 and 12: "))
    if month_number < 1 or month_number > 12:
        print("Sorry, this number is not between 1 and 12, try again", end="\n")
        month_number = ""

if month_number == 1:
    month = "January"
elif month_number == 2:
    month = "Febuary"
elif month_number == 3:
    month = "March"
elif month_number == 4:
    month = "April"
elif month_number == 5:
    month = "May"
elif month_number == 6:
    month = "June"
elif month_number == 7:
    month = "July"
elif month_number == 8:
    month = "August"
elif month_number == 9:
    month = "September"
elif month_number == 10:
    month = "October"
elif month_number == 11:
    month = "November"
elif month_number == 12:
    month = "December"

print(month)