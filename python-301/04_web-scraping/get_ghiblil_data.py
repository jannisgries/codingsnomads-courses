import requests
from pathlib import Path
import json

path_to_file = Path.home().joinpath('Documents/codingnomads/courses/python-301').joinpath('films.json')

response = requests.get("https://ghibliapi-iansedano.vercel.app/api/films")
resp_json = response.json()['data']['films']

with open(path_to_file, "w") as file:
    json.dump(resp_json, file)
