# Problem 2: Pumpkin Patch Path

### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - What should we return if the root is None?
# - If two paths tie for the most pumpkins, which one should we return?

### P - Plan
# 2. Write out in plain English what you want to do:
# For each node, find the best path in the left subtree and the best path in the right subtree by calling the same function on each child, along with how many pumpkins each path has. Pick the child path with more pumpkins and put the current node at the front of it. A leaf's best path is just itself. An empty tree has no path, so it gives 0 pumpkins and an empty list. Return only the path at the end.

# 3. Translate each sub-problem into pseudocode:
# Create a helper that returns a (total, path) pair for a node:
#   If node is None, return 0 and an empty list
#   Set left_total, left_path to the result of calling the helper on the left child
#   Set right_total, right_path to the result of calling the helper on the right child
#   If the node has no left child, use the right side
#   Otherwise if the node has no right child, use the left side
#   Otherwise use whichever side has the larger total
#   Return the node's value plus the chosen total, and a list with the node's value plus the chosen path
# Return the path from calling the helper on root

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
from collections import deque

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def max_pumpkins_path(root):
    def best_path(node):
        if node is None:
            return 0, []

        left_total, left_path = best_path(node.left)
        right_total, right_path = best_path(node.right)

        if node.left is None:
            total, path = right_total, right_path
        elif node.right is None:
            total, path = left_total, left_path
        elif left_total >= right_total:
            total, path = left_total, left_path
        else:
            total, path = right_total, right_path

        return node.val + total, [node.val] + path

    return best_path(root)[1]

# Time: O(n * h) where n is the number of nodes and h is the height of the tree. We visit each node once, but at each node we copy the chosen path, which can be up to h values long. This is O(n log n) if the tree is balanced.
# Space: O(h) for the recursion stack plus the path lists being built, which are at most h values long at each level. This is O(log n) if the tree is balanced.

#I picked this problem because it helped me practice returning more than one piece of information from each subtree and using it to build the answer.

# Problem 6: Find Next Order to Fulfill Today

### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - Should we compare the order by the node object itself, or by its value, since two orders could have the same name?
# - What should we return if the order is not in the tree?

### P - Plan
# 2. Write out in plain English what you want to do:
# Use breadth first search to go through the tree one level (day) at a time with a queue. For each level, pop the nodes from left to right. When we pop the node that is the current order, the next node in that same level is the next order. If the current order is the last node in its level, return None. If we never find the order, also return None.

# 3. Translate each sub-problem into pseudocode:
# If order_tree is None, return None
# Create a queue with the root
# While the queue is not empty:
#   Set level_size to the length of the queue
#   Loop i from 0 to level_size:
#     Pop a node from the front of the queue
#     If the node is order:
#       If i is the last index in the level, return None
#       Otherwise return the node at the front of the queue
#     If the node has a left child, add it to the queue
#     If the node has a right child, add it to the queue
# Return None

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def find_next_order(order_tree, order):
    if order_tree is None:
        return None

    queue = deque([order_tree])

    while queue:
        level_size = len(queue)

        for i in range(level_size):
            node = queue.popleft()

            if node is order:
                if i == level_size - 1:
                    return None
                return queue[0]

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return None

# Time: O(n) where n is the number of nodes, since in the worst case the order is near the end of the tree and each node is added to and removed from the queue once.
# Space: O(n) because the queue can hold up to about n/2 nodes at the bottom level of a balanced tree.

#I picked this problem because it helped me practice level order traversal and using the position of a node within its level.

# Problem 7: Can Rearrange Orders

### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - If both orders are empty, should we return True?
# - Can the same flavor appear more than once in an order?

### P - Plan
# 2. Write out in plain English what you want to do:
# Compare the two trees starting at the roots. If both nodes are empty they match, and if only one is empty or the flavors are different they do not match. Otherwise the children can line up in two ways: without a swap (left with left, right with right) or with a swap (left with right, right with left). If either way works for both pairs of children, the orders can be rearranged to match.

# 3. Translate each sub-problem into pseudocode:
# If order1 and order2 are both None, return True
# If only one of them is None, return False
# If order1's value does not equal order2's value, return False
# Set no_swap to True if order1.left matches order2.left and order1.right matches order2.right
# Set swap to True if order1.left matches order2.right and order1.right matches order2.left
# Return True if no_swap or swap is True

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def can_rearrange_orders(order1, order2):
    if order1 is None and order2 is None:
        return True

    if order1 is None or order2 is None:
        return False

    if order1.val != order2.val:
        return False

    no_swap = can_rearrange_orders(order1.left, order2.left) and can_rearrange_orders(order1.right, order2.right)
    if no_swap:
        return True

    return can_rearrange_orders(order1.left, order2.right) and can_rearrange_orders(order1.right, order2.left)

# Time: O(n) where n is the number of nodes in the smaller tree. When the flavors are different, at most one of the two pairings can pass the flavor check at the children, so the mismatched pairing stops right away and each node is really only compared once. If many flavors repeat, both pairings can go deep before failing, so the worst case can be slower than O(n).
# Space: O(h) where h is the height of the smaller tree, because the recursion goes one level deeper for each level of the tree. This is O(log n) if the tree is balanced.

#I picked this problem because it helped me practice comparing two trees at the same time and trying both the swapped and unswapped options at every node.
