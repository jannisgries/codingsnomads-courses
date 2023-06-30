# Use the Pokemon API at https://pokeapi.co/ to assemble a team of your
# six favorite Pokémon.
# Your task is to fetch information about six Pokémon through the
# necessary API calls and include the information in your local script.
# This information should include at least:
# - name
# - number
# - types
#
# You can improve on your project even more by writing the data to a small
# `.html` page which allows you to also display the sprites of each Pokémon.
# Check out the guides they provide: https://pokeapi-how.appspot.com/page5
from pathlib import Path
import readline
import requests
import json
import webbrowser


BASE_URL = "https://pokeapi.co/api/v2/"
horizontal_line = "\n______________________________\n"

######################################################################################
# Class Definitions
######################################################################################
class TypeCompleter(object):  # Custom completer
    def __init__(self, options):
        self.options = sorted(options)
    def complete(self, text, state):
        if state == 0:  # on first trigger, build possible matches
            if text:  # cache matches (entries that start with entered text)
                self.matches = [s for s in self.options if s and s.startswith(text)]
            else:  # no text entered, all matches possible
                self.matches = self.options[:]
        # return match indexed by state
        try: 
            return self.matches[state]
        except IndexError:
            return None

class Pokemon():
    def __init__(self, name) -> None:
        self.name = name
        pokemon_api_url = BASE_URL + f"pokemon/{self.name}"
        self.json_information = requests.get(pokemon_api_url).json()
        self.types = [] 
        for el in self.json_information['types']:
            self.types.append(el['type']['name'])
        self.id = self.json_information['id']
        self.sprite_link = self.json_information['sprites']['front_default']
    
    def __str__(self) -> str:
        return f"{self.name}, types: {self.types}"

######################################################################################
# Functions
######################################################################################

def get_all_pokemon_names(wants_update:bool = False):
    path_to_storage_file = Path.home().joinpath('Documents/codingnomads/courses/python-301/04_web-scraping/pokemon.json')
    if wants_update == True:
        url = BASE_URL + "pokemon?limit=15000"
        results = requests.get(url).json()['results']
        with open(path_to_storage_file, "w") as file:
            json.dump(results, file)
    else: 
        with open(path_to_storage_file, "r") as file:
            results = json.load(file)
    pokemon_names = []
    for el in results:
        pokemon_names.append(el['name'])
    return pokemon_names

def pick_pokemon_team(update_pokemon_list: bool = False):
    pokemon_list = get_all_pokemon_names(update_pokemon_list)
    completer = TypeCompleter(pokemon_list)
    readline.set_completer(completer.complete)
    readline.parse_and_bind('bind ^I rl_complete')
    chosen_pokemon = []
    while len(chosen_pokemon) < 8:
        print(f"Which pokemon would you like to choose? Press <tab> to show pokemons based on your current input.")
        user_input = input("Type in a pokemon: ")
        if user_input in pokemon_list:
            chosen_pokemon.append(user_input)
            print(f"You have chosen {user_input} for your team ({len(chosen_pokemon)} / 8)")
            print(horizontal_line)
        else:
            print("I am afraid, this pokemon doesn´t exist. Try again (you may use the autocomplete function)")
            print(horizontal_line)
    return chosen_pokemon

def create_html_page(user_pokemon: dict):
    path_to_html_file = Path.home().joinpath('Documents/codingnomads/courses/python-301/04_web-scraping/pokemon.html')
    i = 0
    html = """<h1 style='text-align: center'>Your Pokemon Team</h1><div style='display:flex; flex-direction:row; align-items:center; justify-content:center'>"""
    for pokemon in user_pokemon.values():
        if i == 4:
            html +=  """</div>
                        <div style='display:flex; flex-direction:row; align-items:center; justify-content:center'>
                    """

        html += f"""
                    <div style='width: 25%; text-align: center;'>
                    <img src={pokemon.sprite_link}>
                    <p>{pokemon.name}</p>
                    <p>types: {' | '.join(pokemon.types)}</p>

                </div>
        """
        i += 1
    html += "</div>"
    path_to_html_file.write_text(html)
    return path_to_html_file

######################################################################################
# Logic
######################################################################################
chosen_pokemon = pick_pokemon_team()
user_pokemon = {}
for pokemon in chosen_pokemon:
    user_pokemon[pokemon] = Pokemon(pokemon)
    print(user_pokemon[pokemon])
html_file_path = create_html_page(user_pokemon)
webbrowser.open(f"file://{str(html_file_path)}")
