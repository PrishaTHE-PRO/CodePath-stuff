# Problem 6: Get All Destinations

### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - Should the starting location be included in the list we return?
# - What should we do if a destination shows up as a neighbor but is not a key in the flights dictionary?

### P - Plan
# 2. Write out in plain English what you want to do:
# Use breadth first search starting from the start airport. A queue lets us visit every airport that is one flight away before any airport that is two flights away, so the result ends up in order of how many layovers are needed. Keep a visited set so we never add the same airport twice, even when there are cycles like Tokyo and Sydney.

# 3. Translate each sub-problem into pseudocode:
# Create a queue with start, a visited set with start, and an empty result list
# While the queue is not empty:
#   Pop an airport from the front of the queue and add it to result
#   For each neighbor of that airport in flights (use an empty list if it has none):
#     If the neighbor has not been visited:
#       Add it to visited and add it to the queue
# Return result

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
from collections import deque

def get_all_destinations(flights, start):
    queue = deque([start])
    visited = {start}
    result = []

    while queue:
        airport = queue.popleft()
        result.append(airport)

        for neighbor in flights.get(airport, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return result

# Time: O(V + E) where V is the number of airports and E is the number of flights, since each airport is added to the queue once and each flight is checked once.
# Space: O(V) because the visited set, the queue, and the result list can each hold up to every airport.

#I picked this problem because it helped me practice breadth first search on a graph and using a visited set to handle cycles.

# Problem 7: Get All Destinations II

### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - Should we visit the neighbors in the same order they appear in the list for each airport?
# - What should we do if an airport like New York has no entry in the flights dictionary?

### P - Plan
# 2. Write out in plain English what you want to do:
# Use depth first search starting from the start airport. When we visit an airport, add it to the result and mark it as visited, then go as deep as possible through its first unvisited neighbor before moving on to the next one. The visited set stops us from going around cycles forever.

# 3. Translate each sub-problem into pseudocode:
# Create an empty visited set and an empty result list
# Define a helper dfs(airport):
#   Add airport to visited and to result
#   For each neighbor of airport in flights (use an empty list if it has none):
#     If the neighbor has not been visited, call dfs(neighbor)
# Call dfs(start)
# Return result

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def get_all_destinations_dfs(flights, start):
    visited = set()
    result = []

    def dfs(airport):
        visited.add(airport)
        result.append(airport)

        for neighbor in flights.get(airport, []):
            if neighbor not in visited:
                dfs(neighbor)

    dfs(start)
    return result

# Time: O(V + E) where V is the number of airports and E is the number of flights, since each airport is visited once and each flight is checked once.
# Space: O(V) because the visited set and result list hold up to every airport, and the recursion can go up to V levels deep.

#I picked this problem because it helped me practice depth first search and compare how its visiting order is different from breadth first search.

# Problem 8: Find Itinerary

### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - What should we return if the list of boarding passes is empty?
# - Can we assume there is exactly one flight leaving each airport except the final destination?

### P - Plan
# 2. Write out in plain English what you want to do:
# Build a dictionary that maps each departure airport to its arrival airport. The first airport of the trip is the one that is a departure but never an arrival, since no flight lands there. Starting from that airport, keep following the dictionary to the next airport and add each one to the itinerary until we reach an airport with no departing flight, which is the final destination.

# 3. Translate each sub-problem into pseudocode:
# If boarding_passes is empty, return an empty list
# Create a dictionary flights mapping each departure to its arrival
# Create a set of all arrival airports
# Find the departure airport that is not in the arrivals set and call it current
# Create an itinerary list with current
# While current is a key in flights:
#   Set current to flights[current]
#   Add current to itinerary
# Return itinerary

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def find_itinerary(boarding_passes):
    if not boarding_passes:
        return []

    flights = {}
    arrivals = set()
    for departure, arrival in boarding_passes:
        flights[departure] = arrival
        arrivals.add(arrival)

    current = None
    for departure in flights:
        if departure not in arrivals:
            current = departure
            break

    itinerary = [current]
    while current in flights:
        current = flights[current]
        itinerary.append(current)

    return itinerary

# Time: O(n) where n is the number of boarding passes, since we build the dictionary and set in one pass, find the start in one pass, and follow each flight once.
# Space: O(n) because the dictionary, the arrivals set, and the itinerary each hold about n airports.

#I picked this problem because it helped me practice turning a list of edges into an adjacency dictionary and finding the starting node of a path.
