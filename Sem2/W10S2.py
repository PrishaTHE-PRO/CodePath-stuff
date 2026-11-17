# Problem 6: Find Shortest Path (Fix the Bug)

### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - Should the returned path include both the source and the destination?
# - What should we return if there is no path from the source to the destination?

### P - Plan
# 2. Write out in plain English what you want to do:
# The original code has two bugs. First, the path for the source starts as an empty list, so the source is never part of the answer. Second, when adding a neighbor to the queue, it uses [neighbor] as the new path, which throws away every airport visited before it, so the function only returns the last airport. To fix this, start the source's path as [source] and build each neighbor's path as path + [neighbor]. I also mark airports as visited when they are added to the queue instead of when they are popped, so the same airport is not added to the queue more than once.

# 3. Translate each sub-problem into pseudocode:
# Create a queue with (source, [source]) and a visited set with source
# While the queue is not empty:
#   Pop (current, path) from the front of the queue
#   If current is the destination, return path
#   For each neighbor of current in flights (use an empty list if it has none):
#     If the neighbor has not been visited:
#       Add it to visited
#       Add (neighbor, path + [neighbor]) to the queue
# Return an empty list

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
from collections import deque

def find_shortest_path(flights, source, destination):
    queue = deque([(source, [source])])
    visited = {source}

    while queue:
        current, path = queue.popleft()

        if current == destination:
            return path

        for neighbor in flights.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return []

# Time: O(V * (V + E)) where V is the number of airports and E is the number of flights. BFS visits each airport once and checks each flight once, which is O(V + E), but building path + [neighbor] copies a list that can be up to V airports long each time an airport is added to the queue.
# Space: O(V^2) because the queue can hold up to V paths and each path can be up to V airports long, plus O(V) for the visited set.

# Adjacency matrix: Yes, the time complexity would change. With a matrix, finding the neighbors of an airport means checking its whole row of V entries, even if it only has a few flights. Since we do that for every airport, the BFS part becomes O(V^2) instead of O(V + E). This is the same or worse than the adjacency dictionary, and it is a lot worse when the graph is sparse (most airports only have a few flights).

#I picked this problem because it helped me practice reading BFS code carefully and seeing how the path needs to be carried along with each airport in the queue.

# Problem 7: Expanding Flight Offerings

### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - What should we return if flights is empty or has only one airport?
# - Can an airport show up in someone's list without being a key in flights?

### P - Plan
# 2. Write out in plain English what you want to do:
# The airports split into groups (connected components) where every airport in a group can already reach every other airport in that group. To connect all the groups together, we need one new flight between each pair of neighboring groups, so the answer is the number of groups minus 1. To count the groups, loop through every airport, and whenever we find one we have not visited yet, it starts a new group, so we add 1 to the count and use DFS to mark every airport in that group as visited.

# 3. Translate each sub-problem into pseudocode:
# If flights is empty, return 0
# Create an empty visited set and set components to 0
# Define a helper dfs(airport):
#   Add airport to visited
#   For each neighbor of airport in flights (use an empty list if it has none):
#     If the neighbor has not been visited, call dfs(neighbor)
# For each airport in flights:
#   If the airport has not been visited:
#     Add 1 to components
#     Call dfs(airport)
# Return components minus 1

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def min_flights_to_expand(flights):
    if not flights:
        return 0

    visited = set()
    components = 0

    def dfs(airport):
        visited.add(airport)
        for neighbor in flights.get(airport, []):
            if neighbor not in visited:
                dfs(neighbor)

    for airport in flights:
        if airport not in visited:
            components += 1
            dfs(airport)

    return components - 1

# Time: O(V + E) where V is the number of airports and E is the number of flights, since each airport is visited once and each flight is checked once across all the DFS calls.
# Space: O(V) because the visited set holds up to every airport and the recursion can go up to V levels deep.

#I picked this problem because it helped me practice counting connected components in a graph and seeing how that connects to the number of edges needed.

# Problem 8: Get Flight Itinerary

### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - What should we return if there is no path from source to dest?
# - What should we return if source and dest are the same airport?

### P - Plan
# 2. Write out in plain English what you want to do:
# Use BFS from the source airport. Instead of storing the whole path in the queue, keep a dictionary that remembers which airport we came from to reach each airport (its parent). Once we reach the destination, rebuild the path by following the parents backward from dest to source, then reverse it. If BFS finishes without reaching dest, there is no path, so return an empty list.

# 3. Translate each sub-problem into pseudocode:
# Create a queue with source and a parent dictionary with {source: None}
# While the queue is not empty:
#   Pop current from the front of the queue
#   If current is dest:
#     Create an empty path list
#     While current is not None:
#       Add current to path and set current to parent[current]
#     Return path reversed
#   For each neighbor of current in flights (use an empty list if it has none):
#     If the neighbor is not in parent:
#       Set parent[neighbor] to current and add neighbor to the queue
# Return an empty list

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def get_itinerary(flights, source, dest):
    queue = deque([source])
    parent = {source: None}

    while queue:
        current = queue.popleft()

        if current == dest:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            return path[::-1]

        for neighbor in flights.get(current, []):
            if neighbor not in parent:
                parent[neighbor] = current
                queue.append(neighbor)

    return []

# Time: O(V + E) where V is the number of airports and E is the number of flights, since BFS visits each airport once and checks each flight once, and rebuilding the path takes at most O(V).
# Space: O(V) because the parent dictionary, the queue, and the path can each hold up to every airport.

#I picked this problem because it helped me practice path reconstruction with a parent dictionary, which is more efficient than copying the whole path for every airport like in the bug fix problem.
