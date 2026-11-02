# Problem 5: Sorting Plants by Rarity

### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - What should we return if the collection is empty?
# - Can two plants have the same rarity key, or are the keys always unique?

### P - Plan
# 2. Write out in plain English what you want to do:
# In a BST, every smaller key is in the left subtree and every larger key is in the right subtree, so an inorder traversal visits the plants in sorted order. Get the sorted list of the left subtree, add the current plant as a (key, val) tuple, then add the sorted list of the right subtree. An empty tree returns an empty list.

# 3. Translate each sub-problem into pseudocode:
# If collection is None, return an empty list
# Set left_plants to the result of calling the function on the left child
# Set right_plants to the result of calling the function on the right child
# Return left_plants plus a list with the (key, val) tuple plus right_plants

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class TreeNode:
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.val = value
        self.left = left
        self.right = right

def sort_plants(collection):
    if collection is None:
        return []

    left_plants = sort_plants(collection.left)
    right_plants = sort_plants(collection.right)

    return left_plants + [(collection.key, collection.val)] + right_plants

# Time: O(n log n) where n is the number of plants if the tree is balanced, since we visit each node once and combining the lists copies a total of n tuples across each of the log n levels. If the tree is completely unbalanced it becomes O(n^2).
# Space: O(n) because the returned list holds n tuples, and the recursion goes as deep as the height of the tree.

#I picked this problem because it helped me practice inorder traversal and see why it returns the keys of a BST in sorted order.

# Problem 6: Finding a New Plant Within Budget

### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - If a plant's price is exactly equal to the budget, does it count? (No, the price must be strictly below the budget.)
# - Should we return the plant's name or its price? (The name, based on the example output.)

### P - Plan
# 2. Write out in plain English what you want to do:
# If the current plant costs the budget or more, it is too expensive and so is everything to its right, so the answer can only be in the left subtree. If the current plant is below budget, it is a possible answer, but a cheaper-than-budget plant with a higher price could be in the right subtree. Search the right subtree, and if nothing is found there, return the current plant. An empty tree returns None.

# 3. Translate each sub-problem into pseudocode:
# If inventory is None, return None
# If the current key is greater than or equal to budget, return the result of calling the function on the left child
# Set closer_plant to the result of calling the function on the right child
# If closer_plant is None, return the current plant's name
# Otherwise return closer_plant

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def pick_plant(inventory, budget):
    if inventory is None:
        return None

    if inventory.key >= budget:
        return pick_plant(inventory.left, budget)

    closer_plant = pick_plant(inventory.right, budget)

    if closer_plant is None:
        return inventory.val

    return closer_plant

# Time: O(h) where h is the height of the tree, since each call only goes down one side. This is O(log n) for a balanced tree with n plants and O(n) if the tree is completely unbalanced.
# Space: O(h) because the recursion goes at most h levels deep.

#I picked this problem because it helped me practice using the BST ordering to skip a whole subtree instead of checking every node.

# Problem 3: Add New Treasure to Collection

### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - What should we return if the grotto is empty?
# - Is the alphabetical order case sensitive, or will all item names start with a capital letter?

### P - Plan
# 2. Write out in plain English what you want to do:
# Compare the new item to the current node. If it comes earlier in the alphabet, add it to the left subtree, and if it comes later, add it to the right subtree. Once we reach an empty spot, create the new node there. If the item matches the current node, it already exists, so nothing changes. Each call returns its root so the parent stays connected to its child.

# 3. Translate each sub-problem into pseudocode:
# If grotto is None, return a new node with new_item
# If new_item is less than the grotto's value
# Set the grotto's left to the result of calling the function on the left child
# Otherwise if new_item is greater than the grotto's value
# Set the grotto's right to the result of calling the function on the right child
# Return grotto

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def add_treasure(grotto, new_item):
    if grotto is None:
        return TreeNode(new_item)

    if new_item < grotto.val:
        grotto.left = add_treasure(grotto.left, new_item)
    elif new_item > grotto.val:
        grotto.right = add_treasure(grotto.right, new_item)

    return grotto

# Time: O(log n) where n is the number of nodes, since each call moves down one level on one side of the balanced tree and does constant work.
# Space: O(log n) because the recursion goes log n levels deep since the tree is balanced.

#I picked this problem because it helped me practice inserting into a BST by using the ordering to find the right spot and reconnecting the nodes on the way back up.
