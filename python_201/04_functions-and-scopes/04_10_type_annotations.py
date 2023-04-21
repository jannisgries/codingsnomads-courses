# Add type annotations to the three functions shown below.

def multiply(num1, num2):
    return num1 * num2

def greet(greeting, name):
    sentence = f"{greeting}, {name}! How are you?"
    return sentence

def shopping_list(*args):
    [print(f"* {item}") for item in args]
    return args
