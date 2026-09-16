# Problem 1: Grafting Apples
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - should i only create the tree by assigning left and right childeren?
# - should the node values exactly match the labels shown in the diagram?

### P - Plan
# 2. Write out in plain English what you want to do:
# - create each child node and connect them to the corrent left or right position

# 3. Translate each sub-problem into pseudocode:
# - Set root.left = TreeNode("Mcintosh")
# - Set root.right = TreeNode("Granny Smith")
# - Add Fuji and Oapl as Mcintosh's left and right childeren
# - add crab and gala as granny smith's left and right childeren

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

root = TreeNode("Trunk")

root.left = TreeNode("Mcintosh")
root.right = TreeNode("Grany Smith")

root.left.left = TreeNode("Fuji")
root.left.right = TreeNode("Opal")

root.right.left = TreeNode("Crab")
root.right.right = TreeNode("Gala")


# Problem 2: Calculating Yield
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - will the tree always have exactly one root and two leaf childeren?
# - will the root value always be one of "+", "-", "*", or "/"?

### P - Plan
# 2. Write out in plain English what you want to do:
# - read the operate at the root, then apply it to the values of the left and right children

# 3. Translate each sub-problem into pseudocode:
# - store left and right child values
# - check th root operator
# - retrun the result of the corresponsing operation

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def calculate_yield(root):
    left = root.left.val
    right = root.right.val

    if root.val == "+":
        return left + right
    elif root.val == "-":
        return left - right
    elif root.val == "*":
        return left * right
    elif root.val == "/":
        return left / right

# Problem 3: Ivy Cutting
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - should i always follow the right child until there is no right child?
# - if the root has no right child, should I return only the root value?

### P - Plan
# 2. Write out in plain English what you want to do:
# - start at the root, add each node's value to a list, and keep moving right until theres no right chils

# 3. Translate each sub-problem into pseudocode:
# - create an empty list
# - add the root value
# - while the current node has a right child:
#   - move to the right child 
#   - add its value to the list
# - return the list

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def right_vine(root):
    path = []
    current = root

    while current:
        path.append(current.val)
        current = current.right

    return path

# Problem 4: Ivy Cutting II
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - should I recursively follow only the right child?
# - if there is no right child, should I return only the current node's value?

### P - Plan
# 2. Write out in plain English what you want to do:
# - use recursion to add the current node's value, then continue down the right until no right nodes

# 3. Translate each sub-problem into pseudocode:
# - if the node has no right child:
#   - return a lsit containing its value
# - otherwise:
#   - return the ucrrent value + recursive call on the right child

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def right_vine(root):
    if root.right is None:
        return [root.val]
    
    return [root.val] + right_vine(root.right)

# Problem 5: Count the Tree Leaves
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - should a node with no left and no right child be counted as a leaf?
# - should I return 0 if the tree is empty?

### P - Plan
# 2. Write out in plain English what you want to do:
# - recursively visit every node
# - if a node is a leaf, return 1
# - else return the sum of the leaves in its left and right subtrees

# 3. Translate each sub-problem into pseudocode:
# - if the node is None, return 0
# - if the node has no childeren, return 1
# - Return count_leaves(left) + count_leaves(right)

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def count_leaves(root):
    if root is None:
        return 0
    
    if root.left is None and root.right is None:
        return 1
    
    return count_leaves(root.left() + root.right())