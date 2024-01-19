# FUNCTIONS
def bark():
  print("Woof woof!")
  print("I'm a cute dog!")
# ran and noting shows off. we have to call the fxn
bark()
bark()
bark()
bark()

# to save time by manualing entrering the call, we can use a for loop fxn

def bark():
  print("Woof woof!")
  print("I'm a cute dog!")
  
for _x in range(100):
  bark()

# CHALLENGE: Create a fxn called hello that prints "Hello Laura!"

def hello():
  print("Hello Laura!")
hello()

# PARAMETERS
def hello(name):
  print(f"Hello {name}!")
hello("Laura")

# what if you want more parameter being passed into a fxn?

def add_number(num1, num2):
  print(num1 + num2)
add_number(4,8) 
add_number(3,7) 

# CHALLENGE: CREATE A FXN CALLED DOG_INFO THAT TAKES IN A DGD'S AGE AND NAME AND PRINTS A SENTENCE ABOUT THE DOG.

def dog_info (age, name):
  print(f"My name is {name}, I am {age} year's old!")
  
dog_info(5, "Oslo")

# RETURN
def double(number):
  number * 2
double(5)
# when ran, nothings is outputes... no print

def double(number):
  print(number * 2)
double(5)

# we could also use the return statement
# The return statement is used in a function to exit the function and go back to the place where it was called. 
    #particularly useful when you want your function to produce a result that can be stored in a variable or used in other operations.

def double(number):
  return number * 2
new_number = double(5)
# can use this as an intergers in other operations.

print(new_number)

# CHALLENGE: Create a fxn that returns as string in all caps.

def uppercase(text):
  return text.upper()
print(uppercase("i love food")) 

# NOW LET'S DO SOMETHING FUN

things_i_love = ["water", "coffee", "lipbalm", "money","waffles"]

for thing in things_i_love:
 print(uppercase(f"I love {thing}"))

# COMMENTS

wallet = 50

wallet -= 8 # I bought coffee

wallet += 60 # J gave me money

# CHALLENGE: Create a comment! like this one :) haha this is already a comment hahahahahaha.


# INPUT STATEMENT

input("Enter some text")

user_text = input("Enter some text:")
print(user_text)
print(user_text.upper())

# The its also putputed as a string
#Ex:
user_number = input("What number do you want to double:")
print(user_number * 2) # we get 22

# If you want to operate a multiplication, you have to convert the string to an int.

print(int(user_number) * 2)

# CHALLENGE: FIRST ASK FOR SOME TEXT, AND THEN THEM PROMPT " ENTER 1 TO UPPERCASE AND 2 TO LOWERCASE:" AND EITHER OUTPUT IN UPPER OR LOWER CASE.

user_input = input("Enter the first word that comes to mind:")
number_input = input("For that word, enter 1 for UPPERCASE or 2 for LOWERCASE:")
if number_input == "1":
  print(user_input.upper())
else:
  print(user_input.lower())



