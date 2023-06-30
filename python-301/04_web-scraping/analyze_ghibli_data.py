from pathlib import Path
from pprint import pprint
import json

path_to_file = Path.home().joinpath('Documents/codingnomads/courses/python-301').joinpath('films.json')

with open(path_to_file, "r") as file:
    resp_json = json.load(file)

i = 0
maxrt_el = []
maxrt = 0
for el in resp_json:
    rt = int(el['running_time'])
    if  rt > maxrt:
        maxrt = rt
        maxrt_el = [el]
    elif rt == maxrt:
        maxrt_el.append(el)
    i += 1
pprint("These are the longest films")
pprint(maxrt_el)