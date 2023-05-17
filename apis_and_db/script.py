import requests
from pprint import pprint

base_url = "http://demo.codingnomads.co:8080/tasks_api/users"
response = requests.get(base_url)

data = response.json()
pprint(data['data'][0]['first_name'])

#what happens if you print data['data'][0]['first_name']
#why is this?
