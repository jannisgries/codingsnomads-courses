# Write a function named `stats()` that takes in a list of numbers
# and finds the maximum, minimum, average and sum of the numbers.
# Print these values to the console you call the function.

example_list = [1, 2, 3, 4, 5, 6, 7]
def stats(numbers: list):
  # define the function here 
  numbers.sort()
  lowest_number = numbers[0]
  highest_number = numbers[-1]
  sum = 0
  for num in numbers:
    sum += num
  average = sum / len(numbers)
  print(f"""
  Highest number: {highest_number}
  Lowest number : {lowest_number}
  Average: {average}
  Sum: {sum}
  """)

stats(example_list)