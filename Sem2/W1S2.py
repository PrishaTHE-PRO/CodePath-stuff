# Problem 8: Exclusive Elements
### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
# - Should the elements keep their original order from each list?
# - If an element appears in both lists, should it be excluded from the result?

### P - Plan
# 2. Write out in plain English what you want to do: 
# - I want to find the elements that are only in lst1 and add them to a new list. Then I want to find the elements that are only in lst2 and add those to the same list. Finally, I will return the new list.


# 3. Translate each sub-problem into pseudocode:
# - Create an empty list called result
# - Go through each element in lst1
# - If the element is not in lst2, add it to result
# - Go through each element in lst2
# - If the element is not in lst1, add it to result
# - Return result


### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def exclusive_elemts(lst1, lst2):
    result = []
    for elm1 in lst1:
        if elm1 not in lst2:
            result.append(elm1)

    for elm2 in lst2:
        if elm2 not in lst1:
            result.append(elm2)

    return result

# I picked this problem because it helped me practice working with lists, for loops, and the not in operator. 
# It also helped me understand how to compare two lists and find elements that are unique to each list.

# Problem 10: Eeyore's House
### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
# - Does a pair count as good when pile1[i] can be divided evenly by pile2[j] * k?
# - Do we need to check every possible combination of a stick from pile1 and a stick from pile2?

### P - Plan
# 2. Write out in plain English what you want to do: 
# - I want to compare every stick in pile1 with every stick in pile2. For each pair, I will multiply the length from pile2 by k and check if the length from pile1 is divisible by that number. 
# If it is, I will increase my count by 1. At the end, I will return the count.

# 3. Translate each sub-problem into pseudocode:
# - Create a variable count and set it to 0
# - Loop through each stick in pile1
# - Loop through each stick in pile2
# - Calculate pile2 stick * k
# - Check if the pile1 stick is divisible by that value
# - If it is, increase count by 1
# - Return count

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def good_pairs(pile1, pile2, k):
    count = 0
    for stick1 in pile1:
        for stick2 in pile2:
            if stick1 % (stick2 * k) == 0:
                count += 1
    return count

# - I picked this problem because it helped me practice nested for loops and the modulo % operator. 
# It also helped me understand how to compare every possible pair of elements from two different lists.

# Problem 6: Acronym
### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
# - Should the letters in the acronym be in the same order as the words?
# - Should the function return False if the number of letters in s does not match the number of words?

### P - Plan
# 2. Write out in plain English what you want to do: 
# - I want to get the first letter from each word and combine them into a new string. 
# Then I will compare that string to s. If they are the same, I will return True; otherwise, I will return False.

# 3. Translate each sub-problem into pseudocode:
# - Create an empty string called acronym
# - Loop through each word in words
# - Add the first character of each word to acronym
# - Compare acronym to s
# - Return True if they are equal, otherwise return False

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def is_acronym(words, s):
    acronym = ""

    for word in words:
        acronym += word[0]

    return s == acronym

# I picked this problem because it helped me practice working with strings, lists, loops, and indexing. 
# It also helped me understand how to access the first character of each word and build a new string from those characters.