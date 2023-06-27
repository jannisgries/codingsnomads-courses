# Add an API call to your CLI game that assigns a name to your player.
# Collect the name from your player
# Check whether it meets the length requirements for the API call
# Ping the Uzby API to create a new random name for your player,
#   using the length of their given name as input
# Inform the player about their in-game name

import requests
import geocoder
import json
from datetime import datetime, timedelta
from pathlib import Path
from pprint import pprint

horizontal_line = "____________________________"

#############################################
# Get User name
#############################################
def checkConditions(name: str):
    if len(name) < 2:
        print("I am sorry, i can only use names which have at least 2 characters.")
        user_name_input = input("Please try again: ")
        name = checkConditions(user_name_input)
    elif len(name) > 40:
        print("I am sorry, i can only use names which have no more than 40 characters.")
        user_name_input = input("Please try again: ")
        name = checkConditions(user_name_input)
    return name

def generateUrl(name: str):
    min_len = len(name)
    max_len = len(name)
    nameapi_url = f'https://uzby.com/api.php?min={min_len}&max={max_len}'
    return nameapi_url

def get_ingame_name() -> str:
    user_name_input = input("What is your real name?: ")
    user_real_name = checkConditions(user_name_input)
    nameapi_url = generateUrl(user_real_name)
    response = requests.get(nameapi_url)
    return response.text

#############################################
# Get User weather on current location
#############################################
filepath = Path.home().joinpath('Documents/codingnomads/courses/python_201/projects/assets/wmo_codes.json')
f = open(filepath)
wmo_codes = json.load(f)


def get_location() -> list:
    """Get Location of user

    Returns:
        list: list which contains lat and lon
    """
    g = geocoder.ip('me')
    return g.latlng

def hour_rounder(t):
    # Rounds to nearest hour by adding a timedelta hour if minute >= 30
    t = (t.replace(second=0, microsecond=0, minute=0, hour=t.hour)
               +timedelta(hours=t.minute//30))
    t = str(t)[:-3]
    t = t.replace(" ", "T")
    return t

def get_weather() -> dict:
    """Get weather at user´s location

    Returns:
        dict: weather information
    """
    location = get_location() # return list with lat and lng in list as floats
    lat = location[0]
    lon = location[1]
    weather_api_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=temperature_2m,weathercode,is_day&forecast_days=1"
    response = requests.get(weather_api_url)
    result = response.json()
    relevant_time = hour_rounder(datetime.now())
    relevant_index = result['hourly']['time'].index(relevant_time)
    is_day = result['hourly']['is_day'][relevant_index]
    weathercode = result['hourly']['weathercode'][relevant_index]
    weather = wmo_codes[f'{weathercode}'][f'{is_day}']
    return weather 

#############################################
# Script Functionality
#############################################
ingame_name = get_ingame_name()
print(horizontal_line)
print(f"Welcome to your new game!")
print(f"For the purpose of this game, you shall now be called {ingame_name}")
weather = get_weather()
print(f"Also, keep in mind, the current weather: {weather['description']}")



