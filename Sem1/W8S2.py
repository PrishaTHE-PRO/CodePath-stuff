# Problem 1: Monstera Madness
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - should every node with an odd value be counted, not just leaf nodes?
# - should i return 0 if the tree is empty?

### P - Plan
# 2. Write out in plain English what you want to do:
# - traverse the entier tree
# - count the current node if its value is odd
# - then recursively count odd values in the left and right subtrees

# 3. Translate each sub-problem into pseudocode:
# - if the node is None, return 0
# - set count = 1 is the node value is odd, otherwise 0
# - retur ncount + count_odd_splits(left) + count_odd_splits(right)

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class TreeNode():
     def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.val = value
        self.left = left
        self.right = right

def count_odd_splits(root):
    if root is None:
        return 0
    
    count = 1 if root.val % 2 == 1 else 0

    return count + count_odd_splits(root.left) + count_odd_splits(root.right)

# Problem 2: Flower Finding
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - is the inventory guaranteed to be a valid binary search tree?
# - should I return False if the tree is empty?

### P - Plan
# 2. Write out in plain English what you want to do:
# - compare the target name with the current node. 
# - if it matches, return True.
# - if it is smaller, search the left subtree
# - otherwise, search the right subtree

# 3. Translate each sub-problem into pseudocode:
# - If the node is None, return False
# - If the node value equals the target, return True
# - If the target is less than the node value, search the left subtree
# - Otherwise, search the right subtree
# - O(n)

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def find_flower(inventory, name):
    if inventory is None:
        return False
    
    if inventory.val == name:
        return True
    elif name < inventory.val:
        return find_flower(inventory.left, name)
    else:
        return find_flower(inventory.right, name)

# Problem 3: Flower Finding II
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - is the goal to compare the 2 search algos?
# - should i discuss both balanced and unbalanced BSTs?

### I - Implement
# 4. Answer the questions:

# 1. How is the code different? Why?
# - find_flower() uses the BST property to search only one path.
# - non_bst_find_flower() cannot assume any ordering, so it searches both
#   the left and right subtrees.

# 2. What is the time complexity of non_bst_find_flower()?
# - O(n), where n is the number of nodes.
# - In the worst case, every node must be visited.
# - This is slower than find_flower() on a balanced BST, which is O(log n).

# 3. How would the time complexity of find_flower() change if the BST was not balanced?
# - The worst-case time complexity becomes O(n).
# - If the tree is skewed, searching may require visiting every node.

# Space Complexity:
# - non_bst_find_flower(): O(h), where h is the height of the tree.
#   For a balanced tree, h = O(log n); for a skewed tree, h = O(n).
# - find_flower(): O(log n) for a balanced BST due to the recursion stack.

# Problem 4: Adding a New Plant to the Collection
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - is the collection guaranteed to be a vlaid BST?
# - if the plant name already exists, should the new node always be inserted in the existing node's right subtree?

### P - Plan
# 2. Write out in plain English what you want to do:
# - compare the new plant's name with the current node
# - if it is smaller, insert it into the left subtree
# - otherwise, insert it into the right subtree
# - if an empty spot is found, create and return a new node

# 3. Translate each sub-problem into pseudocode:
# - If the current node is None, return a new TreeNode(name)
# - If name < current node value:
#     - Recursively insert into the left subtree
# - Otherwise:
#     - Recursively insert into the right subtree
# - Return the current node

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def add_plant(collection, name):
    if collection is None:
        return TreeNode(name)
    
    if name < collection.val:
        collection.left = add_plant(collection.left, name)
    else:
        collection.right = add_plant(collection.right, name)
        
    return collection

# Problem 5: Sorting Plants by Rarity
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - is the collection guaranteed to be a valid bst?
# - should the function return a list of (key, val) tuples in ascending order by key?

### P - Plan
# 2. Write out in plain English what you want to do:
# - perform an inorder traversal of the BST
# - visit the left subtree, then the current node,
# - then the right subtree, adding each node's (key, val) tuple to a list

# 3. Translate each sub-problem into pseudocode:
# - Create an empty result list
# - Define an inorder helper function:
#     - If node is None, return
#     - Traverse the left subtree
#     - Add (node.key, node.val) to the list
#     - Traverse the right subtree
# - Return the result list

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def sort_plant(collection):
    result = []

    def inorder(node):
        if node is None:
            return
        
        inorder(node.left)
        result.append((node.key, node.val))
        inorder(node.right)

    inorder(collection)
    return result