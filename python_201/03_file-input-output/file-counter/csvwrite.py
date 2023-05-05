# Refactor your file counter script to use `pathlib` also for
# reading and writing to your CSV file. Make sure to handle the
# path in a way so that you can run the script from anywhere.
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
count = files_on_desktop
headers = []
data = []
for key in count.keys():
    headers.append(key)
    data.append(count[key])

try:
    with open("filecounts.csv", "a") as csvfile:
        countwriter = csv.writer(csvfile)
        countwriter.writerow(data)
except:
    with open("filecounts.csv", "w") as csvfile:
        countwriter = csv.writer(csvfile)
        countwriter.writerow(headers)
        countwriter.writerow(data)
