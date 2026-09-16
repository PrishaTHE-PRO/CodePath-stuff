# Problem 1: Mutual Friends
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - what should the method return?
# - how can I determine if two villagers share the same friend?

### P - Plan
# 2. Write out in plain English what you want to do:
# - compare the friends lists of both villagers 
# - return common friends

# 3. Translate each sub-problem into pseudocode:
# - create an empty list for mutual friends
# - loop through the current villager's friends
# - if a friend is also in new_contact.friends, add their name to the list

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.friends = []

    def get_mutuals(self, new_contact):
        mutuals = []

        for friend in self.friends:
            if friend in new_contact.friends:
                mutuals.append(friend.name)
        
        return mutuals

# Problem 2: Linked Up
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - in what order should the nodes be connected?
# - which node is the head of the linked list?

### P - Plan
# 2. Write out in plain English what you want to do:
# - connect each node by setting its next pointer to the following node

# 3. Translate each sub-problem into pseudocode:
# - set kk_slider.next to harriet
# - set harriet.next to saharah
# - set saharah.next to isabelle

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

# Problem 3: Daily Tasks
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - where should the new task be added in the linked list?
# - what should the function return after adding the new task?

### P - Plan
# 2. Write out in plain English what you want to do:
# - create a new node containing the task, point it to the current head, and retur nit as the new head

# 3. Translate each sub-problem into pseudocode:
# - create a new node with the given task
# - set its next pointer to the current head
# - return the new node

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def add_first(head, task):
    new_head - Node(task)
    new_head.next = head
    return new_head

# Problem 4: Halve List
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - should every node's value be divided by 2?
# - should the function modify the existing lsit or create a new one?

### P - Plan
# 2. Write out in plain English what you want to do:
# - traverse the linked lsit, divide each node's value by 2 and return the original head

# 3. Translate each sub-problem into pseudocode:
# - start ad the head
# - while the current node:
    # - divide by 2
    # - move to the next node
# - return the head

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def half_list(head):
    current = head

    while current:
        current.value /= 2
        current = current.next

    return head

# Problem 5: Remove Last
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - what should happen if the list has only one node?
# - should the function modify the existing list or create a new one?

### P - Plan
# 2. Write out in plain English what you want to do:
# - traverse to the second-to-last node
# - remove the last node by setting its pointer to None
# - reutrn the head

# 3. Translate each sub-problem into pseudocode:
# - if the list is empty or has one node, return None
# - traverse until the next node is the tail
# - set the current node's pointer to None
# - return the head

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def delete_tail(head):
    if head is None or head.next is None:
        return None
    
    current = head
    while current.next.next:
        current = current.next

    current.next = None
    return head
