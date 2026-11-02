# Problem 6: Pruning Plans

### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - What should we return if the root is None?
# - If a node only has one child, should we just skip the missing child?

### P - Plan
# 2. Write out in plain English what you want to do:
# Get the postorder list of the left subtree by calling the same function on the left child, then do the same for the right child. Combine the two lists and add the current node's value at the end. An empty tree has no values, so it returns an empty list.

# 3. Translate each sub-problem into pseudocode:
# If root is None, return an empty list
# Set left_values to the result of calling the function on the left child
# Set right_values to the result of calling the function on the right child
# Return left_values plus right_values plus a list with the root's value

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def survey_tree(root):
    if root is None:
        return []

    left_values = survey_tree(root.left)
    right_values = survey_tree(root.right)

    return left_values + right_values + [root.val]

# Time: O(n log n) where n is the number of nodes, since we visit each node once and combining the lists copies a total of n values across each of the log n levels of the balanced tree.
# Space: O(n) because the returned list holds n values, and the recursion only goes log n levels deep since the tree is balanced.

#I picked this problem because it helped me practice postorder traversal by handling both subtrees before the root.

# Problem 7: Foraging Berries

### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - Should a node with a value exactly equal to the threshold be counted, or only values strictly greater?
# - What should we return if the root is None?

### P - Plan
# 2. Write out in plain English what you want to do:
# Find the harvest from the left subtree and the right subtree by calling the same function on each child. If the current node's value is greater than the threshold, add it to the total. An empty tree has nothing to harvest, so it returns 0.

# 3. Translate each sub-problem into pseudocode:
# If root is None, return 0
# Set left_sum to the result of calling the function on the left child
# Set right_sum to the result of calling the function on the right child
# If the root's value is greater than threshold, return the root's value plus left_sum plus right_sum
# Otherwise return left_sum plus right_sum

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def harvest_berries(root, threshold):
    if root is None:
        return 0

    left_sum = harvest_berries(root.left, threshold)
    right_sum = harvest_berries(root.right, threshold)

    if root.val > threshold:
        return root.val + left_sum + right_sum

    return left_sum + right_sum

# Time: O(n) where n is the number of nodes, since we visit each node once and do constant work at each one.
# Space: O(log n) because the recursion goes log n levels deep since the tree is balanced.

#I picked this problem because it helped me practice combining results from both subtrees while only counting the nodes that meet a condition.

# Problem 8: Flower Fields

### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - Is the search case sensitive, so that "lilac" would not match "Lilac"?
# - What should we return if the root is None?

### P - Plan
# 2. Write out in plain English what you want to do:
# Check if the current node is the flower we want. If it is not, search the left subtree, and if the flower is not there, search the right subtree. The tree is not sorted, so we may need to check every node. An empty tree does not contain the flower, so it returns False.

# 3. Translate each sub-problem into pseudocode:
# If root is None, return False
# If the root's value equals flower, return True
# Return True if calling the function on the left child or the right child returns True

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def find_flower(root, flower):
    if root is None:
        return False

    if root.val == flower:
        return True

    return find_flower(root.left, flower) or find_flower(root.right, flower)

# Time: O(n) where n is the number of nodes, since the tree is not sorted and in the worst case the flower is missing, so we visit every node once.
# Space: O(log n) because the recursion goes log n levels deep since the tree is balanced.

#I picked this problem because it helped me practice searching a tree and stopping early as soon as the target is found.
