# Problem 1: New Horizons
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - What values should the villager object be intialized with?
# - what var name should store the village instance?

### P - Plan
# 2. Write out in plain English what you want to do:
# - Create a Villager object with the giv en name, species, and catchphrase
# - store it in var villager

# 3. Translate each sub-problem into pseudocode:
# - create a Village object using the provided values
# - assign the object to the var apollo

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []

apollo = Villager("Apollo", "Eagle", "pah")

# Problem 2: Greet Player
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - what method should be added to the villager class?
# - what values should the new Villager object have?

### P - Plan
# 2. Write out in plain English what you want to do:
# - add the greet_player() method, create the Bones villager, and call the method with my name

# 3. Translate each sub-problem into pseudocode:
# - add great_player() to the Villager class
# - create bones - Vilalger("Bones", "Dog", "yip yip")
# - print bones.greet_player("Prisha")

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def greet_player(self, player_name):
    return f"{self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}!"

bones = Villager("Bones", "Dog", "yip yip")
print(bones.greet_player("Prisha"))

# Problem 3: Update Catchphrase
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - which villager object's catachphrase should be updated?
# - whcat should the new catchphrase be?

### P - Plan
# 2. Write out in plain English what you want to do:
# - change Bone's catachphrase to the new value and call greet_player() to verify the update

# 3. Translate each sub-problem into pseudocode:
# - update bones.catchphrase to "ruff it up"
# - print bones.greet_player("Samia")

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
bones.catchphrase = "ruff it up"
print(bones.greet_players("Samia"))

# Problem 4: Set Character
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - what makes a catchphrase vlaid?
# - what should happen if the catchphrase is invlaid?

### P - Plan
# 2. Write out in plain English what you want to do:
# - create a setter method that checks if the new catchphrase is valid before updating it

# 3. Translate each sub-problem into pseudocode:
# - check if the catchphrase is less than 20 chars
# - check if every char is a letter or a space
# - if valid, update catchphrase and print "Catchphrase updated"
# - else, print "Invlaid Catchphrase"

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def set_catchphrase(self, new_catchphrase):
    if len(new_catchphrase) < 20 and all(char.isalpha() or char.isspace() for char in new_catchphrase):
        self.catchphrase = new_catchphrase
        print("Catchphrase Updated!")
    else:
        print("Invalid catchphrase")


# Problem 5: Add Furniture
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - which furniture items are considered valid?
# - what should happen if an invlaid item is passed in?

### P - Plan
# 2. Write out in plain English what you want to do:
# - create a method that checks if an items is valid and, if so, adds it to the villager's furniture list

# 3. Translate each sub-problem into pseudocode:
# - create a lsit of valid furniture items
# - check if item_name is in the list
# - if it is, append it to self.furniture

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def add_item(self, item_name):
    valid_items = [
        "acoustic guitar",
        "ironwood kitchenette",
        "rattan armchair",
        "kotatsu",
        "cacao tree"
    ]

    if item_name in valid_items:
        self.furniture.append(item_name)