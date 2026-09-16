# Problem 1: 
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - Is an empty tree considered balanced?
# - Should we return as soon as an unbalanced subtree is found?

### P - Plan
# 2. Write out in plain English what you want to do:
# -  Recursively find the height of each subtree.
# - If any height difference is greater than 1, return False.

# 3. Translate each sub-problem into pseudocode:
# - Define helper(node):
#     - If node is None, return 0
#     - Get left and right heights
#     - If either is -1 or height difference > 1, return -1
#     - Return 1 + max(left, right)
# - Return helper(display) != -1

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def is_balanced(display):
    def height(node):
        if node is None:
            return 0

        left = height(node.left)
        right = height(node.right)

        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1

        return 1 + max(left, right)

    return height(display) != -1

# Problem 2: 
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - What should be returned if the tree is empty?
# - Should the sums be returned in level order?

### P - Plan
# 2. Write out in plain English what you want to do:
# - Use a queue for level order traversal.
# - Sum the values at each level and add the sum to the result.

# 3. Translate each sub-problem into pseudocode:
# - If orders is None, return []
# - Add root to queue
# - While queue is not empty:
#     - Compute sum of current level
#     - Add children to queue
#     - Append level sum to result
# - Return result

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
from collections import deque

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def sum_each_days_orders(orders):
    if orders is None:
        return []

    result = []
    queue = deque([orders])

    while queue:
        level_sum = 0

        for _ in range(len(queue)):
            node = queue.popleft()
            level_sum += node.val

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level_sum)

    return result

# Problem 3: 
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - What should be returned if the tree is empty?
# - Is the difference calculated as max value - min value at each level?

### P - Plan
# 2. Write out in plain English what you want to do:
# - Use level order traversal.
# - For each level, find the minimum and maximum sweetness.
# - Add their difference to the result.

# 3. Translate each sub-problem into pseudocode:
# - If chocolates is None, return []
# - Add root to queue
# - While queue is not empty:
#     - Find min and max values in current level
#     - Append max - min to result
#     - Add children to queue
# - Return result

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
from collections import deque

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def sweet_difference(chocolates):
    if chocolates is None:
        return []

    result = []
    queue = deque([chocolates])

    while queue:
        level_min = float('inf')
        level_max = float('-inf')

        for _ in range(len(queue)):
            node = queue.popleft()

            level_min = min(level_min, node.val)
            level_max = max(level_max, node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level_max - level_min)

    return result

# Problem 4: 
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - Can either tree be empty?
# - Can swaps be performed at any number of nodes?

### P - Plan
# 2. Write out in plain English what you want to do:
# - Recursively compare both trees.
# - At each node, check both the no-swap and swap cases.

# 3. Translate each sub-problem into pseudocode:
# - If both nodes are None, return True
# - If one is None or values differ, return False
# - Return (left-left and right-right) OR (left-right and right-left)

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class TreeNode():
    def __init__(self, flavor, left=None, right=None):
        self.val = flavor
        self.left = left
        self.right = right

def can_rearrange_orders(order1, order2):
    if order1 is None and order2 is None:
        return True
    if order1 is None or order2 is None:
        return False
    if order1.val != order2.val:
        return False

    return (
        (can_rearrange_orders(order1.left, order2.left) and
         can_rearrange_orders(order1.right, order2.right))
        or
        (can_rearrange_orders(order1.left, order2.right) and
         can_rearrange_orders(order1.right, order2.left))
    )

# Problem 5: 
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - Should the tree be modified in place?
# - What should be returned if the tree is empty?

### P - Plan
# 2. Write out in plain English what you want to do:
# - Traverse the BST in reverse inorder (right, root, left).
# - Keep a running sum of visited values.
# - Update each node with the running sum.

# 3. Translate each sub-problem into pseudocode:
# - sum = 0
# - Traverse right
# - sum += node.val
# - node.val = sum
# - Traverse left
# - Return root

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class TreeNode():
    def __init__(self, order_size, left=None, right=None):
        self.val = order_size
        self.left = left
        self.right = right

def larger_order_tree(orders):
    total = 0

    def dfs(node):
        nonlocal total
        if node is None:
            return

        dfs(node.right)
        total += node.val
        node.val = total
        dfs(node.left)

    dfs(orders)
    return orders