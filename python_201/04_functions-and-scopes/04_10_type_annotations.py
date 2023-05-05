# Add type annotations to the three functions shown below.

def multiply(num1:int, num2:int) -> int:
    return num1 * num2

def greet(greeting:str, name:str) -> str:
    sentence = f"{greeting}, {name}! How are you?"
    return sentence

def shopping_list(*args:str) -> list:
    [print(f"* {item}") for item in args]
    return args
