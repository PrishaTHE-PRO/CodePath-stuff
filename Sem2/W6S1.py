# Problem 4: On Repeat

### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - What should we return if the playlist is empty or only has one song with no next?
# - Can the cycle point back to the head, or only to a node in the middle of the list?

### P - Plan
# 2. Write out in plain English what you want to do:
# Use a slow pointer that moves one song at a time and a fast pointer that moves two songs at a time. If the list loops, the fast pointer will eventually catch up to the slow pointer. If the fast pointer reaches the end, there is no cycle.

# 3. Translate each sub-problem into pseudocode:
# Set slow and fast to the head
# While fast is not None and fast's next is not None
# Move slow forward one node
# Move fast forward two nodes
# If slow and fast are the same node, return True
# Return False

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class SongNode:
    def __init__(self, song, artist, next=None):
        self.song = song
        self.artist = artist
        self.next = next

def on_repeat(playlist_head):
    slow = playlist_head
    fast = playlist_head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow is fast:
            return True

    return False

# Time: O(n) where n is the number of songs, since the fast pointer passes through the list at most a constant number of times before meeting the slow pointer or hitting the end.
# Space: O(1) because we only keep track of two pointers.

#I picked this problem because it helped me practice the slow and fast pointer technique for detecting a cycle in a linked list.

# Problem 5: Loop Length

### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - Does the length of the cycle count only the songs inside the loop, or every song in the list?
# - What should we return if the playlist is empty?

### P - Plan
# 2. Write out in plain English what you want to do:
# Use slow and fast pointers to find a meeting point inside the cycle. Once they meet, keep one pointer still and walk the other around the loop counting steps until it comes back to the meeting point. That count is the length of the cycle.

# 3. Translate each sub-problem into pseudocode:
# Set slow and fast to the head
# While fast is not None and fast's next is not None
# Move slow forward one node
# Move fast forward two nodes
# If slow and fast are the same node
# Set count to 1
# Set current to slow's next
# While current is not slow
# Move current forward and add 1 to count
# Return count
# Return 0

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def loop_length(playlist_head):
    slow = playlist_head
    fast = playlist_head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow is fast:
            count = 1
            current = slow.next

            while current is not slow:
                current = current.next
                count += 1

            return count

    return 0

# Time: O(n) where n is the number of songs, since finding the meeting point takes at most a constant number of passes through the list and walking the loop once takes at most n steps.
# Space: O(1) because we only keep track of a few pointers and a counter.

#I picked this problem because it helped me see how the slow and fast pointer meeting point can be reused to measure the size of a cycle.

# Problem 6: Volume Control

### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - If a node has the same value as one of its neighbors, is it still a critical point?
# - What should we return if the list has fewer than three nodes?

### P - Plan
# 2. Write out in plain English what you want to do:
# Walk through the list while keeping track of the previous node, the current node, and the next node. For every node that has a neighbor on both sides, check if it is smaller than both neighbors or larger than both neighbors, and count it if so.

# 3. Translate each sub-problem into pseudocode:
# If the head is None or has fewer than three nodes, return 0
# Set previous to the head and current to the head's next
# Set count to 0
# While current has a next node
# If current's value is less than both previous's and next's values, add 1 to count
# Else if current's value is greater than both previous's and next's values, add 1 to count
# Move previous to current and current to current's next
# Return count

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def count_critical_points(song_audio):
    if song_audio is None or song_audio.next is None or song_audio.next.next is None:
        return 0

    previous = song_audio
    current = song_audio.next
    count = 0

    while current.next is not None:
        before = previous.value
        after = current.next.value

        if current.value < before and current.value < after:
            count += 1
        elif current.value > before and current.value > after:
            count += 1

        previous = current
        current = current.next

    return count

# Time: O(n) where n is the number of nodes, since we visit each node once and do constant work at each step.
# Space: O(1) because we only keep track of two pointers and a counter.

#I picked this problem because it helped me practice tracking the previous and next nodes at the same time while walking a linked list.
