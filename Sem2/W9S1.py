# Problem 4: Maximum Tiers in Cake II

### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - What should we return if the cake is empty?
# - Does a cake with only one section (just the root) count as 1 tier?

### P - Plan
# 2. Write out in plain English what you want to do:
# Use breadth first search to go through the cake one tier (level) at a time with a queue. Each time we finish processing every section in a tier, add 1 to the tier count and move on to the children in the next tier. When the queue is empty, the count is the number of tiers. An empty cake has 0 tiers.

# 3. Translate each sub-problem into pseudocode:
# If cake is None, return 0
# Create a queue with the root and set tiers to 0
# While the queue is not empty:
#   Set level_size to the length of the queue
#   Repeat level_size times:
#     Pop a node from the front of the queue
#     If the node has a left child, add it to the queue
#     If the node has a right child, add it to the queue
#   Add 1 to tiers
# Return tiers

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
from collections import deque

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def max_tiers(cake):
    if cake is None:
        return 0

    queue = deque([cake])
    tiers = 0

    while queue:
        level_size = len(queue)

        for _ in range(level_size):
            node = queue.popleft()

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        tiers += 1

    return tiers

# Time: O(n) where n is the number of nodes, since each node is added to and removed from the queue once and we do constant work for each one.
# Space: O(n) because the queue can hold up to about n/2 nodes at the bottom level of a balanced tree.

#I picked this problem because it helped me practice solving the same problem with breadth first search instead of depth first search by counting levels with a queue.

# Problem 5: Can Fulfill Order

### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - What should we return if the inventory tree is empty?
# - Does the path have to end at a leaf, or can it stop at any node whose running sum equals order_size?

### P - Plan
# 2. Write out in plain English what you want to do:
# Walk down the tree from the root, subtracting each node's value from the order size as we go. When we reach a leaf, check if the remaining amount equals the leaf's value. If either the left or right subtree finds a matching path, the order can be fulfilled. An empty tree has no paths, so it returns False.

# 3. Translate each sub-problem into pseudocode:
# If inventory is None, return False
# Set remaining to order_size minus the root's value
# If the root has no left child and no right child, return True if remaining equals 0, otherwise False
# Return True if calling the function on the left child or the right child with remaining returns True

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def can_fulfill_order(inventory, order_size):
    if inventory is None:
        return False

    remaining = order_size - inventory.val

    if inventory.left is None and inventory.right is None:
        return remaining == 0

    return can_fulfill_order(inventory.left, remaining) or can_fulfill_order(inventory.right, remaining)

# Time: O(n) where n is the number of nodes, since in the worst case no path matches and we visit every node once, doing constant work at each one.
# Space: O(log n) because the recursion goes log n levels deep since the tree is balanced.

#I picked this problem because it helped me practice passing information down the tree by updating the remaining amount at each level.

# Problem 6: Icing Cupcakes in Zigzag Order

### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - What should we return if the cupcakes tree is empty?
# - Should the first row (the root) always be iced left to right?

### P - Plan
# 2. Write out in plain English what you want to do:
# Use a queue to visit the tree one level at a time. For each level, collect the values of all the nodes in that level from left to right and add their children to the queue. If the level should go right to left, reverse the collected values before adding them to the result. Flip the direction after every level. An empty tree returns an empty list.

# 3. Translate each sub-problem into pseudocode:
# If cupcakes is None, return an empty list
# Create a queue with the root, an empty result list, and set left_to_right to True
# While the queue is not empty:
#   Set level_size to the length of the queue and create an empty level list
#   Repeat level_size times:
#     Pop a node from the front of the queue and add its value to level
#     If the node has a left child, add it to the queue
#     If the node has a right child, add it to the queue
#   If left_to_right is False, reverse level
#   Add the values in level to result
#   Flip left_to_right
# Return result

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def zigzag_icing_order(cupcakes):
    if cupcakes is None:
        return []

    queue = deque([cupcakes])
    result = []
    left_to_right = True

    while queue:
        level_size = len(queue)
        level = []

        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        if not left_to_right:
            level.reverse()

        result.extend(level)
        left_to_right = not left_to_right

    return result

# Time: O(n) where n is the number of nodes, since each node is added to and removed from the queue once, and reversing each level only touches the nodes in that level, which adds up to n in total.
# Space: O(n) because the result list holds n values, and the queue can hold up to about n/2 nodes at the bottom level of a balanced tree.

#I picked this problem because it helped me practice level order traversal with a queue and changing the direction for every other level.
