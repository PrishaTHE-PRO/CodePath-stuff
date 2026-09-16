# Problem 1: Finding the Perfect Cruise
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - Is cruise_lengths always sorted in ascending order?
# - Can the list contain duplicate cruise lengths?

### P - Plan
# 2. Write out in plain English what you want to do:
# - Use binary search to repeatedly check the middle element.
# - If the middle element matches vacation_length, return True.
# - If vacation_length is smaller, search the left half.
# - If vacation_length is larger, search the right half.
# - If the search space becomes empty, return False.

# 3. Translate each sub-problem into pseudocode:
# - Set left = 0 and right = len(cruise_lengths) - 1
# - While left <= right:
#     - Find middle index
#     - If middle value equals vacation_length, return True
#     - If middle value is less than vacation_length:
#         - Search right half
#     - Otherwise:
#         - Search left half
# - Return False
# - O(log n), where n is the number of cruise lengths.

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def find_cruise_length(cruise_lengths, vacation_length):
    left, right = 0, len(cruise_lengths) - 1
    while left <= right:
        mid = (left + right) // 2
        if cruise_lengths[mid] > vacation_length:
            right = mid - 1
        elif cruise_lengths[mid] < vacation_length:
            left = mid + 1
        else:
            return True
    return False

# Problem 2: Booking the Perfect Cruise Cabin
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - Is the cabins list always sorted in ascending order?
# - Can there be duplicate deck levels in the list?

### P - Plan
# 2. Write out in plain English what you want to do:
# - Use recursive binary search.
# - If the search range is empty, return the position where the preferred deck should be inserted.
# - Otherwise, compare the middle deck with the preferred deck.
# - If they are equal, return the middle index.
# - If the preferred deck is smaller, search the left half.
# - If it is larger, search the right half.

# 3. Translate each sub-problem into pseudocode:
# - Define helper(left, right):
#     - If left > right, return left
#     - Find middle index
#     - If cabins[mid] == preferred_deck, return mid
#     - If preferred_deck < cabins[mid]:
#         - Return helper(left, mid - 1)
#     - Otherwise:
#         - Return helper(mid + 1, right)
# - Return helper(0, len(cabins) - 1)

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def find_cabin_index(cabins, preferred_deck):
    def helper(left, right):
        if left > right:
            return left
        
        mid = (left + right) // 2

        if cabins[mid] == preferred_deck:
            return mid
        elif preferred_deck < cabins[mid]:
            return helper(left, mid - 1)
        else:
            return helper(mid + 1, right)
        
    return helper(0, len(cabins) - 1)

# Problem 3: Count Checked In Passengers
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - Is the list always sorted with all 0s before any 1s?
# - Can the list be empty?

### P - Plan
# 2. Write out in plain English what you want to do:
# - Use binary search to find the index of the first 1.
# - If no 1 exists, return 0.
# - Otherwise, subtract the index of the first 1 from the total length of the list.

# 3. Translate each sub-problem into pseudocode:
# - - Set left = 0 and right = len(rooms) - 1
# - Set first_one = len(rooms)
# - While left <= right:
#     - Find middle index
#     - If rooms[mid] == 1:
#         - first_one = mid
#         - Search left half
#     - Otherwise:
#         - Search right half
# - Return len(rooms) - first_one

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def count_checked_in_passengers(rooms):
    left, right = 0, len(rooms) - 1
    first = len(rooms)

    while left <= right:
        mid = (left + right) // 2

        if rooms[mid] == 1:
            first = mid
            right = mid - 1
        else:
            left = mid + 1

    return len(rooms) - first

# Problem 4: Determining Profitability of Excursions
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - Is excursion_counts always sorted in ascending order?
# - Can the list be empty?

### P - Plan
# 2. Write out in plain English what you want to do:
# - Use binary search to test possible values of x.
# - For each middle index, calculate how many excursions have at least that many passengers.
# - If the count equals the passenger requirement, return it.
# - Otherwise, adjust the search range.
# - If no valid value is found, return -1.

# 3. Translate each sub-problem into pseudocode:
# - Set left = 0 and right = len(excursion_counts) - 1
# - While left <= right:
#     - Find middle index
#     - Let x = len(excursion_counts) - mid
#     - If excursion_counts[mid] >= x and
#       (mid == 0 or excursion_counts[mid - 1] < x):
#         - Return x
#     - If excursion_counts[mid] < x:
#         - Search right half
#     - Else:
#         - Search left half
# - Return -1

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def is_profitable(excursion_counts):
    n = len(excursion_counts)
    l, r = 0, n - 1
    while l <= r:
        m = (l + r) // 2
        x = n - m

        if excursion_counts[m] >= x and (m == 0 or excursion_counts[m - 1] < x):
            return x
        elif excursion_counts[m] < x:
            l = m + 1
        else:
            r = m - 1
    return -1

# Problem 5: Finding the Shallowest Point
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - Can the list of depths be empty?
# - Should the solution use recursion only (divide-and-conquer)?

### P - Plan
# 2. Write out in plain English what you want to do:
# - Split the list into two halves recursively.
# - Find the minimum value in each half.
# - Compare the two minimum values and return the smaller one.
# - If the list contains only one element, return that element.

# 3. Translate each sub-problem into pseudocode:
# - Define helper(left, right):
#     - If left == right, return depths[left]
#     - Find the middle index
#     - Find the minimum in the left half
#     - Find the minimum in the right half
#     - Return the smaller of the two
# - Return helper(0, len(depths) - 1)

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def find_shallowest_point(depths):
    def helper(left, right):
        if left == right:
            return depths[left]

        mid = (left + right) // 2
        left_min = helper(left, mid)
        right_min = helper(mid + 1, right)

        if left_min < right_min:
            return left_min
        return right_min

    return helper(0, len(depths) - 1)
