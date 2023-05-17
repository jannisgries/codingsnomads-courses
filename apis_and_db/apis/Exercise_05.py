'''
Write a program that makes a DELETE request to remove the user your create in a previous example.

Again, make a GET request to confirm that information has been deleted.

'''

import requests
from pprint import pprint

# Manually add user-id
userId = 644
api_url = 'http://demo.codingnomads.co:8080/tasks_api/users'
url_with_userid = api_url + f'/{userId}'
response = requests.delete(url_with_userid)
print(f"{response.status_code}")

# Verify updates w/ get request
response = requests.get(url_with_userid)
if response.json()['data'] == None:
    print('User was deleted sucessfullly')