# Problem 8: Telephone

### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - Should the function return True if the start villager and the target villager are the same person?
# - Can the chain of neighbors ever loop back to a villager we already visited?

### P - Plan
# 2. Write out in plain English what you want to do:
# Start at the start villager and keep moving to the next neighbor until we either reach the target villager or run out of neighbors.

# 3. Translate each sub-problem into pseudocode:
# Set the current villager to the start villager
# While the current villager is not None
# If the current villager is the target, return True
# Move to the current villager's neighbor
# Return False

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class Villager:
    def __init__(self, name, species, personality, catchphrase, neighbor=None):
        self.name = name
        self.species = species
        self.personality = personality
        self.catchphrase = catchphrase
        self.furniture = []
        self.neighbor = neighbor

def message_received(start_villager, target_villager):
    current = start_villager

    while current is not None:
        if current is target_villager:
            return True

        current = current.neighbor

    return False

# Time: O(n) where n is the number of villagers in the chain, since we visit each neighbor at most once.
# Space: O(1) because we only keep track of the current villager.

#I picked this problem because it helped me practice following a chain of references, which is like traversing a linked list.

# Problem 9: Nook's Cranny

### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - Should the last node's next pointer stay as None since there is nothing after Tommy?
# - Should the nodes be linked when they are created, or after by setting the next attribute?

### P - Plan
# 2. Write out in plain English what you want to do:
# Create a node for Tom Nook and a node for Tommy, then set Tom Nook's next pointer to the Tommy node so they are linked in order.

# 3. Translate each sub-problem into pseudocode:
# Create a Node with the value "Tom Nook"
# Create a Node with the value "Tommy"
# Set the Tom Nook node's next to the Tommy node

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

tom_nook = Node("Tom Nook")
tommy = Node("Tommy")
tom_nook.next = tommy

# Time: O(1) because we create a fixed number of nodes and set one pointer.
# Space: O(1) because we only store two nodes.

#I picked this problem because it helped me understand how nodes in a linked list point to each other.

# Problem 10: Timmy and Tommy

### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - Should I reuse the tom_nook and tommy nodes from Problem 9, or create new ones?
# - Does the order I set the pointers matter so that I do not lose the link to tommy?

### P - Plan
# 2. Write out in plain English what you want to do:
# Create a new node for Timmy, point it at Tommy, then redirect Tom Nook's next pointer to Timmy so Timmy sits in the middle.

# 3. Translate each sub-problem into pseudocode:
# Create a Node with the value "Timmy"
# Set the Timmy node's next to the Tommy node
# Set the Tom Nook node's next to the Timmy node

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
timmy = Node("Timmy")
timmy.next = tommy
tom_nook.next = timmy

# Time: O(1) because we create one node and change two pointers.
# Space: O(1) because we only add one new node.

#I picked this problem because it helped me practice inserting a node in the middle of a linked list by redirecting pointers.
