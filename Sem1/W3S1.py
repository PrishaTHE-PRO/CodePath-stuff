# Problem 1: Post Format Validator
### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
# - Can the input string contain only the characters () [] {} or could it contain other text as well?
# - Should an empty string ("") be considered a valid post format?

### P - Plan
# 2. Write out in plain English what you want to do: 
# - use a stack to keep track of opening tags
# - when we see an opening tag ((,[,{), push it onto the stack
# - when we see a closing tag (), ], }), check if it matched the most recent opening tag
# - if it doesn't match, return False
# - after processing the entier string, return True only if the stack is empty

# 3. Translate each sub-problem into pseudocode:
# - create an empty stack
# - create a dictionary that maps closing tags to their matching opening tags
# - loop through each charcter in the string:
    # - if the charcter is an opening tag:
        # - push it onto the stack
    # - Otherwise, if it is a closing tag:
        # - if the stack is empty, return False
        # - pop the top item from the stack
        # - if it does not match the corresponsing opening tag, return False
    # - after the loop:
        # - if the stack is empty, return True
        # - ortherwise, return False

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def is_valid_post_format(posts):
    stack = []
    matching_tags = {
        ')':'(',
        ']':'[',
        '}':'{'
    }

    for char in posts:
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if not stack:
                return False
            
            top = stack.pop()

            if top != matching_tags[char]:
                return False
            
    return len(stack) == 0


# Problem 2: Reverse User Comments Queue
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - should the original queue be modified or should we return a new revered queue?
# - can the queue be empty?

### P - Plan
# 2. Write out in plain English what you want to do: 
# - use a stack to reverse the order of comments
# - push all comments onto the stack
# - pop them off one by one into a new list
# - return the reversed list

# 3. Translate each sub-problem into pseudocode:
# - create an emoty stack
# - push each comment onto the stack
# - create an emoty result list
# - while the stack is not empty
    # - pop a comment and add it to the result
# - result the result

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def reverse_comments_queue(comments):
    stack = []

    for comment in comments:
        stack.append(comment)

    reverse_comments = []

    while stack:
        reverse_comments.append(stack.pop())

    return reverse_comments

# Problem 3: Check Symmetry in Post Titles
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - Should spaces, puncuation, and capitalization be ignored when checking symmetry?
# - can the title contain number or special characters?

### P - Plan
# 2. Write out in plain English what you want to do: 
# - clean the title by keeping only letters and numbers and converting everything to lowercase.
# - Use two pointers: one at the beginning and one at the end
#- Compare the characters at both pointers
# - If they ever differ, return False
#- If all pairs match, return True

# 3. Translate each sub-problem into pseudocode:
# - create a cleaned version of the title
# - set left = 0 and right = len(cleaned_title) - 1
# - while left < right:
    # - if charcters doen't match, return False
    # - move left right and right left
# - return True

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def is_symmetrical_title(title):
    cleaned = ""

    for char in title:
        if char.isalnum():
            cleaned += char.lower()

    left = 0
    right = len(cleaned) - 1

    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        
        left += 1
        right -= 1

    return True

# Problem 4: Engagment Boost
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - Is the input array always sorted in non-decreasing order?
# - can the array contain both negative and positive numbers?

### P - Plan
# 2. Write out in plain English what you want to do: 
# - Since the array is already sorted, the largest square will come from either the leftmost negative number or the rightmost positive number.
# - Use two pointers, one at the beginning and one at the end.
# - Compare their squares and place the larger square at the end of the result array.
# - Move the corresponding pointer inward and continue until all positions are filled.

# 3. Translate each sub-problem into pseudocode:
# - Create a result array of the same length.
# - Set left = 0 and right = len(engagements) - 1.
# - Fill the result array from right to left:
# - Compare engagements[left]^2 and engagements[right]^2.
# - Place the larger square in the current position.
# - Move the corresponding pointer.
# - Return the result array.

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def engagement_boost(engagements):
    result = [0] * len(engagements)

    left = 0
    right = len(engagements) - 1

    for position in range(len(engagements) - 1, -1, -1):
        left_square = engagements[left] ** 2
        right_square = engagements[right] ** 2

        if left_square > right_square:
            result[position] = left_square
            left += 1
        else:
            result[position] = right_square
            right -= 1

    return result

# Problem 5: Clean Post
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - Can the input string be empty?
# - Should we continue removing pairs until no more adjacent lowercase-uppercase matches remain?

### P - Plan
# 2. Write out in plain English what you want to do:
# - Use a stack to keep track of characters.
# - For each character, compare it with the top of the stack.
# - If they are the same letter but different cases, remove the pair.
# - Otherwise, add the current character to the stack.
# - Join the remaining characters in the stack to form the clean post.

# 3. Translate each sub-problem into pseudocode:
# - Create an empty stack.
# - Loop through each character in the post:
# - If the stack is not empty and the current character forms a bad pair with the top character:
#     - Pop the top character from the stack.
# - Otherwise:
#     - Push the current character onto the stack.
# - Join all characters in the stack into a string.
# - Return the cleaned string.

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:

def clean_post(post):
    stack = []

    for char in post:
        if stack and stack[-1] != char and stack[-1].lower() == char.lower():
            stack.pop()
        else:
            stack.append(char)

    return "".join(stack)