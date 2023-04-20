# You start this journey with a number `n`.
# You have to display a string representation of all numbers from 1 to n,
# but there are some constraints:
# - If the number is divisible by 3, write `Fizz` instead of the number
# - If the number is divisible by 5, write `Buzz` instead of the number
# - If the number is divisible by both 3 and 5, write `FizzBuzz` instead of the number
n = 100
for number in range(1, n):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz", end=" ")
    elif number % 3 == 0:
        print("Fizz", end=" ")
    elif number % 5 == 0:
        print("Buzz", end=" ")
    else:
        print(str(number), end=" ")
