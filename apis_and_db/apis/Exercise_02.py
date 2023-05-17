'''
Building on the previous example, create a list of all of the emails of the users and print
the list to the console.

'''
import requests
from pprint import pprint
request_url = 'http://demo.codingnomads.co:8080/tasks_api/users'
response = requests.get(request_url)
data = response.json()
user_emails = []
for user in data['data']:
    user_emails.append(user['email'])
pprint(user_emails)