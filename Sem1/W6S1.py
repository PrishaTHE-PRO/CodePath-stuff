# Problem 1: Building a Playlist
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - Should i create one SongNode object per line?
# - How do I connect each node to form the same linked list?

### P - Plan
# 2. Write out in plain English what you want to do:
# - create each SongNode seperatly, then use the .next attribute to link them together

# 3. Translate each sub-problem into pseudocode:
# - create node for each song
# - set Uptown Funk.next = Party Rock Anthem
# - Set Party Rock Anthem.next = Bad Romance

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
uptown_funk = SongNode("Uptown Funk")
party_rock_anthem = SongNode("Party Rock Anthem")
bad_romance = SondNode("Bad Romance")

uptown_funk.next = party_rock_anthem
party_rock_anthem.next = bad_romance

top_hits_2010s = uptown_funk

# Problem 2: Top Artists
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - should duplicate artists be counted multiple times?
# - what should be returned if the playlist is empty?

### P - Plan
# 2. Write out in plain English what you want to do:
# - traverse the linked list and count how mnay times each artist appears using a dict

# 3. Translate each sub-problem into pseudocode:
# - create empty dict
# - traver linked list
# - if artist in dect, incremnet count
# - else add artist with count = 1
# - return dict
# - Time: O(n) Space: O(k)

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def get_artist_frequency(playlist):
    freq = {}
    current = playlist

    while current:
        if current.artist in freq:
            freq[current.artist] += 1
        else:
            freq[current.artist] = 1
        current = current.next
    
    return freq

# Problem 3: Glitiching Out
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - what should happen if the song to remove is the head node?
# - what should happen if the song is not in the playlist?

### P - Plan
# 2. Write out in plain English what you want to do:
# - traverse the linked list until the target sound is found, then update the prevous node's next pointer to skip over the node being removed

# 3. Translate each sub-problem into pseudocode:
# - if the list is empty, return None
# - is the head contains the soung, return the next node
# - traverse the list while there is a next node
# - is the next node contains the song, skip over it by updating the next pointer
# - return the head of the modified list

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def removed_song(playlist_head, song):
    if not playlist_head:
        return None
    if playlist_head.song == song:
        return playlist_head.next
    
    current = playlist_head
    while current.next:
        if current.next.song == song:
            current.next = current.next.next
            return playlist_head
        current = current.next
    
    return playlist_head

# Problem 4: On Repeat
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - what should be returned if the playlist is empty?
# - how can i detect a cycle without modifying the linked list?

### P - Plan
# 2. Write out in plain English what you want to do:
# - use a slow pointer that moved one node at a time and a fast pointer that moves 2 nodes at a time
# - if they ever meet, there is a cycle
# - if the fast pointer reaches the end. there is no cycle

# 3. Translate each sub-problem into pseudocode:
# - set slow and fast to the head
# - while fast and fast.next exist:
# - move slow one step
# - move fast two steps
# - if slow equals fast, return True
# - return fale

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def on_repeat(playlist_head):
    slow = playlist_head
    fast = playlist_head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True
        
    return False

# Problem 5: Looped
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - What should be returned if the linked list has no cycle?
# - Once a cycle is found, how can I determine its length?

### P - Plan
# 2. Write out in plain English what you want to do:
# - Use slow and fast pointers to detect a cycle. If they meet, keep one pointer in place and move the other around the cycle until it returns to the same node, counting the number of steps.

# 3. Translate each sub-problem into pseudocode:
# - Set slow and fast to the head
# - While fast and fast.next exist:
#     - Move slow one step
#     - Move fast two steps
#     - If slow equals fast:
#         - Set length = 1
#         - Move one pointer one step
#         - While it has not returned to the meeting point:
#             - Increment length
#             - Move one step
#         - Return length
# - Return 0

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def loop_length(playlist_head):
    slow = playlist_head
    fast = playlist_head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            length = 1
            current = slow.next

            while current != slow:
                length += 1
                current = current.next

            return length
