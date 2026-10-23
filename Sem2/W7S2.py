# Problem 5: Finding the Shallowest Point

### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - What should we return if the depths list is empty?
# - Can depths be negative, or are they always positive numbers?

### P - Plan
# 2. Write out in plain English what you want to do:
# Split the list in half, find the shallowest point in each half by calling the same function on each half, then compare the two results and return the smaller one. A list with one depth is its own shallowest point.

# 3. Translate each sub-problem into pseudocode:
# If the list has only one depth, return that depth
# Find the middle index of the list
# Set left_min to the result of calling the function on the left half
# Set right_min to the result of calling the function on the right half
# If left_min is less than right_min, return left_min
# Otherwise return right_min

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def find_shallowest_point(depths):
    if len(depths) == 1:
        return depths[0]

    mid = len(depths) // 2
    left_min = find_shallowest_point(depths[:mid])
    right_min = find_shallowest_point(depths[mid:])

    if left_min < right_min:
        return left_min

    return right_min

# Time: O(n log n) where n is the number of depths, since the list is split log n times and each level of splitting copies a total of n elements through slicing.
# Space: O(n) because the slices at each level add up to n elements and the recursion goes log n levels deep.

#I picked this problem because it helped me practice divide and conquer by splitting a list in half and combining the answers from each half.

# Problem 6: Cruise Ship Treasure Hunt

### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - Can the same room number appear more than once in the grid, and if so which one should we return?
# - What should we return if the matrix is empty?

### P - Plan
# 2. Write out in plain English what you want to do:
# Start at the top right corner of the grid. Since rows go up to the right and columns go up going down, if the current room is bigger than the treasure we can throw away the whole column and move left. If it is smaller we can throw away the whole row and move down. Keep going until we find the treasure or run off the grid.

# 3. Translate each sub-problem into pseudocode:
# If the matrix is empty, return (-1, -1)
# Set row to 0 and col to the last column index
# While row is inside the grid and col is at least 0
# If the current room equals the treasure, return (row, col)
# If the current room is greater than the treasure, move col left by 1
# Otherwise move row down by 1
# Return (-1, -1)

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def find_treasure(matrix, treasure):
    if not matrix or not matrix[0]:
        return (-1, -1)

    row = 0
    col = len(matrix[0]) - 1

    while row < len(matrix) and col >= 0:
        current = matrix[row][col]

        if current == treasure:
            return (row, col)

        if current > treasure:
            col -= 1
        else:
            row += 1

    return (-1, -1)

# Time: O(m + n) where m is the number of rows and n is the number of columns, since every step removes either one row or one column from consideration.
# Space: O(1) because we only keep track of the current row and column.

#I picked this problem because it helped me see how the sorted rows and columns let us eliminate a whole row or column with one comparison.

# Problem 3: Sqrt(x)

### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - What should we return if x is 0 or 1?
# - Can x be a very large number, so we should avoid checking every integer one by one?

### P - Plan
# 2. Write out in plain English what you want to do:
# Binary search between 0 and x for the largest integer whose square is less than or equal to x. Each step pick the middle number, square it by multiplying it by itself, and compare it to x to decide which half to keep.

# 3. Translate each sub-problem into pseudocode:
# If x is less than 2, return x
# Set left to 1 and right to x // 2
# Set answer to 0
# While left is less than or equal to right
# Set mid to the middle of left and right
# If mid times mid equals x, return mid
# If mid times mid is less than x, save mid as the answer and move left to mid + 1
# Otherwise move right to mid - 1
# Return answer

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def my_sqrt(x):
    if x < 2:
        return x

    left = 1
    right = x // 2
    answer = 0

    while left <= right:
        mid = (left + right) // 2
        square = mid * mid

        if square == x:
            return mid

        if square < x:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    return answer

# Time: O(log x) where x is the input number, since each step of the binary search cuts the range of possible answers in half.
# Space: O(1) because we only keep track of a few integer variables.

#I picked this problem because it helped me practice using binary search on a range of numbers instead of on a list.
