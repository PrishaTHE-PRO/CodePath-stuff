# Problem 6: Task Prioritization with Limited Time

### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - Can the tasks be completed in any order?
# - Does a task count if it finishes exactly at the time limit?

### P - Plan
# 2. Write out in plain English what you want to do:
# Sort the tasks from shortest to longest, then keep completing the shortest tasks until there is not enough time left for the next one.

# 3. Translate each sub-problem into pseudocode:
# Sort the tasks from shortest to longest
# Set the time used and the task count to 0
# Loop through the sorted tasks
# If the task does not fit in the time left, stop
# Otherwise add its duration to the time used and add 1 to the count
# Return the count

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def max_tasks_within_time(tasks, time_limit):
    sorted_tasks = sorted(tasks)
    time_used = 0
    count = 0

    for duration in sorted_tasks:
        if time_used + duration > time_limit:
            break

        time_used += duration
        count += 1

    return count

# Time: O(n log n) where n is the number of tasks, since sorting takes the most time.
# Space: O(n) for the sorted copy of the tasks.

#I picked this problem because it helped me practice sorting first to make a greedy choice easier.

# Problem 7: Frequent Co-working Spaces

### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - If there is a tie, what order should the spaces be returned in?
# - What should we return if the list of visits is empty?

### P - Plan
# 2. Write out in plain English what you want to do:
# Count how many times each space was visited using a dictionary, find the highest count, then return every space with that count.

# 3. Translate each sub-problem into pseudocode:
# Create an empty dictionary
# Loop through the visits and add 1 to the count for each space
# Find the highest count in the dictionary
# Loop through the dictionary and add each space with the highest count to the result
# Return the result

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def most_frequent_spaces(visits):
    counts = {}

    for space in visits:
        counts[space] = counts.get(space, 0) + 1

    if not counts:
        return []

    max_count = max(counts.values())
    result = []

    for space in counts:
        if counts[space] == max_count:
            result.append(space)

    return result

# Time: O(n) where n is the number of visits, since we loop through the visits once and the dictionary once.
# Space: O(n) because the dictionary could hold every visit if all the spaces are different.

#I picked this problem because it helped me practice using a dictionary to count frequencies and handle ties.

# Problem 8: Track Popular Destinations

### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - Are the visits always given in order from earliest to latest?
# - What should we return if the list of visits is empty?

### P - Plan
# 2. Write out in plain English what you want to do:
# Count how many times each destination was visited and save its latest visit date, then pick the destination with the highest count and use the latest visit to break ties.

# 3. Translate each sub-problem into pseudocode:
# Create a dictionary for the counts and a dictionary for the latest visit dates
# Loop through the visits
# Add 1 to the count for the destination
# Update its latest visit if this date is later
# Loop through the destinations
# Keep the one with the highest count, or the later visit if the counts are tied
# Return the destination and its count

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def most_popular_destination(visits):
    counts = {}
    latest_visit = {}

    for destination, date in visits:
        counts[destination] = counts.get(destination, 0) + 1

        if destination not in latest_visit or date > latest_visit[destination]:
            latest_visit[destination] = date

    most_popular = None
    max_count = 0

    for destination in counts:
        if counts[destination] > max_count:
            most_popular = destination
            max_count = counts[destination]
        elif counts[destination] == max_count and latest_visit[destination] > latest_visit[most_popular]:
            most_popular = destination

    return (most_popular, max_count)

# Time: O(n) where n is the number of visits, since we loop through the visits once and the destinations once.
# Space: O(n) because the dictionaries could hold every visit if all the destinations are different.

#I picked this problem because it helped me practice tracking two things in dictionaries and breaking a tie.
