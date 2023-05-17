'''
Write the necessary code to make a POST request to:

    http://demo.codingnomads.co:8080/tasks_api/users

and create a user with your information.

Make a GET request to confirm that your user information has been saved.

'''

import requests
from pprint import pprint
api_url = 'http://demo.codingnomads.co:8080/tasks_api/users'
body = {
    "email": "mrtest@test.com",
    "first_name": "Tim",
    "last_name": "Test",
}
response = requests.post(api_url, json=body)
user_id = response.json()['data']['id']
print(f"{response.status_code}")

# Verify updates w/ get request
url_with_userid = api_url + f'/{user_id}'
response = requests.get(url_with_userid)
data = response.json()
pprint(data)
