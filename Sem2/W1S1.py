# Problem 8: Pooh's To Do's
### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
# - Should the function print the heading "Pooh's To Dos:" every time the function is called?
# - Should the tasks be numbered starting from 1?

### P - Plan
# 2. Write out in plain English what you want to do: 
# - Print the heading "Pooh's To Dos:" and then loop through the list of tasks, numbering and printing each task on a new line. If the list is empty, only print the heading.

# 3. Translate each sub-problem into pseudocode:
# - Print "Pooh's To Dos:"
# - Loop through each task in the list
# - Print the task's number followed by the task
# - Start numbering at 1

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def print_todo_list(tasks):
	print("Pooh's To Dos:") 
	for i in range(len(tasks) - 1):
		print(f"{i + 1}. {tasks[i]}")

# I picked this problme because I got to use an f-string to answer this problem more efficiently.

# Problem 11: T-I-Double Guh-ER
### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
# - Should I remove both uppercase and lowercase versions of the letters?
# - Should the function return the new string instead of printing it?

### P - Plan
# 2. Write out in plain English what you want to do: 
# - Go through the string and remove every occurrence of the letters t, i, g, e, and r. Then return the new string without those letters.

# 3. Translate each sub-problem into pseudocode:
# - Create an empty string to store the new string
# - Go through each character in the original string
# - If the character is not t, i, g, e, or r, add it to the new string
# - Return the new string

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def tiggerfy(s):
    result = ""

    for char in s:
        if char.lower() not in "tiger":
            result += char

    return result

# I picked this problem because it seemed straightforward but still gave me practice with strings, loops, conditionals, and returning values. 
# It also helped me practice going through a string character by character and modifying it based on a condition.
			

# Problem 10: Split Haycorns
### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
# - Should the list include the quantity itself as a divisor?
# - Should the divisors be returned in increasing order?

### P - Plan
# 2. Write out in plain English what you want to do: 
# - I want to find all the numbers that divide the given quantity evenly with no remainder. I will check each number from 1 up to the quantity and add it to a list if it is a divisor.


# 3. Translate each sub-problem into pseudocode:
# - Create an empty list for the divisors
# - Loop through every number from 1 to the quantity
# - Check if the quantity can be divided evenly by that number
# - If it can, add the number to the list
# - Return the list of divisors

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def split_haycorns(quantity):
    divisors = []
    for num in range(1, quantity + 1):
        if quantity % num == 0:
            divisors.append(num)

    return divisors

# I picked this problem because it helped me practice using for loops and the modulo % operator. 
# It also helped me understand how to check whether one number divides evenly into another.
