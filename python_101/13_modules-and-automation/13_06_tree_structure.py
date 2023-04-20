# Write a script that walks through a nested folder structure
# and prints out all the Python files it can find.
# Run it in your labs folder and add formatting for nicer viewing.

# Könnte man eleganter lösen > So ist das ganze beschrännkt auf zwei Sub-Folder
import pathlib
path = pathlib.Path.cwd()
list_of_python_files = []
for element in path.iterdir():
    if element.suffix == ".py":
        list_of_python_files.append(element.name)
    if path.joinpath(element.name).is_dir() == True:
        new_path = path.joinpath(element.name)
        for sub_element in new_path.iterdir():
            if sub_element.suffix == ".py":
                list_of_python_files.append(sub_element.name)
            if new_path.joinpath(sub_element.name).is_dir():
                new_new_path = new_path.joinpath(sub_element.name)
                for sub_sub_element in new_new_path.iterdir():
                    if sub_sub_element.suffix == ".py":
                        list_of_python_files.append(sub_sub_element.name)


for element in list_of_python_files:
    print(f"{list_of_python_files.index(element):<5} {element:<30}")
