'''
Use the countries API https://restcountries.com/ to fetch information
on your home country and the country you're currently in.

In your python program, parse and compare the data of the two responses:
* Which country has the larger population?
* How much does the area of the two countries differ?

'''
import requests
horitontal_line = "____________________________"
api_url = "https://restcountries.com/v3.1/name/"
country1 = input("Which is the first country, you want to compare? ")
country2 = input("Which is the second country, you want to compare? ")
response_country1 = requests.get(api_url + f"{country1}").json()[0]
response_country2 = requests.get(api_url + f"{country2}").json()[0]
print(horitontal_line)

# Which country has the larger population?
if response_country1['population'] > response_country2['population']:
    print(f"{response_country1['name']['common']} has the bigger population with {response_country1['population']} inhabitants.")
elif response_country2['population'] > response_country1['population']:
    print(f"{response_country2['name']['common']} has the bigger population with {response_country2['population']} inhabitants.")
else: 
    print(f"They both have the same population with {response_country1['population']} inhabitants.")
print(horitontal_line)

# How much does the area of the two countries differ?
if response_country1['area'] > response_country2['area']:
    print(f"The area of {response_country1['name']['common']} is {response_country1['area'] -  response_country2['area']} m2 bigger than the area of {response_country2['name']['common']}")
elif response_country2['area'] > response_country1['area']:
    print(f"The area of {response_country2['name']['common']} is {response_country2['area'] -  response_country1['area']} m2 bigger than the area of {response_country1['name']['common']}")
print(horitontal_line)

# Print the native name of both countries, as well as their capitals
native_name_dict_c1 = response_country1['name']['nativeName']
official_name_c1 = native_name_dict_c1[next(iter(native_name_dict_c1))]['official']
print(f"{official_name_c1} has the capital: {response_country1['capital'][0]}")
native_name_dict_c2 = response_country2['name']['nativeName']
official_name_c2 = native_name_dict_c2[next(iter(native_name_dict_c2))]['official']
print(f"{official_name_c2} has the capital: {response_country2['capital'][0]}")
