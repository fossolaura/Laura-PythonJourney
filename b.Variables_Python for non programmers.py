wallet = 30

print (wallet)

wallet = 24

print(wallet)

#Challenge: make a variable call day and set it equal to the date of the month 
day = 7

print(day)

#There are 2 types of varaibles: Intergers and floats. 

  #intergers are whole numbers and can be positive or negative.
day = 7
temp = -11

 #Floats are decimals numbers and can be negative or positive.
weight= 208.4

print(3 + 6)
#no capital p
#no space between print and parenthesis
#space between number and operations sign

print(day + 3)
print(weight * 2)
print(temp / 2)
print(day - 4)

#Challenge: Find something in your life to represent a int and a float. Put them in varaiables
  #int
age = 25
  #float
height = 5.9

#Strings (text) need a quote around it.

shirt = "pink"

print(shirt)

#Can use double quotes and single quotes but you cannot mixed them in one string. 

shirt = 'pink'

print(shirt)

store = "Laura's Daquari"

print(store)

store = "Laura\'s Daquari"

print(store)

#add a backslah before the first quote so as to treat it as regular single quote and not the end of a string.


#CHALLENGE: Put the name of a movie you like into a variable called movie

movie = "smile"

print(movie)



#Using varaibles in strings.

print("Today is January 7 and its' -11 degrees outside")

#to add variables in strings, we use the f string and add the variable in curly brackets.

month = "January"

print(f"Today is {month} {day} and it's {temp} outside")


#CHALLENGE: Make a variable called day_name and set it to day of the week like tuesday and add it to the string we print.

day_name = "Sunday"
year = 2024

print(f"Today is {day_name}, {month} {day} {year} and it's {temp} outside")


#BOOLEANS AND IF STATEMENT
  #binanry, 1/0, yes or no, true or false.

light_is_on = True  

if light_is_on:
  print("The light is on!")
print("Hello")


#CHALLENGE: Find something around you that can be represented by a bolleand and make a variable for it.

Fridge_is_open = False 

light_is_on = False
if light_is_on:
  print("the light is on!")
else:
  print("We are in the dark")

weight = 208.4
if weight < 210:
  print("you are under weight :)")

# 2 equal signs (==) means exactly equal to
  # != means not the same.

#CHALLENGE: Make a variable call age, if someone is 18yrs or older, print that they are an adult. Otherwise print that they are a child.

age = 25
if age >= 18:
  print("ADULT")
else:
  print("CHILD")