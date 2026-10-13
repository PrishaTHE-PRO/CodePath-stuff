# Problem 7: Remove From Inventory

### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - What should we return if the item to remove is the head of the list?
# - What should we return if the list is empty?

### P - Plan
# 2. Write out in plain English what you want to do:
# Check if the head holds the item first, and if so return the next node as the new head. Otherwise walk through the list and when the next node holds the item, skip over it by pointing to the node after it.

# 3. Translate each sub-problem into pseudocode:
# If the head is None, return None
# If the head's value is the item, return the head's next
# Set current to the head
# While current has a next node
# If the next node's value is the item
# Point current's next to the node after the next node
# Return the head
# Move current to the next node
# Return the head

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def delete_item(head, item):
    if head is None:
        return None

    if head.value == item:
        return head.next

    current = head

    while current.next:
        if current.next.value == item:
            current.next = current.next.next
            return head

        current = current.next

    return head

# Time: O(n) where n is the number of nodes, since we may have to look at every node to find the item.
# Space: O(1) because we only keep track of the current node.

#I picked this problem because it helped me practice removing a node from a linked list by changing the pointer around it.

# Problem 8: Move Tail to Front of Linked List

### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - What should we return if the list is empty or only has one node?
# - Should the function change the list in place or build a new list?

### P - Plan
# 2. Write out in plain English what you want to do:
# Walk to the end of the list while keeping track of the node right before the tail, disconnect the tail, then point the tail at the old head and return the tail as the new head.

# 3. Translate each sub-problem into pseudocode:
# If the head is None or has no next node, return the head
# Set previous to None and current to the head
# While current has a next node
# Move previous to current and current to the next node
# Set previous's next to None to cut off the tail
# Set the tail's next to the head
# Return the tail

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def tail_to_head(head):
    if head is None or head.next is None:
        return head

    previous = None
    current = head

    while current.next:
        previous = current
        current = current.next

    previous.next = None
    current.next = head

    return current

# Time: O(n) where n is the number of nodes, since we walk through the whole list to find the tail.
# Space: O(1) because we only keep track of two nodes.

#I picked this problem because it helped me practice tracking the previous node while walking a linked list.

# Problem 9: Create Double Links

### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - Should the prev attribute default to None the same way next does?
# - Do we need to set both the next and prev pointers, or does setting one update the other?

### P - Plan
# 2. Write out in plain English what you want to do:
# Add a prev attribute to the Node constructor so each node can point backwards, then link the head and tail in both directions.

# 3. Translate each sub-problem into pseudocode:
# Add a prev parameter to the constructor that defaults to None
# Save prev on the node just like value and next
# Create the head and tail nodes
# Set the head's next to the tail
# Set the tail's prev to the head

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

head = Node("Isabelle")
tail = Node("K.K. Slider")

head.next = tail
tail.prev = head

# Time: O(1) because we create two nodes and set two pointers.
# Space: O(1) because we only store two nodes.

#I picked this problem because it helped me understand how a doubly linked list lets you move backwards with a prev pointer.
