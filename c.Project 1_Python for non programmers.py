#FORTUNE COOKIE PROJECT

#PICKING RANDOM NUMBERS

#For intergers
import random
random.randint(1,10)
print(random.randint(1,10))

#for floats
random.random
print(random.random())

#CHALLENGE: Make your own version of the magic 8 ball that prints yes, no, or maybe each time you ask it.

answer = random.randint(1,3)

if answer == 1:
  print("yes")
if answer == 2:
  print("No")
if answer == 3:
  print("Maybe")

#CHOOSING WHAT FORTUNE TO SHOW

import random

lucky_number = random.randint(1,100)

fortune_number = random.randint(1,3)

fortune_text = ""

if fortune_number == 1:
  fortune_text = "You will have a great day !"
if fortune_number == 2:
  fortune_text = "Today will be tough...but worth it."
if fortune_number == 3:
  fortune_text = "You will get married this year!"
      

print(f"{fortune_text} Your lucky number is: {lucky_number}")