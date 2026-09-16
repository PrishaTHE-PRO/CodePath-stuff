# Problem 1:

### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - Is the graph directed or undirected?
# - How should the graph be represented (adjacency list, adjacency dictionary, etc.)?

### P - Plan
# 2. Write out in plain English what you want to do:
# - Create a dictionary where each airport is a key.
# - Store a list of all directly connected airports as the value for each key.
# - Since the graph is undirected, every connection should appear in both airports' lists.

# 3. Translate each sub-problem into pseudocode:
# - Create an empty dictionary called flights.
# - Add each airport as a key.
# - For each airport, assign a list of its neighboring airports.
# - Return the completed dictionary.

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
flights = {
    "JFK": ["LAX", "DFW"],
    "LAX": ["JFK"],
    "DFW": ["JFK", "ATL"],
    "ATL": ["DFW"]
}

# Problem 2:

### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - Is the graph represented as an adjacency list?
# - Should every flight from destination i to destination j have a corresponding flight from j to i?

### P - Plan
# 2. Write out in plain English what you want to do:
# - Visit each destination in the graph.
# - For every flight from destination i to destination j, check whether i also appears in j's list of flights.
# - If any flight is missing its reverse flight, return False.
# - If all flights have matching reverse flights, return True.

# 3. Translate each sub-problem into pseudocode:
# - For each destination i:
#     - For each neighboring destination j in flights[i]:
#         - If i is not in flights[j]:
#             - Return False
# - Return True

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def bidirectional_flights(flights):
    for i in range(len(flights)):
        for j in flights[i]:
            if i not in flight_sets[j]:
                return False
    return True

# Problem 3: 

### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - Is the graph represented as an adjacency matrix where 1 means there is a flight?
# - Should we return only destinations directly connected to the source (not destinations reachable through multiple flights)?

### P - Plan
# 2. Write out in plain English what you want to do:
# - Look at the row in the matrix that represents the source destination.
# - Check every value in that row.
# - If the value is 1, add that destination's index to the result list.
# - Return the list of destinations with direct flights from the source.

# 3. Translate each sub-problem into pseudocode:
# - Create an empty list called direct_flights.
# - Loop through every destination index in flights[source].
#     - If flights[source][destination] == 1:
#         - Add destination to direct_flights.
# - Return direct_flights.

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:

def get_direct_flights(flights, source):
    direct_flights = []

    for destination in range(len(flights[source])):
        if flights[source][destination] == 1:
            direct_flights.append(destination)

    return direct_flights


# Example Usage
flights = [
    [0, 1, 1, 0],
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 0, 0, 0]
]

print(get_direct_flights(flights, 2))
print(get_direct_flights(flights, 3))

# Problem 4: Converting Flight Representations

### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - Are all flights bidirectional?
# - Should each city store a list of its connected cities?

### P - Plan
# 2. Write out in plain English what you want to do:
# - Create a dictionary where each city is a key.
# - Add connected cities to each city's list.
# - Since flights are bidirectional, add both directions.

# 3. Translate each sub-problem into pseudocode:
# - Create empty dictionary adj_dict.
# - For each flight [a, b]:
#     - Add a and b as keys if missing.
#     - Add b to a's list and a to b's list.
# - Return adj_dict.

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:

def get_adj_dict(flights):
    adj_dict = {}

    for a, b in flights:
        if a not in adj_dict:
            adj_dict[a] = []
        if b not in adj_dict:
            adj_dict[b] = []

        adj_dict[a].append(b)
        adj_dict[b].append(a)

    return adj_dict

# Problem 5: Find Center of Airport

### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - Is there only one center node in the star graph?
# - Does the center node appear in every edge?

### P - Plan
# 2. Write out in plain English what you want to do:
# - In a star graph, the center is connected to every other node.
# - The center must appear in the first two edges.
# - Compare the first two edges and return the shared node.

# 3. Translate each sub-problem into pseudocode:
# - Get first edge.
# - Get second edge.
# - Check which node appears in both edges.
# - Return that node.

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:

def find_center(terminals):
    if terminals[0][0] in terminals[1]:
        return terminals[0][0]
    else:
        return terminals[0][1]