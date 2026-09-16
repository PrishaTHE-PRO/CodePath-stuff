# Problem 1: Hundred Acre Wood
### U - Understand 
1. Share 2 questions you would ask to help understand the question:
  - What is the name of the function that needs to be created?
  - What exact string should the function print?

### P - Plan
2. Write out in plain English what you want to do: 
  - Create a function called `welcome()`
  - Print the message "Welcome to The Hundred Acre Wood!"

3. Translate each sub-problem into pseudocode:
  - Define a function named `welcome`
  - Print "Welcome to The Hundred Acre Wood!"
  - End the function

### I - Implement
4. Translate the pseudocode into Python and share your final answer:
def welcome():
    print("Welcome to The Hundred Acre Wood!")

# Problem 2: Greeting
### U - Understand 
1. Share 2 questions you would ask to help understand the question:
  - What param does the function accept?
  - What messsage should be printed using the provided name?

### P - Plan
2. Write out in plain English what you want to do: 
  - create a fuction called 'greeting(name)'
  - use the 'name' param in the welcome message
  - print the complete scentence with the person's name inserted

3. Translate each sub-problem into pseudocode:
  - define a function named 'greeting' with param 'name'
  - print "Welcome to The Hundred Acre Wood <name>! My name is Christopher Robin."
  - end the function

### I - Implement
4. Translate the pseudocode into Python and share your final answer:
def greeting(name):
  print("Welcome to The Hundred Acre Wood {name}! My name is Christopher Robin.")

# Problem 3: Catchphrase
### U - Understand 
1. Share 2 questions you would ask to help understand the question:
  - what characters have predefined catchphrases?
  - what should be printed if the character is not in the list of known characters?

### P - Plan
2. Write out in plain English what you want to do: 
  - create a function called `print_catchphrase(character)`
  - print the character's catachphrase if known
  - else print error message

3. Translate each sub-problem into pseudocode:
  - Define a function `print_catchphrase(character)`
  - Check the character's name
  - Print the matching catchphrase if found
  - Else, print the error message
  - End the function

### I - Implement
4. Translate the pseudocode into Python and share your final answer:
def print_catchphrase(character):
  if character == 'Pooh':
    print("Oh brother!")
  elif character == "Tigger":
    print("TTFN: Ta-ta for now!")
  elif character == "Eeyore":
    print("Thanks for noticing me.")
  elif character == "Christopher Robin":
    print("Silly old bear.")
  else:
    print(f"Sorry! I don't know {character}'s catchphrase!")

# Problem 4: Return Time
### U - Understand 
1. Share 2 questions you would ask to help understand the question:
  - What would the function return if 'x' is a valid index?
  - what should the function return if 'x' is not a valid index?

### P - Plan
2. Write out in plain English what you want to do: 
  - create a function that returns the item at index 'x'
  - return 'None' if 'x' is not a valid index

3. Translate each sub-problem into pseudocode:
  - define fucntion get_item
  - if 'x' is a valid index, return the item at index 'x'
  - else, return 'None'
  - end function

### I - Implement
4. Translate the pseudocode into Python and share your final answer:
def get_item(items, x):
  if 0 <= x < len(items):
    return items[x]
  return None

# Problem 5: Total Honey
### U - Understand 
1. Share 2 questions you would ask to help understand the question:
  - what does the fuction return?
  - can I use 'sum()'?

### P - Plan
2. Write out in plain English what you want to do: 
  - add all numbers in the list and return the total

3. Translate each sub-problem into pseudocode:
  - set the total = 0
  - loop through the list and add each numebr to total
  - return total

### I - Implement
4. Translate the pseudocode into Python and share your final answer:
def sum_honey(hunny_jars):
  total = 0
  for jar in hunny_jars:
    total = jar
  return total


