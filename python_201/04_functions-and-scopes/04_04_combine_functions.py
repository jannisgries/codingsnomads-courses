# Combine the `greet()` function that you developed in the course materials
# with the `write_letter()` function from the previous exercise.
# Write both functions in this script and call `greet()` within `write_letter()`
# to let `greet()` take care of creating the greeting string.


def greet(greeting: str, name:str) -> str:
    sentence = f"{greeting}, {name}! How are you?"
    return sentence

def write_letter( name : str, text: str) -> str:
    greeting = greet( "Hello", name)
    letter = f"""
    {greeting}\n\n
    {text}\n\n
    Have a nice day, {name}\n\n
    """
    return letter
input_name = input("Who do you want to greet?: ")
input_text = input("What do you want to tell this person?:  ")
print(write_letter(input_name, input_text))