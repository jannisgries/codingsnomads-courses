# Import pathlib
import pathlib

# Find the path to my Desktop
desktop_path = pathlib.Path.home().cwd()
print(desktop_path)
# Create a new folder
new_path = desktop_path /"screenshots"
new_path.mkdir(exist_ok=True)

for filepath in desktop_path.iterdir():
  # Filter for screenshots only
  if filepath.suffix == '.png':  # Filter for screenshots only
    # Move the screenshots in new filepath with old name there
    new_filepath = new_path.joinpath(filepath.name) # = new_path /filepath.name
    filepath.replace(new_filepath)
