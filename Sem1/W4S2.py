# Problem 1: Planning Your Daily Work Schedule
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - should the function return a boolean value?
# - can the same task be used twice to form the target time?

### P - Plan
# 2. Write out in plain English what you want to do:
# - use a set to track tast times already seen
# - for each task, check if its complement exists in the set

# 3. Translate each sub-problem into pseudocode:
# - create an empty set
# - for each time in task_time:
# - complement = available_time - time
# - if complement is in seen:
# - return True 
# - add time to seen
# - return False

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def find_task_pair(task_times, available_time):
    seen = set()

    for time in task_times:
        complement = available_time - time
        if complement in seen:
            return True
        seen.add(time)

    return False

# Problem 2: Minimizing Workload Gaps
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - are the work sessions already sorted by start time?
# - should the gap be measured in mins?

### P - Plan
# 2. Write out in plain English what you want to do:
# - compare each session's end tiem with the next session's start time
# - keep track of the smallest gap found

# 3. Translate each sub-problem into pseudocode:
# - set samllest_gap to infinity
# - for i from 0 to len of work_sessions - 1:
# - current_end = end time of curr sessiont
# - gap = next_start - current_end
# - update smallest_gap if gap is smaller
# - return smallest_gap

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def find_smallest_gap(work_sessions):
    smallest_gap = float("inf")

    for i in range(len(work_sessions) - 1):
        current_end = work_sessions[i][1]
        next_start = work_sessions[i+1][0]

        current_end_minutes = (current_end // 100) * 60 + (current_end % 100)
        next_start_minutes = (next_start // 100) * 60 + (next_start % 100)

        gap = next_start_minutes - current_end_minutes
        smallest_gap = min(smallest_gap, gap)

    return smallest_gap

# Problem 3: Expense Tracking and Categorization
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - Should the function return both the totals dictionary and the highest-spending category?
# - Can a category appear multiple times in the expense list?

### P - Plan
# 2. Write out in plain English what you want to do:
# - Sum the expenses for each category using a dictionary
# - Find the category with the highest total expense and return both results

# 3. Translate each sub-problem into pseudocode:
# - create an empty dict 
# - for each (category, amount) in expenses:
# - totals[category] = totals.get(category,0) + amount
# - set highest_category to the category with the largest value in totals
# - return totals and highest_category

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def calculate_expenses(expenses):
    totals = {}

    for category, amount in expenses:
        totals[category] = totals.get(category, 0) + amount

    highest_category = max(totals, key=totals.get)

    return totals, highest_category

# Problem 4: Analyzing Word Frequency
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - Should capitalization and punctuation be ignored?
# - Should all words tied for the highest frequency be returned?

### P - Plan
# 2. Write out in plain English what you want to do:
# - Clean the text and count how often each word appears
# - Find and return the word(s) with the highest frequency

# 3. Translate each sub-problem into pseudocode:
# - Convert text to lowercase
# - Remove punctuation from text
# - Split text into words
# - Create an empty dictionary called word_counts
# - For each word:
# - word_counts[word] = word_counts.get(word, 0) + 1
# - Find the maximum frequency
# - Create a list of words whose frequency equals the maximum
# - Return word_counts and the list of most frequent words

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
import string

def word_frequency_analysis(text):
    text = text.lower()

    for char in string.punctuation:
        text = text.replace(char, "")

    words = text.split()

    word_counts = {}

    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    max_frequency = max(word_counts.values())

    most_frequent = []

    for word, count in word_counts.items():
        if count == max_frequency:
            most_frequent.append(word)

    return word_counts, most_frequent

# Problem 5: Validating HTML Tags
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - Are we guaranteed that tags are always properly formatted (no malformed strings like <div or missing >)?
# - Can we assume only simple opening <tag> and closing </tag> pairs with no attributes?

### P - Plan
# 2. Write out in plain English what you want to do:
# - Use a stack to track opening tags
# - Push opening tags onto the stack
# - For closing tags, check if they match the most recent opening tag
# - If everything matches and stack is empty at the end, the HTML is valid

# 3. Translate each sub-problem into pseudocode:
# - Create an empty stack
# - Parse the string into tags
# - For each tag:
# - If it is an opening tag:
    # - push tag name onto stack
# - Else if it is a closing tag:
    # - If stack is empty → return False
    # - If top of stack != tag name → return False
    # - Pop stack
# - If stack is empty:
# - return True
# - Else:
# - return False

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def validate_html_tags(html):
    stack = []
    i = 0

    while i < len(html):
        if html[i] == "<":
            j = i + 1

            while html[j] != ">":
                j += 1

            tag = html[i + 1:j]

            if not tag.startswith("/"):
                # opening tag
                stack.append(tag)
            else:
                # closing tag
                tag_name = tag[1:]
                if not stack or stack[-1] != tag_name:
                    return False
                stack.pop()

            i = j + 1
        else:
            i += 1

    return len(stack) == 0