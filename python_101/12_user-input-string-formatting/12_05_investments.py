# Take in the following three values from the user:
# 1. investment amount
# 2. interest rate in percentage
# 3. number of years to invest
#
# Calculate the future values and print them to the console.

investment = int(input("Which amount of investment did you take?: "))
interest_rate = int(input("How high is the interest rate per year?: "))
years_of_investment = int(input("How many years do you plan to invest? "))

for year in range(0, years_of_investment):
    investment = investment * (100 + interest_rate) / 100
    print(f"Year: {year} Value of Investment: {investment}")

print(f"After {years_of_investment} of Investment, you will probably have {investment}.")