# Define a function called `write_letter()` that takes as input a `name`
# and a `text` argument. In the body of the function, create a greeting
# message with the `name` input, as well as a goodbye message that uses
# the `name` again. Combine that with the input `text` to return a
# complete `letter`.

def write_letter( name : str, text: str) -> str:
    letter = f"""
    Hello, {name}!\n\n
    {text}\n\n
    Have a nice day, {name}\n\n
    """
    return letter
input_name = input("Who do you want to greet?: ")
input_text = input("What do you want to tell this person?:  ")
print(write_letter(input_name, input_text))
