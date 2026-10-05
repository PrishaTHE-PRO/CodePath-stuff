# Problem 6: NFT Queue Processing

### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - Does the processing time change the order, or is it always first in, first out?
# - What should we return if the queue is empty?

### P - Plan
# 2. Write out in plain English what you want to do:
# Put the NFTs in a queue, remove them from the front one at a time, and save each name in the order it was removed.

# 3. Translate each sub-problem into pseudocode:
# Create a queue from the list of NFTs
# Create an empty result list
# While the queue is not empty
# Remove the NFT at the front of the queue
# Add its name to the result
# Return the result

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
from collections import deque

def process_nft_queue(nft_queue):
    queue = deque(nft_queue)
    processed = []

    while queue:
        nft = queue.popleft()
        processed.append(nft["name"])

    return processed

# Time: O(n) where n is the number of NFTs, since each one is removed from the queue once.
# Space: O(n) for the queue and the result list.

#I picked this problem because it helped me practice using a queue to process items in FIFO order.

# Problem 7: Validate NFT Addition

### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - Should an empty list of actions count as balanced?
# - Will the list only contain "add" and "remove"?

### P - Plan
# 2. Write out in plain English what you want to do:
# Use a stack to keep track of each "add", and pop one off for every "remove". The actions are balanced if the stack is empty at the end.

# 3. Translate each sub-problem into pseudocode:
# Create an empty stack
# Loop through the actions
# If the action is "add", push it onto the stack
# If the action is "remove" and the stack is empty, return False
# Otherwise pop from the stack
# Return True if the stack is empty

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def validate_nft_actions(actions):
    stack = []

    for action in actions:
        if action == "add":
            stack.append(action)
        else:
            if not stack:
                return False
            stack.pop()

    return len(stack) == 0

# Time: O(n) where n is the number of actions, since we loop through the list once.
# Space: O(n) because the stack could hold every action if they are all "add".

#I picked this problem because it helped me practice using a stack to check if actions are balanced.

# Problem 8: Find Closest NFT Values

### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - What should we return if the budget is smaller or larger than every value in the list?
# - Will the list always have at least two values?

### P - Plan
# 2. Write out in plain English what you want to do:
# Use two pointers at the start and end of the sorted list and keep moving them toward the budget until they are next to each other.

# 3. Translate each sub-problem into pseudocode:
# Set left to the first index and right to the last index
# While left and right are not next to each other
# Find the middle index
# If the middle value is less than or equal to the budget, move left to the middle
# Otherwise move right to the middle
# Return the values at left and right

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def find_closest_nft_values(nft_values, budget):
    left = 0
    right = len(nft_values) - 1

    while right - left > 1:
        mid = (left + right) // 2

        if nft_values[mid] <= budget:
            left = mid
        else:
            right = mid

    return (nft_values[left], nft_values[right])

# Time: O(log n) where n is the number of NFT values, since the search range is cut in half each loop.
# Space: O(1) because we only use a few variables.

#I picked this problem because it helped me practice using two pointers to search a sorted list.
