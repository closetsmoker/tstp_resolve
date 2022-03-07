# state 
# state is the value of a program's variables while it is running. 
# global state is the value of a program's global variables while it is running 

# procedural programming example 
from curses.textpad import rectangle
from tkinter import W


x = 2
y = 4
z = 8 
xyz = x + y + z
xyz
# each line of code in the above example changes the program's state.

# another example: 
rock = []
country = []


def collect_songs(): 
    song = "Enter a song." 
    ask = "Type r or c. q to quit"


    while True: 
        genre = input(ask)
        if genre == "q":
            break


        if genre == "r": 
            rk = input(song)
            rock.append(rk)

        elif genre == "c":
            cy = input(song)
            country.append(cy)
        
        else: 
            print("Invalid.")
        print(rock)
        print(country)

collect_songs()

# there is no state in functional programming
# example of non-functional programmingm 
a = 0


def increment(): 
    global a 
    a += 1

# same code but done functionally 
def increment(a): 
    return a + 1

# but of course we want to use object-oriented programming 
# where every object is an instance of a class 
# methods are like functions but you define them within a class and ca nonly be called on the object that the class creates 
#
# example below: 
class Orange: 
    def __init__(self):
        print("Created!")

# self can be used to define an instance variable: a variable that belongs to that object. 
# multiple objects off the same class can have different instance variables 
# instance variable example below: 
class Orange: 
    def __init__(self, w, c): 
        self.weight = w 
        self.color = c 
        print("Created")

# the code in __init__ executes when you create the object 
# magic method: any method surrounded by double underscores like __init__ 
class Orange: 
    def __init__(self,): 
        self.weight = w 
        self.color = c
        print("Created!")

# now let's instantiate the object 
orange_1 = Orange(10, "dark orange")
# we can print all kind of attributes
print(orange_1)
print(orange_1.weight)
print(orange_1.color)

# we can modify single attributes of an object as well 
class Orange: 
    def __init__(self, w, c):
        self.weight = w 
        self.color = c
        print("Created!")

or1 = Orange(10, "dark orange")
or1.weight = 100
or1.color = "light orange"

print(or1.weight)
print(or1.color)

# we can create multiple objects of a single class 
ora1 = Orange(4, "light orange")
ora2 = Orange(8, "dark orange") 
ora3 = Orange(14, "yellow")

# we can define additional properties in a class 
class Orange(): 
    def __init__(self, w, c): 
        """weights are in oz"""
        self.weight = w 
        self.color = c
        self.mold = 0
        print("Created!")

    def rot(self, days, temp): 
        self.mold = days * temp 

orange = Orange(6, "orange")
print(orange.mold)
orange.rot(10, 98)
print(orange.mold)

# you can create many methods within a class 
# model a rectangle 

class Rectangle(): 
    def __init__(self, w, l): 
        self.width = w 
        self.len = l 
    

    def area(self): 
        return self.width * self.len
    
    def change_size(self, w, l): 
        self.width = w 
        self.len = l 

rectangle = Rectangle(10, 20)
print(rectangle.area())
rectangle.change_size(20, 40)
print(rectangle.area())

# Vocabulary 
# State: The value of a program's variables while it is running 
# Global state: THe value of a program's global variables while it is running 
# Procedural programming: A programming style in which you write a sequence of steps moving toward a solution
#   with each step changing the program's state 
# Functional programming: Functional programming addresses the problems that arise in procedural programming 
#   by eliminating global state by passing it from function to function
# Side effect: Changing the state of a global variable 
# Object-oriented: A programming paradigm where you define objects that interfact with each other. 
# Classes: A mechanism allowing the programmer to calssify and group together similar objects
# Methods: Suites in a class. They are like functions but defined inside of a class. They can only be called on the object the class creates 
# Instance: Every object is an instnace of a class. Every instance ofa  class has the same type as all other instances of that class 
# Instance Variables: Variables that belong to an object 
# Magic Method: A method python uses in different situations, like initializing an object. 
# Instantiating a class: Creating a new object using a class. 