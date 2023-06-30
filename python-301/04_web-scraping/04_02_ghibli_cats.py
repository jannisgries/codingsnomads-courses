# Read through the documentation of the Ghibli API and reproduce the example
# listed at https://ghibliapi.herokuapp.com/#section/Use-Case in Python.
# Try skim the Haskell code example and see if you can understand anything.
# Don't worry if you don't, it's a completely different language :)
#
# Your task is to use the API to find information about all the cats that
# appear in Studio Ghibli films.

import requests
from pprint import pprint
api_url = 'https://ghibliapi-iansedano.vercel.app/api/species'
resp = requests.get(api_url).json()['data']['species']
people = []
for species in resp:
    if species['name'] == "Cat":
        people = species['people']
pprint(people)