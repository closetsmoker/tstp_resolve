# for-loops 
# for [variable_name] in [iterable_name]:
#   [instructions]
name = "Ted" 
for x in name: 
    print(x)
# variable names can be defined on the fly 

# Here we print out every item in a list 
shows = ["Game of Thrones", 
         "Narcos", 
         "Vice"]
for show in shows: 
    print(show)

# Here we iterate through a tuple: 
coms = ("A. Development", 
        "Friends", 
        "Always Sunny")
for show in coms: 
    print(show)

# loop through keys in a dictionary 
people = {"G. Bluth II":"A. Development", 
          "Barney":"HIMYM", 
          "Dennis":"Always Sunny"
         }
for character in people: 
    print(character)

# you can use a for-loop to change the items in a mutable iterable
# list example
tv = ["Game of Thrones", 
      "Narcos", 
      "Vice"]
i = 0
for show in tv:
    # create a new variable so that we can change the existing item in the list  
    new = tv[i]
    # convert the existing item to upper case 
    new = new.upper()
    # assign our new item to the index that we're currently working on 
    tv[i] = new
    # increment the count so we continue to loop through 
    i += 1

print(tv)

# accessing each item and its index in an iterable is so common there is a special syntax for it 
# we pass the iterable to enumerate and used a new variable i to keep track of the current index 
tv = ["Game of Thrones", "Narcos", "Vice"]
for i, show in enumerate(tv): 
    new = tv[i]
    new = new.upper()
    tv[i] = new 

print(tv)

# you can use for-loops to move data between mutable iterables 
tv = ["GOT", "Narcos", 
      "Vice"]
coms = ["Arrested Development", "friends", 
        "Always Sunny"]
all_shows = []

for show in tv: 
    show = show.upper()
    all_shows.append(show)

for shows in coms: 
    show = show.upper()
    all_shows.append(show)

print(all_shows)

# you can use the range function to create a sequence of integers and then iterate through them
# the range will stop one integer before the second argument and begin on the first argument
for i in range(1, 11): 
    print(i)

# while-looop will execute code so long as some condition is truel 
# syntax: while [expression]: [code_to_execute]
# example: 
x = 10
while x > 0: 
    print('{}'.format(x))
    x -= 1
print("Happy New Year!")

# this is an infinite loop 
# infinite loops are bad 
# don't code them

# while True: 
#     print("Hello, World!")

# you can use a break-statement with the keyword break to terminate a loop 
for i in range(0, 100): 
    print("Run {}".format(i))

# using a break-statement the loop will only run once 
for i in range(0, 100): 
    print("Run {}".format(i))
    break

# write a program that uses a break statement to keep the user asking for input until they type q to quit 
qs = ["What is your name?", 
      "What is your favorite color?", 
      "What is your quest?"]
n = 0
while True: 
    print("Type q to quit...")
    a = input(qs[n])
    if a == "q": 
        break 
    n = (n + 1) % 3

# you can use a continue-statement to stop the current interation of a loop and move to the next iteration of it 
# this will not execute the loop you are currently on. 
for i in range(1, 6): 
    if i == 3: 
        continue 
    print(i)

# while-loop example 
i = 1
while i <= 5:
    if i == 3:
        i += 1 
        continue 
    print(i)
    i += 1

# nested loops 
# you can nest loops 
for i in range(1, 3):
    print(i)
    for letter in ["a", "b", "c"]:
        print(letter)

# add numbers in a list to all the numbers in another list
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
added = []
for i in list1: 
    for j in list2: 
        added.append(i + j)

print(added)

# you can nest for-loops inside of while-loops and vice versa 

while input('y or n?') != 'n':
    for i in range(1, 6):
        print("Damn that's crazy {}".format(i))