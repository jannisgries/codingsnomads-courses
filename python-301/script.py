# Define a class for a stove
class Stove:
    def __init__(self, num_burners):
        self.num_burners = num_burners
        self.on = False

    def turn_on(self):
        self.on = True
        print("Stove is now on")

    def turn_off(self):
        self.on = False
        print("Stove is now off")

# Define a class for a sink
class Sink:
    def __init__(self, num_faucets):
        self.num_faucets = num_faucets
        self.water_on = False

    def turn_water_on(self):
        self.water_on = True
        print("Water is now on")

    def turn_water_off(self):
        self.water_on = False
        print("Water is now off")

# Define a class for a fridge
class Fridge:
    def __init__(self, num_shelves, capacity):
        self.num_shelves = num_shelves
        self.capacity = capacity
        self.contents = []

    def add_food(self, food):
        self.contents.append(food)
        print(f"Added {food} to the fridge")

    def remove_food(self, food):
        self.contents.remove(food)
        print(f"Removed {food} from the fridge")

# Define a class for a countertop
class Countertop:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"Added {item} to the countertop")

    def remove_item(self, item):
        self.items.remove(item)
        print(f"Removed {item} from the countertop")

# Define a class for a kitchen using composition
class Kitchen:
    def __init__(self, stove, sink, fridge, countertop):
        self.stove = stove
        self.sink = sink
        self.fridge = fridge
        self.countertop = countertop

# Create instances of `Stove`, `Sink`, `Fridge`, and `Countertop`
stove = Stove(4)
sink = Sink(2)
fridge = Fridge(3, 200)
countertop = Countertop(10, 5)

# Create an instance of `Kitchen` using the smaller objects
kitchen = Kitchen(stove, sink, fridge, countertop)

# The `kitchen` object has access to the methods and attributes of the component objects
kitchen.stove.turn_on()  # "Stove is now on"
kitchen.fridge.add_food("Milk")  # "Added Milk to the fridge"
kitchen.countertop.add_item("Mixing bowl")  # "Added Mixing bowl to the countertop"