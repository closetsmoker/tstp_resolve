"Hello".upper()

"Hello".replace("o", "@")

# list is a container that stores objects in a specific order 

# create an empty list using the list function 
fruit = list()

# can also use brackets 
fruit = []

# create a list that has some data 
fruit = ["Apples", "Orange", "Pear"]

# append to an existing list 
fruit = ["Apples", "Oranges", "Pears"]
fruit.append("Bannanas")
fruit.append("Peach")
fruit

# you can store multiple data types in a list 
random = []
random.append(True)
random.append(100)
random.append(1.1)
random.append("Hello")
random 

# it is worth noting that strings, lists and tuples are all iterable 
# it is also worth knowing that a list is 0 indexed 
fruit = ["Apple", "Orange", "Pear"]
fruit[0]
fruit[1]
fruit[2]
# access each elemetn from the list 

# accessing an element of a list that doesn't exist will throw an error in python 
# list index out of range 
# lists are mutable, you can add and remove objects from the container 
# you can change an item in a list by assigning its index to a new element 
colors = ["blue", "green", "yellow"]
colors
colors[2] = "red" # yellow will be changed to "red"
colors

# pop removes the last item from a list 
colors = ["blue", "green", "yellow"]
colors
item = colors.pop() # this will remove yellow 

# if you try to use pop on an empty list Python will raise an exception 
# you can combine lists w/ the addition operator 
colors = [some_list]
colors2 = [some_other_list]
colors + colors2 

# you can check for an item in a list w/ the keyword in 
colors = ["blue", "green", "yellow"]
"green" in colors 

for "green" in colors: 
    some_function

# you can check not to see if an item is not in a list 

colors = ["blue", "green", "yellow"]
"black" not in colors

# len will show you how many items are in a list 
len(colors)

# list example 
colors = ["Purple", 
          "Orange", 
          "Green"]

guess = input("Guess a color: ")

if guess in colors: 
    print("You guessed correctly!")
else: 
    print("Wrong, guess again big daddy.")

# Tuples 
# immutable - contents cannot change 
# creating a tuple: 
my_tuple = tuple()
my_tuple 

# or 
my_tuple = ()
my_tuple

# adding objects to a tuple works closely to the way we add objects to a list 
rndm = ("Miss Jackson", 1958, True)
rndm 

# you always need to put a comma after a tuple so python can differentiate it from a number and evaluate the order of operations 

# this is a tuple 
("self_taught", )

# this is not a tuple 
(9) + 1

# you cannot change a tuple after you create it :(
dys = ("1984", 
       "Brave New World", 
       "Fahrenheit 451")

dys[1] = "Handmaid's Tale" 

# you can get items from a tuple the same way you'd get themf rom a list 
dys = ("1984", 
       "Brave New World", 
       "Fahrenheit 451")

dys[2]

# you can check if an item is in a tuple using keyword "in"
dys = ("1984", 
       "Brave New World", 
       "Fahrenheit 451")

"1984" in dys

for "1984" in dys: 
    some_function

# you can check if an item is not in a tuple using the keyword "not"
dys = ("1984", 
       "Brave New World", 
       "Fahrenheit 451")

"Handmaid's Tale" not in days

if "Handmaid's Tale" not in days: 
    some_function

# dictionaries 
# link one object to another 
# key to a value 
# this linking is called a mapping 
# end result is a key-value pair 
# dictionary values are mutable, dictionary keys are immutable

# syntax for creating a dictionary
my_dict = dict()

# or 
my_dict = {}
my_dict 

# create a key-value pair 
fruits = {"Apples":
          "Red", 
          "Banana": 
          "Yellow"}

fruits 
# dictionaries do not store key-value pairs in any particular order 

# adding key-value pairs 

facts = dict()

# add a key-value pair 
# code is the key 
# fun is the value 
facts["code"] = "fun"

# look up a key
facts["code"]

# add additional key-value pairs to the 'facts' dictionary 
facts["Bill"] = "Gates" 
facts["founded"] = "1776"

# you can use the in keyword to check if a key is in a dictionary 
# you cannot use the in keyword to check if a value is in a dictionary 

bill = {"Bill Gates": 
        "charitable"}

"Bill Gates" in bill 

for "bill gates" in bill: 
    some_function

# you can delete a key-value pair from a dictionary with the del keyword 
books = {"Dracula": "Stoker", 
         "1984": "Orwell", 
         "The Trial": "Kafka"}

del books["The Trial"]

books

# example script using a dictionary 

rhymes = {"1": "fun", 
          "2": "blue", 
          "3": "me", 
          "4": "floor", 
          "5": "live"
          }

n = input("Type a number: ")
if n in rhymes: 
    rhyme = rhymes[n]
    print(rhyme)
else: 
    print("Fat boy")

# you can store containers in other containers 
# list within a list 

lists = []
rap = ["Kanye West", 
       "Jay Z", 
       "Eminem",
       "Nas"]

rock = ["Bob Dylan", 
        "The Beatles", 
        "Led Zeppelin"]

djs = ["Zeds Dead", 
       "Tiesto"]

lists.append(rap)
lists.append(rock)
lists.append(djs)

print(lists)

# lists has three indexes, each index is a list 
# rap is index 0, rock is index 1, djs is index 2

rap = lists[0]
print(rap)

# append a new item to rap list and see the change when you call 'lists' 
rap = lists[0]
rap.append("Kendrick Lamar")
print(rap)
print(lists)

# you can store a tuple inside a list, a list insdie a tuple, and a dictionary inside ofa  list or a tuple

# empty list 
locations = []

# tuples
la = (34.0522, 188.2437)
chicago = (41.8781, 87.6298)

# add these tuples to the locations list 
locations.append(la)
locations.append(chicago)

# another example 

eights = ["Edgar Allan Poe", 
          "Charles Dickens"]

nines = ["Hemingway", 
         "Firtzgerald", 
         "Orwell"]

authors = (eights, nines)
print(authors)

# another example 

bday = {"Hemingway":
        "7.21.1899", 
        "Fitzgerald":
        "9.24.1896"}

my_list = [bday]
print(my_list)
my_tuple = (bday, )
print(my_tuple)

# a list, tuple, or dictionary can be a value in a dictionary 
ny = {"location":
      (40.7128, 74.0059), 
      
      "celebs":
      ["W. Allen", 
       "Jay Z.", 
       "K. Bacon"],
       
      "facts":
      ["state":
       "NY", 
       "country":
       "America"]
       
       }