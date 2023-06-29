# Use your `Ingredients` class to create a URL to an online search
# that allows to look for recipes for dishes made from the
# available ingredients.
import webbrowser
import inquirer
from time import sleep
from copy import deepcopy
from pprint import pprint


horizontal_line = "______________________________________"

def wait_for_user():
    sleep(1)

class Ingredient:
    def __init__(self, name, wiki_name) -> None:
        self.name = name
        self.wiki_name = wiki_name
    def get_info(self):
        url = f"https://en.wikipedia.org/wiki/{self.wiki_name}"
        webbrowser.open_new(url)

class UserIngredient(Ingredient):
    def __init__(self, name, wiki_name, amount) -> None:
        super().__init__(name, wiki_name)
        self.amount = amount
        self.cutted = False
        self.peeled = False
        self.cooked = False
    def use_ingredient(self, used_ingredients: int):
        self.amount -= used_ingredients
    def add_ingredient(self, added_ingredient: int):
        self.amount += added_ingredient
    def cut(self):
        self.cutted = True
    def peel(self):
        self.peel = True
    def cook(self):
        self.peel = True

class InputIngredient(Ingredient):
    def __init__(self, name, wiki_name, needed_amount, needs_cutted:bool = False, needs_peeled: bool = False, needs_cooked: bool = False) -> None:
        super().__init__(name, wiki_name)
        self.needed_amount = needed_amount
        self.needs_cutted = needs_cutted
        self.needs_peeled = needs_peeled
        self.needs_cooked = needs_cooked
    def n_cutted(self, needs_cutted: bool):
        self.needs_cutted = needs_cutted
    def n_peeled(self, needs_peeled: bool):
        self.needs_peeled = needs_peeled
    def n_cooked(self, needs_cooked: bool):
        self.needs_cooked = needs_cooked

class CookingStep:
    def __init__(self, step_name, step_number, needed_ingredients, action) -> None:
        self.step_name = step_name
        self.step_number = step_number
        self.needed_ingredients = needed_ingredients
        self.action = action

    def __str__(self) -> str:
        return f"{self.step_name}"

class Dish:
    def __init__(self, name, steps:list, needed_ingredients: list) -> None:
        self.name = name
        self.steps = {}
        for step in steps:
            self.steps[step.step_name] = step
        self.needed_ingredients = needed_ingredients
    
    def __str__(self) -> str:
        return f"Dish: {self.name}"

    def cook(self, cooking_ingredients: dict):
        is_cooking = True
        meal_done = False
        for ingredient in self.needed_ingredients:
            if ingredient.name not in cooking_ingredients.keys():
                print(f"Sorry, but you are missing '{ingredient.name}'")
                is_cooking = False
            else:               
                if ingredient.needed_amount > cooking_ingredients[ingredient.name].amount:
                    print(f"Sorry, but you don´t have enough of {ingredient.name}, you need {ingredient.needed_amount} in total.")
                    is_cooking = False

                
        wait_for_user()
        print(horizontal_line)
        while is_cooking == True:
            questions = [
                    inquirer.List(
                        "step_to_choose",
                        message="What would you like to do?",
                        choices=[step for step in self.steps.keys()],
                    ),
            ]
            chosen_step = inquirer.prompt(questions)['step_to_choose']
            step = self.steps[chosen_step]
            print(f"Ok, you try to do: {step.step_name}")
            conditions_fulfilled = True
            for ing in step.needed_ingredients:
                # Check if ingredient is in the right condition for this step
                # needs_cutted
                if ing.needs_cutted == True and cooking_ingredients[ing.name].cutted == False:
                    print(f"The {ing.name} needs to be cutted first.")
                    conditions_fulfilled = False
                # needs_peeled
                elif ing.needs_peeled == True and cooking_ingredients[ing.name].peeled == False:
                    print(f"The {ing.name} needs to be peeled first.")
                    conditions_fulfilled = False
                # needs_cooked
                elif ing.needs_cooked == True and cooking_ingredients[ing.name].cooked == False:
                    print(f"The {ing.name} needs to be peeled first.")
                    conditions_fulfilled = False
            if conditions_fulfilled == True:
                if step.action == "cooked":
                    print(f"Nice, the {self.name} has been cooked")
                    meal_done = True
                    break
                else: 
                    exec(step.action)
            wait_for_user()
            print(horizontal_line)
        return meal_done
##################################################################
# Create Dish
##################################################################
dishes = {}
# Input Ingredients
carrots = InputIngredient("Carrot", "carrot", 5)
tomatoes = InputIngredient("Tomatoe", "tomatoe", 10)
print(carrots.needs_cutted)

# Steps
step_action = ('''for ing in step.needed_ingredients:
                    cooking_ingredients[ing.name].peeled = True
               ''')
step1 = CookingStep("peel the carrots", 1, [carrots], step_action)
########################
step_action = ('''for ing in step.needed_ingredients:
                    cooking_ingredients[ing.name].cutted = True
               ''')
peeled_carrots = InputIngredient("Carrot", "carrot", 5, needs_peeled=True)
step2 = CookingStep("cut the vegetables", 2, [peeled_carrots, tomatoes], step_action)
########################
step_action = "cooked"
cutted_carrots = InputIngredient("Carrot", "carrot", 5, needs_cutted=True)
cutted_tomatoes = InputIngredient("Carrot", "carrot", 5, needs_cutted=True)
step3 = CookingStep("cook the vegetables", 3, [cutted_carrots, cutted_tomatoes], step_action)
# Add Dish
cartomsoup = Dish("Carrot-Tomatoe-Soup",[step1, step2, step3], [carrots, tomatoes])
dishes[str(cartomsoup)] = cartomsoup

print(carrots.needs_cutted)
################################################################
# Cook Dish
##################################################################
# Choose Dish
questions = [
        inquirer.List(
            "dishes_to_choose",
            message="Which dish would you like to cook?",
            choices=dishes,
        ),
    ]
dish_to_cook = dishes[inquirer.prompt(questions)['dishes_to_choose']]

done_meal = False
while done_meal == False:
    # Choose items of fridge
    print(f"Ok, lets cook a {dish_to_cook.name}. First, lets collect all items we need.")
    user_item = ""
    user_items = {}
    i = 0
    while user_item != "Ok, close fridge":
        questions = [
            inquirer.List(
                "ingredients_to_choose",
                message="Which item would you like to choose?",
                choices=['Kale', 'Carrot','Cabbage', 'Celery', 'Asparagus', 'Lettuce', "Tomatoe", "Ok, close fridge"],
            ),
        ]
        user_item = inquirer.prompt(questions)['ingredients_to_choose']
        if user_item != "Ok, close fridge":
            number_of_item = int(input(f'How many {user_item} do you want to grab?: '))
            item = UserIngredient(user_item, user_item.lower(),number_of_item)
            user_items[item.name] = item
            i += 1

    # Start Cooking
    done_meal = dish_to_cook.cook(user_items)
