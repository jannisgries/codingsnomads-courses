# Move and rename all .png files on your Desktop

# Identify all screenshots on your Desktop

# Create a new directory

# Move and rename all screenshots

import pathlib

path_to_file = pathlib.Path.cwd() /"README.md"
path_to_file.rename(pathlib.Path.cwd() /"Readme.md")
