# Problem 1: Counting Iron Man's Suits
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - Can the list of suits be empty?
# - Should the recursive solution avoid using len() as well?

### P - Plan
# 2. Write out in plain English what you want to do:
# - Iterative: Loop through the list and increment a counter for each suit.
# - Recursive: If the list is empty, return 0. Otherwise, return 1 plus the count of the remaining suits.

# 3. Translate each sub-problem into pseudocode:
# - - Iterative:
#   - Set count = 0
#   - For each suit in suits:
#       - count += 1
#   - Return count
#
# - Recursive:
#   - If suits is empty, return 0
#   - Return 1 + count_suits_recursive(suits[1:])

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def count_suits_iterative(suits):
    res = 0
    for suit in suits:
        res += 1
    return res

def count_suits_recursive(suits):
    if not suits:
        return 0
    return 1 + count_suits_recursive(suits[1:])

# Problem 2: Collecting Infinity Stones
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - Can the list of stones be empty?
# - Should the function use recursion only (no loops)?

### P - Plan
# 2. Write out in plain English what you want to do:
# - If the list is empty, return 0.
# - Otherwise, return the first stone's power plus the sum of the remaining stones recursively.

# 3. Translate each sub-problem into pseudocode:
# - If stones is empty, return 0
# - Return stones[0] + sum_stones(stones[1:])

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def sum_stones(stones):
    if not stones:
        return 0
    return stones[0] + sum_stones(stones[1:])

# Problem 3: Counting Iron Man's Unique Suits
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - can the lsit be empty?
# - should 2 suits with the same name count as one distinct suit?

### P - Plan
# 2. Write out in plain English what you want to do:
# - Iterative: loop through the lsit, add each suit to a set, then return the size of the set
# - recursive: Recursively process the list, adding each suit to a set until the list is empty, then return the size of the set.

# 3. Translate each sub-problem into pseudocode:
# - Iterative:
#   - Create an empty set
#   - For each suit in suits:
#       - Add suit to the set
#   - Return the size of the set
#
# - Recursive:
#   - Create an empty set
#   - Define a helper function(index):
#       - If index == length of suits, return
#       - Add suits[index] to the set
#       - helper(index + 1)
#   - Call helper(0)
#   - Return the size of the set

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def count_suits_iterative(suits):
    seen = set()

    for suit in suits:
        seen.add(suit)
    
    return len(seen)

def count_suits_recursive(suits):
    unique = set()

    def helper(index):
        if index == len(suits):
            return
        unique.add(suits[index])
        helper(index + 1)

    helper(0)
    return len(unique)

# Problem 4: Calculating Groot's Growth
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - is n always a non-negative int?
# - shoul the fuct return the nth Fibonacci # using recrsior only?

### P - Plan
# 2. Write out in plain English what you want to do:
# - if n is 0 or 1, return n
# - otehrwise, recursively return the sume of the prev two Fib #s

# 3. Translate each sub-problem into pseudocode:
# - if n == 0, ret 0
# - if n == 1, ret 1
# - return fibonacci_growth(n - 1) + fibonacci_growth(n - 2)
# - O(2^n) (n = # of months)

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def fibonacci_growth(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_growth(n - 1) + fibonacci_growth(n - 2)

# Problem 5: Calculating the Power of the Fantastic Four
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - is n always an int?
# - should the func handle both pos and negative exponents recursively?

### P - Plan
# 2. Write out in plain English what you want to do:
# - if n is 0, return 1
# - if n is pos, return 4 multiplied by 4 raised to the (n - 1) power
# - if n is neg, return 1 divided by 4 to the absolue value of n

# 3. Translate each sub-problem into pseudocode:
# - if n == 0, return 1
# - if n > 0, return 4 * power_of_four(n - 1)
# - otherwise, return 1 / power_of_four(-n)
# - 0(n)

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def power_of_four(n):
    if n == 0:
        return 1
    if n > 0:
        return 4 * power_of_four(n - 1)
    return 1 / power_of_four(-n)
