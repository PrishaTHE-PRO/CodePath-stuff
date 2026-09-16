# Problem 1: Festival Lineup
### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
# - should each artist be pairs with set time at the same index?
# - what should the function return if both lists are empty?

### P - Plan
# 2. Write out in plain English what you want to do: 
# - create a dictionary
# - match each artist with the set time at the same index
# - return the dictionary

# 3. Translate each sub-problem into pseudocode:
# - create an empty dictionary
# - loop through the lists
# - add each artist and set time as key-value pair
# - return the dictionary

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def lineup(artists, set_times):
    lineup_dict = {}

    for i in range(len(artists)):
        lineup_dict[artists[i]] = set_times[i]

    return lineup_dict

# Problem 2: Planning App
### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
# - what should be returned if the artist is not in the schedule?
# - is each artist name a unique key in the dictionary?

### P - Plan
# 2. Write out in plain English what you want to do: 
# - check if the artist exists in the schedule
# - return their info if founf; otherwise return an error message

# 3. Translate each sub-problem into pseudocode:
# - if artist is in festival_schedule
#   - return festival_schedule[artist]
# - return {"message": "Artist not found"}

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def get_artist_info(artist, festival_schedule):
    if artist in festival_schedule:
        return festival_schedule[artist]
    return {"message": "Artist not found"}

# Problem 3: Ticket Sales
### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
# - should all ticket counts be added together?
# - can the dictionary be empty?

### P - Plan
# 2. Write out in plain English what you want to do: 
# - add all ticket sales values
# - return the total 

# 3. Translate each sub-problem into pseudocode:
# - get all values from ticket_sales
# - sum all values
# - return the sum

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def total_sales(ticket_sales):
    return sum(ticket_sales.values())

# Problem 4: Scheduling Conflict
### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
# - should an artist be included only if both the artist and set time match?
# - what should be returned if there are no conflicts?

### P - Plan
# 2. Write out in plain English what you want to do: 
# - find artists that appear in both scheduled with the same set time
# - store and return those matches

# 3. Translate each sub-problem into pseudocode:
# - create an empty dictionary 
# - loop through venue1_schedule
# - if the artist is in venue2_schedule and the time matche:
  # - add the artist and time to the result
# - return the result

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def identify_conflicts(venue1_schedule, venue2_schedule):
    conflicts = {}

    for artist in venue1_schedule:
        if artist in venue2_schedule and venue1_schedule[artist] == venue2_schedule[artist]:
            conflicts[artist] = venue1_schedule[artist]

        return conflicts

# Problem 5: Best Set
### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
# - how should ties be handeled?
# - does each attendee vote for exactly one artist?

### P - Plan
# 2. Write out in plain English what you want to do: 
# - count how many votes each artist recieved
# - return the artist with the most votes

# 3. Translate each sub-problem into pseudocode:
# - create an empty dictionary for vote counts
# - loop through all votes
# - increment the count for each artist
# - return the artist with the highet count 

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def best_set(votes):
    counts = {}

    for artist in votes.values():
        counts[artist] = counts.get(artist, 0) + 1

    return max(counts, key = counts.get)