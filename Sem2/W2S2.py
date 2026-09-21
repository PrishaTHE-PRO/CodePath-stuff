# Problem 6: Wildlife Reintroduction 
### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - Can each character in raised_species only be used once?
# - Can target_species contain the same character more than once?

### P - Plan
# 2. Write out in plain English what you want to do:
# Count how many times each species appears in raised_species.
# Count how many times each species is needed to make one target_species.
# For each species in target_species, figure out how many copies we can make.
# The smallest number of copies will be the answer.

# 3. Translate each sub-problem into pseudocode:
# Create an empty dictionary for raised species counts
# Loop through raised_species:
#     Add each species to the dictionary or increase its count
# Create an empty dictionary for target species counts
# Loop through target_species:
#     Add each species to the dictionary or increase its count
# Set max_copies to a large number
# Loop through each species in the target dictionary:
#     Find how many copies can be made using that species
#     Update max_copies to the smaller value
# Return max_copies

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:

def max_species_copies(raised_species, target_species):
    raised_count = {}
    target_count = {}

    for species in raised_species:
        if species in raised_count:
            raised_count[species] += 1
        else:
            raised_count[species] = 1

    for species in target_species:
        if species in target_count:
            target_count[species] += 1
        else:
            target_count[species] = 1

    max_copies = len(raised_species)

    for species in target_count:
        if species not in raised_count:
            return 0

        copies = raised_count[species] // target_count[species]
        max_copies = min(max_copies, copies)

    return max_copies


raised_species1 = "abcba"
target_species1 = "abc"
print(max_species_copies(raised_species1, target_species1))

raised_species2 = "aaaaabbbbcc"
target_species2 = "abc"
print(max_species_copies(raised_species2, target_species2))

#I picked this problem because I wanted to practice using dictionaries to count characters and compare how many of each character are available versus how many are needed.

# Problem 8: Equivalent Species Pairs

### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - Does the order of the two species in a pair matter?
# - Should we count every combination of two equivalent pairs?

### P - Plan
# 2. Write out in plain English what you want to do:
# Go through each species pair and put the smaller number first so that
# equivalent pairs look the same.
# Use a dictionary to keep track of how many times each pair has appeared.
# Every time we see a pair again, add the number of previous matching pairs
# to the total.

# 3. Translate each sub-problem into pseudocode:
# Create an empty dictionary to store pair counts
# Set count to 0
# Loop through each pair in species_pairs:
#     Put the smaller value first and larger value second
#     Turn the pair into a tuple
#     If the pair is already in the dictionary:
#         Add its current count to the total
#         Increase its count in the dictionary
#     Otherwise:
#         Add the pair to the dictionary with a count of 1
# Return count

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:

def num_equiv_species_pairs(species_pairs):
    pair_counts = {}
    count = 0

    for pair in species_pairs:
        a = min(pair[0], pair[1])
        b = max(pair[0], pair[1])
        normalized_pair = (a, b)

        if normalized_pair in pair_counts:
            count += pair_counts[normalized_pair]
            pair_counts[normalized_pair] += 1
        else:
            pair_counts[normalized_pair] = 1

    return count


species_pairs1 = [[1,2],[2,1],[3,4],[5,6]]
species_pairs2 = [[1,2],[1,2],[1,1],[1,2],[2,2]]

print(num_equiv_species_pairs(species_pairs1))
print(num_equiv_species_pairs(species_pairs2))

# I picked this problem because I wanted to practice using dictionaries to keep track of pairs and recognize when two pairs are equivalent even if their order is different.


# Problem 7: Count Unique Species

### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - Can a species count have leading zeros, such as "001"?
# - Should counts like "1", "01", and "001" be considered the same count?

### P - Plan
# 2. Write out in plain English what you want to do:
# Go through each character in ecosystem_data and replace every letter with a space.
# Split the new string by spaces to get each species count.
# Convert each count to an integer to remove leading zeros.
# Add the counts to a set so that duplicates are removed.
# Return the number of values in the set.

# 3. Translate each sub-problem into pseudocode:
# Create an empty string
# Loop through each character in ecosystem_data:
#     If the character is a digit:
#         Add it to the string
#     Otherwise:
#         Add a space to the string
# Split the string to get the species counts
# Create an empty set
# Loop through each species count:
#     Convert the count to an integer
#     Add it to the set
# Return the length of the set

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:

def count_unique_species(ecosystem_data):
    numbers_string = ""

    for char in ecosystem_data:
        if char.isdigit():
            numbers_string += char
        else:
            numbers_string += " "

    numbers = numbers_string.split()
    unique_numbers = set()

    for number in numbers:
        unique_numbers.add(int(number))

    return len(unique_numbers)


ecosystem_data1 = "f123de34g8hi34"
ecosystem_data2 = "species1234forest234"
ecosystem_data3 = "x1y01z001"

print(count_unique_species(ecosystem_data1))
print(count_unique_species(ecosystem_data2))
print(count_unique_species(ecosystem_data3))