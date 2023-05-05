# Adapt your file counter script so that it records more different file types
# in your CSV file. Remember that the format of your output needs to be
# consistent across multiple runs of your script. This means you'll need to
# make a compromise and choose which file types you want to record beforehand.

import pathlib
import csv
# Counting functionality 
path_to_desktop = pathlib.Path.home() / "Desktop"
files_on_desktop = {}
# Loop through all files on desktop
for file in path_to_desktop.iterdir():
    # Identify all screenshots on your Desktop
    if file.is_file() == True and file.suffix:
        if file.suffix not in files_on_desktop.keys():
            files_on_desktop.update({file.suffix: 1})
        elif file.suffix in files_on_desktop.keys():
            files_on_desktop[file.suffix] += 1

# Write the file counts to a `.csv` file.
# Create headers
count = files_on_desktop
headers = []
data = []

#Write to file
path_to_counting_file = pathlib.Path.home().joinpath("Documents/codingnomads/courses/python_201/03_file-input-output/file-counter/filecounts.csv")
if path_to_counting_file.exists() == False:
    for key in count.keys():
        headers.append(key)
        data.append(count[key])
    with open(path_to_counting_file, "w") as csvfile:
            countwriter = csv.writer(csvfile)
            countwriter.writerow(headers)
            countwriter.writerow(data)
else:
    new_headers = False
    with open(path_to_counting_file, "r") as csvfile:
        existing_headers = []
        str_headers = csvfile.readline()
        str_headers = str_headers.replace("\n", "")
        for el in str_headers.split(","):
            existing_headers.append(el)
        existing_file = csvfile.readlines()        
    for file_extension in existing_headers:
        headers.append(file_extension)
        if file_extension in count.keys():
            data.append(count[file_extension])
        else:
            data.append(0)
    for key in count.keys():
        if key not in existing_headers:
            headers.append(key)
            data.append(count[key])
            new_headers = True
    if new_headers == True:
        with open(path_to_counting_file, "w") as csvfile:
            countwriter = csv.writer(csvfile)
            countwriter.writerow(headers)
            for count_entry in existing_file:
                count_list = []
                for char in count_entry:
                    if char.isnumeric() == True:
                        count_list.append(char)
                countwriter.writerow(count_list)
            countwriter.writerow(data)
    else: 
        with open(path_to_counting_file, "a") as csvfile:
            countwriter = csv.writer(csvfile)
            countwriter.writerow(data)
