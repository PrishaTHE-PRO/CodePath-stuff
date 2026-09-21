# Problem 9: Stage Arrangement Difference Between Two Performances

### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - Will every performer in s also appear exactly once in t?
# - Do we need to add the index differences for every performer in the lists?

### P - Plan
# 2. Write out in plain English what you want to do:
# Go through each performer in s, find where that same performer is in t,
# find the absolute difference between their two indexes, and add all
# of the differences together.

# 3. Translate each sub-problem into pseudocode:
# Set total difference to 0
# Loop through every index in s:
#     Find the index of the same performer in t
#     Find the absolute difference between the two indexes
#     Add the difference to the total
# Return the total difference

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:

def find_stage_arrangement_difference(s, t):
    total_difference = 0

    for i in range(len(s)):
        performer = s[i]
        t_index = t.index(performer)
        total_difference += abs(i - t_index)

    return total_difference


s1 = ["Alice", "Bob", "Charlie"]
t1 = ["Bob", "Alice", "Charlie"]
s2 = ["Alice", "Bob", "Charlie", "David", "Eve"]
t2 = ["Eve", "David", "Bob", "Alice", "Charlie"]

print(find_stage_arrangement_difference(s1, t1))
print(find_stage_arrangement_difference(s2, t2))

# I picked this problem because it seemed like a good way to practice working with lists, indexes, loops, and absolute values in Python.

# Problem 10: VIP Passes and Guests
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - Can the same type of guest appear more than once in guests?
# - Are uppercase and lowercase letters considered different guest types?

### P - Plan
# 2. Write out in plain English what you want to do:
# Create a set containing all the VIP guest types.
# Then go through each guest and check if they are in the VIP set.
# If they are, add 1 to the count.

# 3. Translate each sub-problem into pseudocode:
# Create an empty set called vip_set
# Loop through vip_passes and add each character to vip_set
# Set count to 0
# Loop through each character in guests:
#     If the character is in vip_set:
#         Add 1 to count
# Return count

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:

def num_VIP_guests(vip_passes, guests):
    vip_set = set()

    for char in vip_passes:
        vip_set.add(char)

    count = 0

    for char in guests:
        if char in vip_set:
            count += 1

    return count


vip_passes1 = "aA"
guests1 = "aAAbbbb"

vip_passes2 = "z"
guests2 = "ZZ"

print(num_VIP_guests(vip_passes1, guests1))
print(num_VIP_guests(vip_passes2, guests2))

# I picked this problem because I wanted to practice using sets and checking whether an element exists in a set.

# Problem 12: Sort the Performers
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - Will performer_names and performance_times always have the same length?
# - Are all the performance times unique?

### P - Plan
# 2. Write out in plain English what you want to do:
# Match each performer with their performance time.
# Sort the performers based on their performance times from largest to smallest.
# Then return just the performer names in that sorted order.

# 3. Translate each sub-problem into pseudocode:
# Create an empty list to store performer and time pairs
# Loop through each index:
#     Add the performance time and performer name as a pair
# Sort the list of pairs in descending order
# Create an empty list for the sorted names
# Loop through the sorted pairs:
#     Add each performer name to the sorted names list
# Return the sorted names list

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:

def sort_performers(performer_names, performance_times):
    """
    :type performer_names: List[str]
    :type performance_times: List[int]
    :rtype: List[str]
    """
    performers = []

    for i in range(len(performer_names)):
        performers.append((performance_times[i], performer_names[i]))

    performers.sort(reverse=True)

    sorted_names = []

    for time, name in performers:
        sorted_names.append(name)

    return sorted_names


performer_names1 = ["Mary", "John", "Emma"]
performance_times1 = [180, 165, 170]

performer_names2 = ["Alice", "Bob", "Bob"]
performance_times2 = [155, 185, 150]

print(sort_performers(performer_names1, performance_times1))
print(sort_performers(performer_names2, performance_times2))