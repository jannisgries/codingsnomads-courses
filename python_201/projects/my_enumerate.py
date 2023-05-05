# Reproduce the functionality of Python's built-in `enumerate()` function.
# Define a function called `my_enumerate()` that takes an iterable as input
# and gives back both the element as well as its index position as an integer.

def my_enumerate_fun(iterable, number: float = 0) -> list:  # add your arguments
      list = []
      for el in iterable:
            list.append((number, el))
            number += 1
      return list

def my_enumerate_gen(iterable, number: float = 0) -> list:  # add your arguments
      for el in iterable:
          yield(number, el)
          number += 1
           


courses = ['Intro', 'Intermediate', 'Advanced', 'Professional']
for index, course in my_enumerate_gen(courses):
    print(f"{index}: {course} Python")

# OUTPUT:
# 0: Intro Python
# 1: Intermediate Python
# 2: Advanced Python
# 3: Professional Python