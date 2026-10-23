# Problem 6: Strongest Avenger

### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - What should we return if the list of strengths is empty?
# - Can strengths be negative, or are they always positive numbers?

### P - Plan
# 2. Write out in plain English what you want to do:
# Compare the first strength to the strongest strength in the rest of the list. To find the strongest in the rest, call the same function on the list without the first element. The base case is a list with one strength, which is its own maximum.

# 3. Translate each sub-problem into pseudocode:
# If the list has only one strength, return that strength
# Set rest_max to the result of calling the function on the list without the first element
# If the first strength is greater than rest_max, return the first strength
# Otherwise return rest_max

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def strongest_avenger(strengths):
    if len(strengths) == 1:
        return strengths[0]

    rest_max = strongest_avenger(strengths[1:])

    if strengths[0] > rest_max:
        return strengths[0]

    return rest_max

# Time: O(n^2) where n is the number of strengths, since we make n recursive calls and each call slices the list, which copies up to n elements.
# Space: O(n) because the recursion goes n levels deep and each level holds its own slice of the list.

#I picked this problem because it helped me practice breaking a problem into a base case and a smaller version of the same problem.

# Problem 7: Counting Vibranium Deposits

### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - Should a lowercase "v" count as a vibranium deposit, or only uppercase "V"?
# - What should we return if the string is empty?

### P - Plan
# 2. Write out in plain English what you want to do:
# Look at the first character of the string. If it is a "V", count 1, otherwise count 0. Then add the number of deposits in the rest of the string by calling the same function on the string without the first character. An empty string has 0 deposits.

# 3. Translate each sub-problem into pseudocode:
# If the string is empty, return 0
# If the first character is "V", set current to 1, otherwise set current to 0
# Return current plus the result of calling the function on the rest of the string

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def count_deposits(resources):
    if resources == "":
        return 0

    if resources[0] == "V":
        current = 1
    else:
        current = 0

    return current + count_deposits(resources[1:])

# Time: O(n^2) where n is the length of the string, since we make n recursive calls and each call slices the string, which copies up to n characters.
# Space: O(n) because the recursion goes n levels deep and each level holds its own slice of the string.

#I picked this problem because it helped me practice counting with recursion by adding one character's result to the result for the rest of the string.

# Problem 8: Merging Missions

### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - What should we return if one or both of the lists are empty?
# - If both lists have the same value, does it matter which node comes first?

### P - Plan
# 2. Write out in plain English what you want to do:
# Compare the heads of the two lists. Whichever is smaller becomes the head of the merged list, and its next pointer is set to the result of merging the rest of that list with the other list. If one list is empty, the answer is just the other list.

# 3. Translate each sub-problem into pseudocode:
# If mission1 is None, return mission2
# If mission2 is None, return mission1
# If mission1's value is less than or equal to mission2's value
# Set mission1's next to the merge of mission1's next and mission2
# Return mission1
# Otherwise
# Set mission2's next to the merge of mission1 and mission2's next
# Return mission2

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def merge_missions(mission1, mission2):
    if mission1 is None:
        return mission2

    if mission2 is None:
        return mission1

    if mission1.value <= mission2.value:
        mission1.next = merge_missions(mission1.next, mission2)
        return mission1

    mission2.next = merge_missions(mission1, mission2.next)
    return mission2

# Time: O(n + m) where n and m are the lengths of the two lists, since each recursive call moves past one node and we stop once one list runs out.
# Space: O(n + m) because the recursion can go as deep as the total number of nodes.

#I picked this problem because it helped me practice merging two sorted linked lists by reusing the existing nodes instead of creating new ones.
