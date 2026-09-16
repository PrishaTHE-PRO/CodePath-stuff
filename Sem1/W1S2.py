# Problem 1: Reverse Sentence
### U - Understand 
1. Share 2 questions you would ask to help understand the question:
  - What should be reversed?
  - What should happen if there is only one word?

### P - Plan
2. Write out in plain English what you want to do: 
  - Reverse the order of the words and return the new sentence

3. Translate each sub-problem into pseudocode:
  - split the sentence into words
  - reverse the list of words
  - join the owrds back into a string
  - return the result

### I - Implement
4. Translate the pseudocode into Python and share your final answer:
def reverse_sentence(sentence):
  words = sentence.split()
  words.reverse()
  return " ".join(words)

# Problem 2: Goldilocks Number
### U - Understand 
1. Share 2 questions you would ask to help understand the question:
  - what number should be returned?
  - what if every number is either the minimum or maximum?

### P - Plan
2. Write out in plain English what you want to do: 
  - return a number that is not the smalles or largest
  - return -1 if no such number exists

3. Translate each sub-problem into pseudocode:
  - find the min and max values
  - loop through the list
  - if a number is not the min or max, return it
  - return -1 if none are found

### I - Implement
4. Translate the pseudocode into Python and share your final answer:
def goldilocks_approved(nums):
  smallest = min(nums)
  largest = max(nums)

  for num in nums:
    if num != smallest and num != largest:
      return num
    return -1
  
# Problem 3: Delete Minimum
### U - Understand 
1. Share 2 questions you would ask to help understand the question:
  - Should we modify the original list or create a new one?
  - what order should the removed elements be returned in?

### P - Plan
2. Write out in plain English what you want to do: 
  - Repeatedly find the smallest number
  - remove if from the list and add it to a result list
  - return the result list

3. Translate each sub-problem into pseudocode:
  - Create an empty result list.
  - While the input list is not empty:
    - Find the minimum value.
    - Remove it from the list.
    - Append it to result.
  - Return result.

### I - Implement
4. Translate the pseudocode into Python and share your final answer:
def delete_minimum_elements(hunny_jar_sizes):
  result = []
  while hunny_jar_sizes:
    m = min(hunny_jar_sizes)
    hunny_jar_sizes.remove(m)
    result.append(m)
  return result

# Problem 4: Sum of Digits
### U - Understand 
1. Share 2 questions you would ask to help understand the question:
  - Should each digit be added idividually?
  - Can the number be converted to a string?

### P - Plan
2. Write out in plain English what you want to do: 
  - Break the numbers into digits
  - add all digits together and return the sum

3. Translate each sub-problem into pseudocode:
  - Convert number to string
  - loop through each character
  - convert each to integer and add to total
  - return total

### I - Implement
4. Translate the pseudocode into Python and share your final answer:
def sum_of_digits(num):
  total = 0
  for digit in str(num):
    total += int(digit)
  return total

# Problem 5: Bouncy, Flouncy, Trouncy, Pouncy
### U - Understand 
1. Share 2 questions you would ask to help understand the question:
  - what is the starting value of tigger?
  - which operations increase or decrease the value?

### P - Plan
2. Write out in plain English what you want to do: 
  - start tigger at 1
  - go through each operation and update the value
  - return the final value

3. Translate each sub-problem into pseudocode:
  - set tigger = 1
  - for each operation in the list:
  - if operation is "bouncy" or "flouncy", add 1
  - else subtract 1
  - return tigger

### I - Implement
4. Translate the pseudocode into Python and share your final answer:
def final_value_after_operations(operations):
  tigger = 1
  for op in operations:
    if op == bouncy or op == flouncy:
      tigger += 1
    else:
      tigger -= 1
  return tigger

