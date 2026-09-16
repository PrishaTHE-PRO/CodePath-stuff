# Problem 1: Wild Goose Chase
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - What should be returned if the linked list is empty?
# - Does a circular list only count if the tail points directly back to the head?

### P - Plan
# 2. Write out in plain English what you want to do:
# - Traverse the linked list until reaching the tail. If the tail's next pointer points to the head, return True; otherwise, return False.

# 3. Translate each sub-problem into pseudocode:
# - If the list is empty, return False
# - Traverse to the last node
# - Check if the last node's next pointer is the head
# - Return True if it is, otherwise False
# - O(n) and O(1)

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def is_circular(clues):
    if not clues:
        return False
    
    current = clues

    while current.next and current.next != clues:
        current = current.next

    return current.next == clues

# Problem 2: Breaking the Cycle
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - What should be returned if the linked list has no cycle?
# - Should the function return only the values inside the cycle?

### P - Plan
# 2. Write out in plain English what you want to do:
# - Use the slow and fast pointer method to detect a cycle. If one exists,
#   find the start of the cycle, then traverse the cycle once to collect
#   all node values into an array.

# 3. Translate each sub-problem into pseudocode:
# - Set slow and fast to the head
# - Move slow one step and fast two steps until they meet or reach the end
# - If no cycle exists, return an empty list
# - Reset one pointer to the head
# - Move both pointers one step until they meet at the start of the cycle
# - Traverse the cycle once, adding each value to a list
# - Return the list

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def collect_false_evidence(evidence):
    slow = evidence
    fast = evidence

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            break
    
    else:
        return []
    
    slow = evidence 
    while slow != fast:
        slow = slow.next
        fast = fast.next

    result = []
    current = slow
    
    while True:
        result.append(current.value)
        current = current.next
        if current == slow:
            break

    return result

# Problem 3: Prioritizing Suspects
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - should the relative order of nodes within each partitions be preserved?
# - what should be returned if the linked is empty?

### P - Plan
# 2. Write out in plain English what you want to do:
# - traverse the list once, placing nodes into two seperate lists:
#   one for values greater than the threshold and one for values less
#   than or equal to the threshold. Then connect the two lists.

# 3. Translate each sub-problem into pseudocode:
# - 

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def partition(suspect_ratings, threshold):
    greater_dummy = Node(0)
    smaller_dummy = Node(0)

    greater = greater_dummy
    smaller = smaller_dummy
    current = suspect_ratings

    while current:
        if current.value > threshold:
            greater.next = current
            greater = greater.next
        else:
            smaller.next = current
            smaller = smaller.next
        current = current.next

    smaller.next = None
    greater.next = smaller_dummy.next

    return greater_dummy.next

# Problem 4: Puzzling it Out
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - Are both linked lists already sorted in ascending order?
# - What should be returned if one or both linked lists are empty?

### P - Plan
# 2. Write out in plain English what you want to do:
# - Compare the current nodes of both lists and repeatedly add the smaller
#   node to the merged list. When one list is exhausted, append the remaining
#   nodes from the other list.

# 3. Translate each sub-problem into pseudocode:
# - Create a dummy node for the merged list
# - Set a current pointer to the dummy node
# - While both lists have nodes:
#     - Compare their values
#     - Attach the smaller node to the merged list
#     - Advance the corresponding pointer
# - Attach any remaining nodes from either list
# - Return the node after the dummy

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def merge_timelines(known_timeline, witness_timeline):
    dummy = Node(0)
    current = dummy

    while known_timeline and witness_timeline:
        if known_timeline.value <= witness_timeline.value:
            current.next = known_timeline
            known_timeline = known_timeline.next
        else:
            current.next = witness_timeline
            witness_timeline = witness_timeline.next

        current = current.next

    if known_timeline:
        current.next = known_timeline
    else:
        current.next = witness_timeline

    return dummy.next


# Problem 5: A New Perspective
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - What should be returned if the linked list is empty or has only one node?
# - What if k is larger than the length of the linked list?

### P - Plan
# 2. Write out in plain English what you want to do:
# - Find the length of the linked list, connect the tail to the head to form
#   a circle, determine the new tail after rotating, break the circle, and
#   return the new head.

# 3. Translate each sub-problem into pseudocode:
# - If the list is empty, has one node, or k is 0, return the head
# - Traverse the list to find its length and tail
# - Compute k = k % length
# - If k is 0, return the head
# - Connect the tail to the head
# - Move to the new tail (length - k - 1 steps)
# - Set the new head to new_tail.next
# - Break the circle
# - Return the new head


### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def rotate_right(evidence, k):
    if not evidence or not evidence.next or k == 0:
        return evidence

    length = 1
    tail = evidence

    while tail.next:
        tail = tail.next
        length += 1

    k %= length
    if k == 0:
        return evidence

    tail.next = evidence

    new_tail = evidence
    for _ in range(length - k - 1):
        new_tail = new_tail.next

    new_head = new_tail.next
    new_tail.next = None

    return new_head