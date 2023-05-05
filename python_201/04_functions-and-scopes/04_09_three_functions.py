# Write a program with three functions. Each function must call
# at least one other function and use the return value
# of that function to do something with it. You can have more
# than three functions, and they don't need to call each other
# in a circular way.

def calculate_average(numbers: list):
    number_of_numbers = calculate_length(numbers)
    sum_of_numbers = calculate_sum(numbers)
    average = sum_of_numbers / number_of_numbers
    return average

def calculate_length(numbers: list):
    return len(numbers)

def calculate_sum(numbers : list):
    sum = 0
    for num in numbers: 
        sum += num
    return sum

def collect_numbers():
    print("\n\nWelcome to the average caluclator. Please type in the numbers, you want do calculate the average of. When you are done, enter 'calculate' to start the calculation", end="\n\n")
    print("Start with your first number", end="\n\n")
    numbers = []
    while True:
        user_input = input("Please type in any number or 'calculate': ")
        if user_input.isnumeric() == True:
            number = int(user_input)
            numbers.append(number)
        elif user_input == "calculate":
            break
    average = calculate_average(numbers)
    print("\n\nThe average is:" + str(average) + "\n\n")
collect_numbers()