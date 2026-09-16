# Problem 1: Can Rebook Flight

### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - Is the graph directed since flights only go from i to j?
# - Do we need to find any path, not necessarily a direct flight?

### P - Plan
# 2. Write out in plain English what you want to do:
# - Use DFS to explore possible flights from the source.
# - Mark visited locations to avoid checking the same flight multiple times.
# - If we reach the destination, return True.
# - If all paths are explored without reaching the destination, return False.

# 3. Translate each sub-problem into pseudocode:
# - Create a visited set.
# - Define DFS function:
#     - If current location is destination, return True.
#     - Mark current location as visited.
#     - Check all possible flights from current location.
#         - If a flight exists and destination is not visited:
#             - Recursively search that location.
#     - Return False if no path exists.
# - Call DFS on source.

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:

def can_rebook(flights, source, dest):
    visited = set()

    def dfs(city):
        if city == dest:
            return True
        
        visited.add(city)

        for next_city in range(len(flights)):
            if flights[city][next_city] == 1 and next_city not in visited:
                if dfs(next_city):
                    return True
        
        return False

    return dfs(source)

# Problem 2: Can Rebook Flight II (BFS)

### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - Is the graph directed?
# - Can we use BFS to explore all possible flight paths?

### P - Plan
# 2. Write out in plain English what you want to do:
# - Use BFS with a queue to explore flights level by level.
# - Keep track of visited locations.
# - If we reach the destination, return True.
# - If the queue is empty, return False.

# 3. Translate each sub-problem into pseudocode:
# - Create queue with source.
# - Create visited set.
# - While queue is not empty:
#     - Remove a location.
#     - If it is the destination, return True.
#     - Add unvisited connected locations to the queue.
# - Return False.

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:

from collections import deque

def can_rebook(flights, source, dest):
    queue = deque([source])
    visited = set([source])

    while queue:
        city = queue.popleft()

        if city == dest:
            return True

        for next_city in range(len(flights)):
            if flights[city][next_city] == 1 and next_city not in visited:
                visited.add(next_city)
                queue.append(next_city)

    return False

# Problem 3: Number of Flights

### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - Do we need the shortest path between two airports?
# - Should we return -1 if no path exists?

### P - Plan
# 2. Write out in plain English what you want to do:
# - Use BFS because it finds the shortest path in an unweighted graph.
# - Track the number of flights taken.
# - Return the count when we reach the destination.

# 3. Translate each sub-problem into pseudocode:
# - Create a queue with (starting airport, number of flights).
# - Mark start as visited.
# - While queue is not empty:
#     - Remove an airport.
#     - If it is destination, return flights taken.
#     - Add unvisited connected airports with count + 1.
# - Return -1 if destination is unreachable.

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:

from collections import deque

def counting_flights(flights, i, j):
    queue = deque([(i, 0)])
    visited = set([i])

    while queue:
        airport, count = queue.popleft()

        if airport == j:
            return count

        for next_airport in range(len(flights)):
            if flights[airport][next_airport] == 1 and next_airport not in visited:
                visited.add(next_airport)
                queue.append((next_airport, count + 1))

    return -1

# Problem 4: Number of Airline Regions

### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - Is each region a connected group of airports?
# - Do we need to count every separate connected component?

### P - Plan
# 2. Write out in plain English what you want to do:
# - Use DFS to explore each connected region.
# - Keep track of visited airports.
# - Each time we find an unvisited airport, it starts a new region.
# - Count the number of DFS searches.

# 3. Translate each sub-problem into pseudocode:
# - Create visited set and count = 0.
# - For each airport:
#     - If it is not visited:
#         - Run DFS to visit all connected airports.
#         - Increase region count.
# - Return count.

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:

def num_airline_regions(is_connected):
    visited = set()

    def dfs(airport):
        visited.add(airport)

        for neighbor in range(len(is_connected)):
            if is_connected[airport][neighbor] == 1 and neighbor not in visited:
                dfs(neighbor)

    regions = 0

    for airport in range(len(is_connected)):
        if airport not in visited:
            dfs(airport)
            regions += 1

    return regions

# Problem 5: Get Flight Cost

### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - Do we need the cheapest path or any valid path?
# - Should we return -1 if no route exists?

### P - Plan
# 2. Write out in plain English what you want to do:
# - Use DFS to explore possible flight paths.
# - Track the total cost as we travel.
# - Return the cost when we reach the destination.
# - If no path exists, return -1.

# 3. Translate each sub-problem into pseudocode:
# - Create visited set.
# - DFS(current, cost):
#     - If current == destination, return cost.
#     - Mark current as visited.
#     - For each (neighbor, price):
#         - If neighbor is not visited:
#             - Recursively search neighbor.
#     - Return -1 if no path found.
# - Call DFS(start, 0).

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:

def calculate_cost(flights, start, dest):
    visited = set()

    def dfs(city, cost):
        if city == dest:
            return cost

        visited.add(city)

        for neighbor, price in flights.get(city, []):
            if neighbor not in visited:
                result = dfs(neighbor, cost + price)
                if result != -1:
                    return result

        return -1

    return dfs(start, 0)