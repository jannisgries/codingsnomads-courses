import pathlib

# Part I 
## Write a script that searches a folder you specify (as well as its subfolders, up
## to two levels deep) and compiles a list of all `.jpg` files contained in there.
## The list should include the complete path of each `.jpg` file.
path = pathlib.Path.cwd()
list_of_python_files = []
for element in path.iterdir():
    if element.suffix == ".jpg":
        list_of_python_files.append(element.name)
    if path.joinpath(element.name).is_dir() == True:
        new_path = path.joinpath(element.name)
        for sub_element in new_path.iterdir():
            if sub_element.suffix == ".jpg":
                list_of_python_files.append(sub_element.name)
            if new_path.joinpath(sub_element.name).is_dir():
                new_new_path = new_path.joinpath(sub_element.name)
                for sub_sub_element in new_new_path.iterdir():
                    if sub_sub_element.suffix == ".jpg":
                        list_of_python_files.append(sub_sub_element.name)
for element in list_of_python_files:
    print(f"{list_of_python_files.index(element):<5} {element:<30}")

# Part II
## If you are feeling bold, create a list containing each type of file extension
## you find in the folder.
## Start with a small folder to make it easy to check whether your program is
## working correctly. Then search a bigger folder.
## This program should work for any specified folder on your computer.

path = pathlib.Path.cwd()
list_of_file_extensions = []
for element in path.iterdir():
    if element.suffix != "" and element.suffix not in list_of_file_extensions:
        list_of_file_extensions.append(element.suffix)
    if path.joinpath(element.name).is_dir() == True:
        new_path = path.joinpath(element.name)
        for sub_element in new_path.iterdir():
            if sub_element.suffix != "" and sub_element.suffix not in list_of_file_extensions:
                list_of_file_extensions.append(sub_element.suffix)
            if new_path.joinpath(sub_element.name).is_dir():
                new_new_path = new_path.joinpath(sub_element.name)
                for sub_sub_element in new_new_path.iterdir():
                    if sub_sub_element.suffix != "" and sub_sub_element.suffix not in list_of_file_extensions:
                        list_of_file_extensions.append(sub_sub_element.suffix)

for element in list_of_file_extensions:
    print(f"{list_of_file_extensions.index(element):<5} {element:<30}")



