import pathlib

# Move and rename all .png files on your Desktop
path_to_desktop = pathlib.Path.home() /"Desktop"
new_dir = path_to_desktop /"screenshots"
# Create a new directory
if new_dir.is_dir() == False:
    new_dir.mkdir()
screenshot_counter = 0
for screenshot in new_dir.iterdir():
    if screenshot.suffix == ".png":
        screenshot_counter += 1
# Loop through all files on desktop
for file in path_to_desktop.iterdir():
    # Identify all screenshots on your Desktop
    path_to_file = path_to_desktop /file
    if file.suffix == ".png":
        # Move and rename all screenshots
        screenshot_counter += 1
        new_file_name = "screenshot" + f"({screenshot_counter})" + ".png"
        path_to_file.replace(new_dir/new_file_name)
            

