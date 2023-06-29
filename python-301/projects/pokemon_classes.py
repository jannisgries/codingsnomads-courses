# Build a very basic Pokémon class that allows you to simulate battles
# in a Rock-Paper-Scissors game mechanic, as well as feed your Pokémon.
#
# The class should follow these specifications:
#
# - Each Pokemon should have a `name`, `primary_type`, `max_hp` and `hp`
# - Primary types should be limited to `water`, `fire` and `grass`
# - Implement a `battle()` method based on rock-paper-scissors that
#   decides who wins based only on the `primary_type`:
#       water > fire > grass > water
# - Display messages that explain who won or lost a battle
# - If a Pokemon loses a battle, they lose some of their `hp`
# - If you call the `feed()` method on a Pokemon, they regain some `hp`

horizontal_line = "________________________"

class Pokemon: 
    def __init__(self, name, primary_type, max_hp, hp) -> None:
        self.name = name
        possible_primary_types = ["water", "fire", "grass"]
        while primary_type not in possible_primary_types:
            print(f"The 'primary_type' of the pokemon {self.name} can only be 'water', 'fire' or 'grass.")
            primary_type = input(f"What is the primary type of the pokemon: ")
        self.primary_type = primary_type
        self.max_hp = max_hp
        self.hp = hp

    def __str__(self) -> str:
        return f"{self.name} ({self.primary_type}) | healthpoints: {self.hp}"

    def feed(self, food, amount):
        if food.amount >= amount:
            if self.hp + food.hp_increase * amount < self.max_hp:
                self.hp += food.hp_increase * amount
                food.amount -= amount
            else:
                print(f'Watch out, {self.name} can only have {self.max_hp} liefpoints. This meands {(self.hp + food.hp_increase * amount) - self.max_hp} healthpoints would be lost.')
                user_input = input('Type in "feed anyway", if you want to still proceed:')
                if user_input == "feed anyway":
                    self.hp += food.hp_increase * amount
                    food.amount -= amount
                else:
                    print("Ok, nothing has been fed.")
        else:
            print(f"You dont have enough {food.name} in your pocket")
    
    def battle_pokemon(self, other_pokemon):
        outcome = self.check_winner(self.primary_type, other_pokemon.primary_type)
        # Substract hp in case of loss
        if outcome == "win":
            other_pokemon.hp -= 10
            print(f"{self.name} won the battle \n{other_pokemon.name} got defeated and has only {other_pokemon.hp} healthpoints left.")
        elif outcome == "loose":
            self.hp -= 10
            print(f"{other_pokemon.name} won the battle \n{self.name} got defeated and has only {self.hp} healthpoints left.")
        else:
            print(f"{self.name} and {other_pokemon.name} fought each other, but no one was winnig – they tied and lost no healthpoints.")

    @staticmethod
    def check_winner(type1, type2):
        result = {0: "loose", 1: "win", -1: "tie"}
        game_map = {"water": 0, "fire": 1, "grass":2}
        win_loose_matrix = [
            [-1, 1, 0], # water
            [0, -1, 1], # fire
            [1, 0, -1]  # grass
        ]
        return result[win_loose_matrix[game_map[type1]][game_map[type2]]]  

class Food:
    def __init__(self, name, amount, hp_increase) -> None:
        self.name = name
        self.amount = amount
        self.hp_increase = hp_increase
    
    def add_food_item(self, amount):
        self.amount += amount

class User: 
    def __init__(self, pokemons: list, foods: list) -> None:
        self.pokenmons = pokemons
        self.foods = foods
  
