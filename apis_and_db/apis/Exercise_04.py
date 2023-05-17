'''
Write a program that makes a PUT request to update your user information to a new first_name, last_name and email.

Again make a GET request to confirm that your information has been updated.

'''

import requests
from pprint import pprint

# Manually add user-id
userId = 641
api_url = 'http://demo.codingnomads.co:8080/tasks_api/users'
url_with_userid = api_url + f'/{userId}'
body = {
    "email": "test@test.com",
    "first_name": "tim",
    "last_name": "test",
}
response = requests.put(url_with_userid, json=body)
print(f"{response.status_code}")

# Verify updates w/ get request
response = requests.get(url_with_userid)
data = response.json()
pprint(data)