# Problem 1: Manage Performance Stage Changes
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - What should we do if Cancel is called but nothing is scheduled?
# - What should we do if Reschedule is called but nothing was canceled?

### P - Plan
# 2. Write out in plain English what you want to do:
# - Use two stacks: scheduled and canceled.
# - Schedule adds to scheduled.
# - Cancel moves last scheduled → canceled.
# - Reschedule moves last canceled → scheduled.
# - Return scheduled list.

# 3. Translate each sub-problem into pseudocode:
# - scheduled = [], canceled = []
# - for action in changes:
#     - if "Schedule": push X
#     - if "Cancel": move scheduled[-1] → canceled
#     - if "Reschedule": move canceled[-1] → scheduled
# - return scheduled

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:

def manage_stage_changes(changes):
    scheduled, canceled = [], []

    for action in changes:
        if action.startswith("Schedule"):
            scheduled.append(action.split()[1])

        elif action == "Cancel" and scheduled:
            canceled.append(scheduled.pop())

        elif action == "Reschedule" and canceled:
            scheduled.append(canceled.pop())

    return scheduled

# Problem 2: Queue of  Performance Requests
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - If two requests have the same priority, do we process them in arrival order?
# - Are priorities always positive integers, and is a larger number higher priority?

### P - Plan
# 2. Write out in plain English what you want to do:
# - We receive a list of (priority, performance) tuples.
# - Higher priority numbers should be processed first.
# - If priorities tie, keep original order (stable sort).
# - Sort requests by priority descending.
# - Return only performance names in sorted order.

# 3. Translate each sub-problem into pseudocode:
# - Sort requests by priority (descending)
# - Extract performance names in that order
# - Return result list

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:

def process_performance_requests(requests):
    requests.sort(key=lambda x: x[0], reverse=True)
    return [name for _, name in requests]

# Problem 3: Collect Points at Festival Points
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - Do we need to simulate actual stack operations, or just sum values?
# - Are booth points always positive integers?

### P - Plan
# 2. Write out in plain English what you want to do:
# - Use a stack to store all booth points.
# - Pop each value and add it to a running total.
# - Return the total points collected.

# 3. Translate each sub-problem into pseudocode:
# - stack = points
# - total = 0
# - while stack not empty:
#     - pop value
#     - add to total
# - return total

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:

def collect_festival_points(points):
    stack = points[:]
    total = 0

    while stack:
        total += stack.pop()

    return total

# Problem 4: Festival Booth Navigation
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - If "back" is called when there is nothing to backtrack, what should happen?
# - Should we assume booth numbers are always valid integers?

### P - Plan
# 2. Write out in plain English what you want to do:
# - Use a stack to track visited booths.
# - If we see a number, add it to the stack.
# - If we see "back", remove the most recent booth (if any).
# - Return the final stack as the path taken.

# 3. Translate each sub-problem into pseudocode:
# - stack = []
# - for clue in clues:
#     - if clue is number: push to stack
#     - else if clue == "back": pop from stack if not empty
# - return stack

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:

def booth_navigation(clues):
    stack = []

    for clue in clues:
        if clue == "back":
            if stack:
                stack.pop()
        else:
            stack.append(clue)

    return stack

# Problem 5: Merge Performance Schedules
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - If one schedule is longer, should we directly append the remaining characters in order?
# - Are schedules always lowercase strings with no spaces?

### P - Plan
# 2. Write out in plain English what you want to do:
# - Use two pointers to traverse both strings.
# - Alternately pick characters from schedule1 and schedule2.
# - Once one string ends, append the rest of the other string.
# - Return the merged string.

# 3. Translate each sub-problem into pseudocode:
# - i = 0, j = 0
# - result = []
# - while i < len(schedule1) or j < len(schedule2):
#     - if i < len(schedule1): add schedule1[i], i++
#     - if j < len(schedule2): add schedule2[j], j++
# - join result and return

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:

def merge_schedules(schedule1, schedule2):
    i, j = 0, 0
    result = []

    while i < len(schedule1) or j < len(schedule2):
        if i < len(schedule1):
            result.append(schedule1[i])
            i += 1
        if j < len(schedule2):
            result.append(schedule2[j])
            j += 1

    return "".join(result)