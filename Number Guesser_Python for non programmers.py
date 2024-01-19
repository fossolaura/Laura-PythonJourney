# GAME LOOP
guess = int(input("What is your guess ?: "))
correct_guess = 10

while guess != correct_guess: # a while loop
  guess = int(input("What is your guess ?: "))
print("You got the right answer :))".upper())

# -------------
guess = int(input("What is your guess ?: "))
correct_guess = 10
guess_count = 0

while guess != correct_guess: # a while loop
  guess = int(input("What is your guess ?: "))
  guess_count += 1
print(f"The right answer was {correct_guess} and it took you {guess_count} tries".upper()) 
# I actually did 10 tries so why does the ouput put have 9 tries?
#  need to make sure guess_count start     at 1 and not 0

guess = int(input("What is your guess ?: "))
correct_guess = 10
guess_count = 1

while guess != correct_guess: 
 guess = int(input("What is your guess ?: "))
  guess_count += 1
print(f"The right answer was {correct_guess} and it took you {guess_count} tries".upper()) # now i get 10 tries!

# HIGHER, LOWER AND POLISHED

# so lets keep optimizing our game loop

guess = int(input("What is your guess ?: "))
correct_guess = 10
guess_count = 1

while guess != correct_guess: 
  guess_count += 1
  if guess < correct_guess:
    guess = int(input("WRONG.You need to guess higher. What is your new guess ?: "))
  else: 
    guess = int(input("WRONG.You need to guess lower. What is your new guess ?: "))
print(f"WELL DONE! The right answer was {correct_guess} and it took you {guess_count} tries".upper())

# Now let optimise our game so as the answer is not always 10.

import random
print("The correct answer is between 1 and 100!")
guess = int(input("What is your guess ?: "))
correct_guess = random.randint(1,100)
guess_count = 1

while guess != correct_guess: 
  guess_count += 1
  if guess < correct_guess:
    guess = int(input("WRONG.You need to guess higher. What is your new guess ?: "))
  else: 
    guess = int(input("WRONG.You need to guess lower. What is your new guess ?: "))
print(f"WELL DONE! The right answer was {correct_guess} and it took you {guess_count} tries".upper())

# Let continues to optime the game 

import random
import time 
print("I'm going to pick a number between 1 and 100 and how have guess what number is it")
time.sleep(15)
print("Picking a number...")
time.sleep(10)
guess = int(input("What is your guess ?: "))
correct_guess = random.randint(1,100)
guess_count = 1

while guess != correct_guess: 
  time.sleep(2)
  guess_count += 1
  if guess < correct_guess:
    guess = int(input("WRONG.You need to guess higher. What is your new guess ?: "))
  else: 
    guess = int(input("WRONG.You need to guess lower. What is your new guess ?: "))
print(f"WELL DONE! The right answer was {correct_guess} and it took you {guess_count} tries".upper())