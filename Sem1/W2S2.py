# Problem 1: Most Endangered Species
### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
# - which field determines conservation priority?
# - what should happen if multiple species have the same lowest population?

### P - Plan
# 2. Write out in plain English what you want to do: 
# - Find the species with the lowest popualtion
# - return its name

# 3. Translate each sub-problem into pseudocode:
# - set the first species as the current msot endangered
# - loop through the remaining species
# - if a species has a lower popualtion:
    # - upsate the current most endangered species
# - return the name of the most endangered species

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def most_endangered(species_list):
    most_endangered_species = species_list[0]

    for species in species_list:
        if species["population"] < most_endangered_species["population"]:
            most_endangered_species = species

    return most_endangered_species["name"]

# Problem 2: Identifying Endangered Species
### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
# - are species represented by individual characters?
# - should uppercase and lowercase letters be treated differntly?

### P - Plan
# 2. Write out in plain English what you want to do: 
# - count how many observed species are endangered
# - return the total amount

# 3. Translate each sub-problem into pseudocode:
# - convert endangered_species to a set
# - initialize the count to 0
# - loop through observes_species
# - if the spcies is in the set:
    # - increment the counter 
# - return the counter

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def count_endangered_species(endangered_species, observed_species):
    endangered = set(endangered_species)
    count = 0

    for species in observed_species:
        if species in endangered:
            count += 1

    return count

# Problem 3: Navigating the Research Station
### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
# - do we start at index 0?
# - is movement cost the absolue difference between indices?

### P - Plan
# 2. Write out in plain English what you want to do: 
# - track the current position
# - move to each required observation point and add the distance traveled

# 3. Translate each sub-problem into pseudocode:
# - create a dictionary mapping each charcter to its index
# - set current position to 0 and total time to 0
# - loop through each charcter in observation
# - find its index and add the distance from the current position
# - update the current position
# - return the total time

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def navigate_research_station(station_layout, observations):
    positions = {}

    for i in range(len(station_layout)):
        positions[station_layout[i]] = i

    current = 0
    total_time = 0

    for observation in observations:
        target = positions[observation]
        total_time += abs(target - current)
        current = target

    return total_time

# Problem 4: Prioritizing Endangered Species Observations
### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
# - should species in priority_species appear first in the given order?
# - how should species not in priority_species be ordered?

### P - Plan
# 2. Write out in plain English what you want to do: 
# - assign each priority species a ranking
# - sort the observations using those rankings
# - place non-priority species at the end in ascending order

# 3. Translate each sub-problem into pseudocode:
# - create a dictionary mapping each priority species to its index
# - create a helper function that returns:
    # - the species' priority index if it is in priority_species
    # - a large value otherwise
# - sort observed_species using the helper function
# - return the sorted lsit

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def prioritize_observations(observed_species, priority_species):
    order = {}

    for i in range(len(priority_species)):
        order[priority_species[i]] = i

    def sort_key(species):
        if species in order:
            return (order[species], species)
        return (len(priority_species), species)
    
    return sorted(observed_species, key=sort_key)

# Problem 5: Calculating Conservation Statistics
### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
# - should the minimum and maximum populations be removed repeatedly until the array is empty?
# - do we return the number of unique averages or the averages themselves?

### P - Plan
# 2. Write out in plain English what you want to do: 
# - sort the populations
# - pair the smalles and largest populatations, compute their averages, and count
# - how many unique averages occur

# 3. Translate each sub-problem into pseudocode:
# - sort species_populations
# - create an empty set for averages
# - use two pointers: one at the start and one at the end
# - while the pointers have not crossed:
    # - calculate the average of the two populations
    # - add the average to the set
    # - move both pointers inward
# - return the size of the set

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def distinct_averages(species_populations):
  species_populations.sort()

  averages = set()
  left = 0
  right = len(species_populations) - 1

  while left < right:
      average = (species_populations[left] + species_populations[right]) / 2
      averages.add(average)

      left += 1
      right -= 1

  return len(averages)