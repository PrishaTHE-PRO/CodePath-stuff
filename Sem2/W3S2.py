# Problem 5: Merge Performance Schedules

### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - Should we always start with a character from schedule1?
# What happens when one schedule is longer than the other?

### P - Plan
# 2. Write out in plain English what you want to do:
# Go through both schedules and alternate characters from each one, then add any leftover characters.

# 3. Translate each sub-problem into pseudocode:
# - Create an empty result
#  Loop through the schedules
# Add a character from schedule1 if available
# Add a character from schedule2 if available
# Return the merged result

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def merge_schedules(schedule1, schedule2):
    result = ""
    max_length = max(len(schedule1), len(schedule2))

    for i in range(max_length):
        if i < len(schedule1):
            result += schedule1[i]

        if i < len(schedule2):
            result += schedule2[i]

    return result

#I picked this problem because it helped me practice working with two strings of different lengths in the same loop.

# Problem 6: Next Greater Event 

### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - Is schedule1 always a subset of schedule2?
# - What should we return if there is no greater value after an event?

### P - Plan
# 2. Write out in plain English what you want to do:
# Use a stack to find the next greater value for each event in schedule2, then use those results for the events in schedule1.

# 3. Translate each sub-problem into pseudocode:
# Create an empty stack and dictionary
# Loop through schedule2
# While the current value is greater than the top of the stack, save it as the next greater value
# Add the current value to the stack
# Give leftover values a next greater value of -1
# Return the values for schedule1

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def next_greater_event(schedule1, schedule2):
    stack = []
    next_greater = {}

    for event in schedule2:
        while stack and event > stack[-1]:
            smaller = stack.pop()
            next_greater[smaller] = event

        stack.append(event)

    while stack:
        next_greater[stack.pop()] = -1

    return [next_greater[event] for event in schedule1]

#I picked this problem because it helped me practice using a stack and dictionary together to find values efficiently.

# Problem 7: Sort Performace by Type 

### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - Should all even numbers come before all odd numbers?
# - Does the order within the even and odd groups matter?

### P - Plan
# 2. Write out in plain English what you want to do:
# Separate the performances into even and odd lists, then combine them with the even performances first.

# 3. Translate each sub-problem into pseudocode:
# Create an even list and an odd list
# Loop through performances
# If the number is even, add it to the even list
# Otherwise, add it to the odd list
# Combine and return both lists\

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def sort_performances_by_type(performances):
    even = []
    odd = []

    for performance in performances:
        if performance % 2 == 0:
            even.append(performance)
        else:
            odd.append(performance)

    return even + odd

#I picked this problem because it helped me practice using loops and conditions to organize values into different groups.