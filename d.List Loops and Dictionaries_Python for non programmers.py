#LIST
fav_movies = ["Notebook", "Smile", "Tomorrow War", "Don't Breath"]

print(fav_movies)

print(fav_movies[0])

print(fav_movies[2])

#CHALLENGE: Make a list of your 3 favorite numbers ad print the first number from your list.

fav_number = [13, 1, 6]

# list start counting from 0. So, 13 is placed at 0, 1 is placed at 1 and 6 is placed at 2. Thus, my favorite number is placed at 0hence 13.

print(fav_number[0])

#LIST --- ADD, INSERT, DELETE

fav_movies = ["Notebook", "Smile", "Tomorrow War", "Don't Breath"]

print(len(fav_movies))

#ADD
fav_movies.append("The Conjuring")

print(len(fav_movies))

print(fav_movies)

#INSERT
fav_movies.insert(6,"The Barbie Movie")

print(fav_movies)

#DELETE

del(fav_movies[2])

print(fav_movies)

#CHALLENGE: REMOVE ENOUGH ITEMS FROM FAV MOVIES UNTIL THERE'S ONLY 1 MOVIE LEFT

del(fav_movies[0])
del(fav_movies[0])
del(fav_movies[0])
del(fav_movies[0])

print(fav_movies)

#QUESTION: WHAT IF I WANTED TO DELETE EVERYTHING BUT "THE CONJURING" ?
fav_movies = ["Notebook", "Smile", "Tomorrow War", "Don't Breath"]
fav_movies.append("The Conjuring")
fav_movies.insert(6,"The Barbie Movie")

print(fav_movies)

del(fav_movies[0])
del(fav_movies[1])
del(fav_movies[2])


print(fav_movies)

#FOR LOOPS
# Allow us to execute teh same chunck of code over and over and over again.

for number in range(10):
  print("Hello") # notice indent
  print("Hi there") 
  print(number) #notice number first starts at 0 so 10 is from 0-9

for x in range(10):
  print(x) # get the same ouptput as above.


fav_movies = ["Notebook", "Smile", "Tomorrow War", "Don't Breath"]
for movie in fav_movies:
  print(movie)

#Fun example to show how powerful computers are 
##for number in range(10000):
##  print(number) #its prints out 0-9999 in seconds.

# CHALLENGE
# Loop 40 times and print the number of the loop time 2. Ex; 2,4, 6,8...
for number in range(40):
  print(number*2) # print number betwwen 0-78 (0x2 - 39x2)

# This doenst really answer our question because because we want answers starting from 2,4,6,8...

for number in range(40):
  print((number+1)*2) #we seperate both equations by brackets (bedmas) and now we have our exact answers.

# DICTIONARIES
# Key value pair.
cats = {"Jane":6}
# Dictionary = cat
# Key = Jane
# value = 6 (the age of the cat)

cats = {"Jane":6, "Tom":14, "Sara":8}
print(cats)
print(cats["Tom"]) # Can only prove keys
# To add
cats["Wilson"]=1
print(cats)
# To see lenght
len(cats)
print(len(cats))
# To delete
del(cats["Tom"])
print(cats)  

# CHALLENGE : Create a dictionary with ints for keys and booleans for values.

challenge = {1:True, 2:False, 3:True, 4:False, 5:False, 6:True}
print(challenge)
