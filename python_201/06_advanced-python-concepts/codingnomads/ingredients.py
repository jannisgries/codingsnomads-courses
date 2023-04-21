# ingredients.py
def prepare(ingredient):
    print(f"You cooked the {ingredient}.")
    return f"cooked {ingredient}"

carrot = "carrot"
salt = "salt"
potato = "potato"


if __name__ == "__main__":
    print(prepare(potato))
