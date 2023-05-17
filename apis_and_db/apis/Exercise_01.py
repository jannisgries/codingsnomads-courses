'''
Using the requests package, make a GET request to the api behind this endpoint:

    http://demo.codingnomads.co:8080/tasks_api/users

Print out:

    - the status code
    - the encoding of the response
    - the text of the response body



'''
import requests
from pprint import pprint
request_url = 'http://demo.codingnomads.co:8080/tasks_api/users'
response = requests.get(request_url)
data = response.json()
print(response.status_code, response.encoding)
pprint(data)