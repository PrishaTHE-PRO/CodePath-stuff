# Problem 1:

### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - Can either of the input trees be empty (None)?
# - Should the merged tree reuse the existing nodes, or should it create an entirely new tree?

### P - Plan
# 2. Write out in plain English what you want to do:
# - If both nodes are None, return None.
# - If one node is None, return the other node.
# - If both nodes exist, add their values together.
# - Recursively merge the left children.
# - Recursively merge the right children.
# - Return the updated root node.

# 3. Translate each sub-problem into pseudocode:
# - If order1 is None:
#       return order2
# - If order2 is None:
#       return order1
# - order1.val += order2.val
# - order1.left = merge_orders(order1.left, order2.left)
# - order1.right = merge_orders(order1.right, order2.right)
# - return order1

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:

class TreeNode():
    def __init__(self, quantity, left=None, right=None):
        self.val = quantity
        self.left = left
        self.right = right

def merge_orders(order1, order2):
    if order1 is None:
        return order2
    if order2 is None:
        return order1

    order1.val += order2.val
    order1.left = merge_orders(order1.left, order2.left)
    order1.right = merge_orders(order1.right, order2.right)

    return order1

# Problem 2: 
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - What should be returned if the tree is empty?
# - Should the function return or print the list?

### P - Plan
# 2. Write out in plain English what you want to do:
# - Use a queue to perform a level order traversal.
# - Visit each node and add its value to the result.

# 3. Translate each sub-problem into pseudocode:
# - If root is None, return []
# - Add root to queue
# - While queue is not empty:
#     - Remove front node
#     - Add value to result
#     - Add left and right children if they exist
# - Return result

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
from collections import deque

class Puff():
    def __init__(self, flavor, left=None, right=None):
        self.val = flavor
        self.left = left
        self.right = right

def print_design(design):
    if design is None:
        return []

    result = []
    queue = deque([design])

    while queue:
        node = queue.popleft()
        result.append(node.val)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result

# Problem 3: 
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - What should be returned if the tree is empty?
# - Does a tree with one node have 1 tier?

### P - Plan
# 2. Write out in plain English what you want to do:
# - Recursively find the height of the left and right subtrees.
# - Return 1 plus the larger height.

# 3. Translate each sub-problem into pseudocode:
# - If cake is None, return 0
# - left = max_tiers(cake.left)
# - right = max_tiers(cake.right)
# - Return 1 + max(left, right)

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class TreeNode():
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def max_tiers(cake):
    if cake is None:
        return 0

    left = max_tiers(cake.left)
    right = max_tiers(cake.right)

    return 1 + max(left, right)

# Problem 4: 
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - What should be returned if the tree is empty?
# - Does a tree with one node have 1 tier?

### P - Plan
# 2. Write out in plain English what you want to do:
# - Use level order traversal.
# - Count the number of levels visited.

# 3. Translate each sub-problem into pseudocode:
# - If cake is None, return 0
# - Add root to queue
# - While queue is not empty:
#     - Process one level
#     - Add children to queue
#     - Increment level count
# - Return level count

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
from collections import deque

class TreeNode():
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def max_tiers(cake):
    if cake is None:
        return 0

    queue = deque([cake])
    levels = 0

    while queue:
        for _ in range(len(queue)):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        levels += 1

    return levels

# Problem 5: 
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - What should be returned if the tree is empty?
# - Must the sum end at a leaf node?

### P - Plan
# 2. Write out in plain English what you want to do:
# - Recursively subtract each node's value from the target.
# - If a leaf is reached, check if the remaining sum equals its value.

# 3. Translate each sub-problem into pseudocode:
# - If inventory is None, return False
# - If node is a leaf, return order_size == node.val
# - remaining = order_size - node.val
# - Return recursive call on left or right

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class TreeNode():
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def can_fulfill_order(inventory, order_size):
    if inventory is None:
        return False

    if inventory.left is None and inventory.right is None:
        return order_size == inventory.val

    remaining = order_size - inventory.val

    return (can_fulfill_order(inventory.left, remaining) or
            can_fulfill_order(inventory.right, remaining))