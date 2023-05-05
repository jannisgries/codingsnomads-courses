# Use the `csv` module to read in and count the different file types.
import csv
headers = []
with open("filecounts.csv", "r") as csvfile:
    str_headers = csvfile.readline()
    str_headers = str_headers.replace("\n", "")
    for el in str_headers.split(","):
        headers.append(el)
    reader = csv.DictReader(csvfile, fieldnames=headers)
    counts = list(reader)
#Delete the header from counts
print(counts)
