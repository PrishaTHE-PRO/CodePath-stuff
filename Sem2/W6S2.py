# Problem 2: Clearing the Path

### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - If there is no cycle, should we just return the head unchanged?
# - Can the cycle loop all the way back to the head, or only to a node in the middle?

### P - Plan
# 2. Write out in plain English what you want to do:
# Use slow and fast pointers to detect whether there is a cycle. If they meet, move one pointer back to the head and walk both one step at a time. The node right before they meet again is the last node in the loop, so set its next to None to break the cycle.

# 3. Translate each sub-problem into pseudocode:
# If the head is None, return None
# Set slow and fast to the head
# While fast is not None and fast's next is not None
# Move slow forward one node and fast forward two nodes
# If slow and fast are the same node, break out of the loop
# If no cycle was found, return the head
# Set slow back to the head
# While slow's next is not fast's next
# Move slow and fast forward one node each
# Set fast's next to None to cut the loop
# Return the head

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def clear_trail(trailhead):
    if trailhead is None:
        return None

    slow = trailhead
    fast = trailhead
    has_cycle = False

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow is fast:
            has_cycle = True
            break

    if not has_cycle:
        return trailhead

    slow = trailhead

    while slow.next is not fast.next:
        slow = slow.next
        fast = fast.next

    fast.next = None

    return trailhead

# Time: O(n) where n is the number of nodes, since detecting the cycle and walking to the start of the loop each take at most a constant number of passes through the list.
# Space: O(1) because we only keep track of two pointers and a flag.

#I picked this problem because it helped me practice using the slow and fast pointer meeting point to find where a cycle begins and break it.

# Problem 4: Controlled Burns

### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - What should happen if the trail ends in the middle of keeping m markers or removing n markers?
# - Can m be 0, and if so should we remove nodes starting from the head?

### P - Plan
# 2. Write out in plain English what you want to do:
# Walk the list in rounds. In each round, move forward m - 1 times to the last marker we want to keep, then skip ahead n nodes past it and connect the kept marker directly to whatever comes after the removed ones. Repeat until we run out of nodes.

# 3. Translate each sub-problem into pseudocode:
# Set current to the head
# While current is not None
# Move current forward m - 1 times, stopping early if we hit the end
# If current is None, return the head
# Set skip to current's next
# Move skip forward n times, stopping early if we hit the end
# Set current's next to skip
# Move current to skip
# Return the head

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def selective_trail_clearing(trailhead, m, n):
    current = trailhead

    while current is not None:
        for _ in range(m - 1):
            if current is None:
                return trailhead
            current = current.next

        if current is None:
            return trailhead

        skip = current.next

        for _ in range(n):
            if skip is None:
                break
            skip = skip.next

        current.next = skip
        current = skip

    return trailhead

# Time: O(n) where n is the number of nodes, since each node is visited once either while being kept or while being skipped.
# Space: O(1) because we only keep track of two pointers.

#I picked this problem because it helped me practice removing a whole run of nodes at once by reconnecting a single pointer.

# Problem 5: Geocaching

### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - What should we return if the list is empty?
# - Will the values always be 0 or 1, or do we need to handle other numbers?

### P - Plan
# 2. Write out in plain English what you want to do:
# Walk through the list from the head. Keep a running total, and for each node double the total and add the node's value. Since the first marker is the most significant bit, each doubling shifts the earlier bits one place to the left.

# 3. Translate each sub-problem into pseudocode:
# Set result to 0
# Set current to the head
# While current is not None
# Set result to result times 2 plus current's value
# Move current to the next node
# Return result

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def locate_cache(cache_labels):
    result = 0
    current = cache_labels

    while current is not None:
        result = result * 2 + current.value
        current = current.next

    return result

# Time: O(n) where n is the number of nodes, since we visit each node once and do constant work at each step.
# Space: O(1) because we only keep track of the running total and the current node.

#I picked this problem because it helped me practice converting binary to decimal one bit at a time while walking a linked list.
