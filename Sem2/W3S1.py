# Problem 6: Post Editor 

### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - Should spaces stay in the same order?
# - Should punctuation be reversed with the word?

### P - Plan
# 2. Write out in plain English what you want to do:
# Split the post into words, reverse each word using a queue, and join the words back together.

# 3. Translate each sub-problem into pseudocode:
# Split post into words
# For each word, add its characters to a queue
# Remove characters from the queue and build the reversed word
# Add each reversed word to the result
# Return the result

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
from collections import deque

def edit_post(post):
    words = post.split()
    result = []

    for word in words:
        queue = deque(word)
        reversed_word = ""

        while queue:
            reversed_word += queue.pop()

        result.append(reversed_word)

    return " ".join(result)

# I picked this problem because it gave me a simple way to practice using queues while also working with strings.

# Problem 7: Post Compare

### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - Does # always represent one backspace?
# - What happens if # is used when the text is already empty?

### P - Plan
# 2. Write out in plain English what you want to do:
# Process both drafts using a stack to handle backspaces, then compare the final strings.

# 3. Translate each sub-problem into pseudocode:
# Create an empty stack
# Go through each character in the draft
# If it is #, remove the last character if possible
# Otherwise, add the character to the stack
# Process both drafts and compare their results

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def post_compare(draft1, draft2):
    def process(draft):
        stack = []

        for char in draft:
            if char == "#":
                if stack:
                    stack.pop()
            else:
                stack.append(char)

        return stack

    return process(draft1) == process(draft2)

# I picked this problem because it helped me practice using stacks in a practical string problem.

# Problem 5: Content Cleaner 

### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - Do the opposite-case letters have to be directly next to each other?
# - should we keep removing pairs until no more can be removed?

### P - Plan
# 2. Write out in plain English what you want to do:
# Use a stack to keep track of characters and remove letters when the top of the stack is the same letter with the opposite case.

# 3. Translate each sub-problem into pseudocode:
# Create an empty stack
# Loop through each character
# Check if it matches the top character but has the opposite case
# If it does, remove the top character
# Otherwise, add the character to the stack
# Join and return the stack

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

#I picked this problem because it helped me practice using a stack to remove matching characters efficiently.