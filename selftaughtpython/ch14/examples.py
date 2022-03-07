# Each class in Python is an object that is an instnace of that 
# class "type" 

class Square: 
    pass


new_square = Square()
print(new_square)

# Square is an object and we printed it. 
# Classes have two types of variables 
#   class variables & instance variables 
# what we have used so far has all been instnace variables defined with 
# the syntax self 
# [variable_name] = [variable_value] 
# instance variables belong to objects 

class Rectangle(): 
    def __init__(self, w, l): 
        self.width = w 
        self.len = l 
    

    def print_size(self): 
        print("""{} by {}
              """.format(self.width, 
                         self.len))


my_rectangle = Rectangle(10, 24)
my_rectangle.print_size()

# in the above example we are using instance variables
#
# Class variables belong to the object Python creates for each class definition & 
# the objects they create. They must be defined within an object. 
# class variables are accessed the same way you access an instance variable (with self)
# class variables allow you to share data between all of the instnaces of a class without 
# relying on global variables 

class Rectangle(): 
    recs = []


    def __init__(self, w, l):
        self.width = w 
        self.length = l 
        self.recs.append((self.width, self.length))
    

    def print_size(self):
        print("""{} by {}
              """.format(self.width, self.length))


r1 = Rectangle(10, 24)
r2 = Rectangle(20, 40)
r3 = Rectangle(100, 200)


print(Rectangle.recs)

# we define recs outside of the __init__ method because Python only cause the __init__ method 
# when creating an object - we want to be able to access the recs variable outside of class instance
# variables so that we can use that variable across every instance of the class 
# it's worth noting that we appended a tuple in the form of the Rectangle objects length and width into the recs list 
#
# Magic methods: every class in Python inherits from a parent class called Object. Python utilizes the method inherited
# from Object in different situations - like when you print an object: 

class Lion:
    def __init__(self, name):
        self.name = name 
    

lion = Lion("Dilbert")
print(lion)

# the output uses a magic method called __repr__ that it inherited from Object on it and prints whatever 
# __repr__ returns 
# you can override the __repr__ method to change what gets printed 

class Lion: 
    def __init__(self, name):
        self.name = name 
    

    def __repr__(self):
        return self.name


lion = Lion("Dilbert")
print(lion)

# here we will see the text "Dilbert" printed since we overrode the __repr__ method in order to 
# print what we wanted 
#
# operands in an expression also have a magic method the operator can use to evaluate the expression
# if we define an __add__ method in a class we can use the ogjects it creates as operands in an expression 
# with the addition operator 

class AlwaysPositive:
    def __init__(self, number):
        self.n = number 
    

    def __add__(self, other):
        return abs(self.n + other.n)


x = AlwaysPositive(-20)
y = AlwaysPositive(10)

print(x + y)

# Is: the keyword "is" returns True if two objects are the same object, and False if not
# example: 

class Person: 
    def __init__(self):
        self.name = 'Bob'


bob = Person()
same_bob = bob 
print(bob is same_bob)


another_bob = Person()
print(bob is another_bob)

# use the is keyword to check if a variable is None: 

x = 10 
if x is None: 
    print("x is None :(")
else: 
    print("x is not None")


x = None
if x is None: 
    print("x is None :(")
else: 
    print("x is not None")

# Vocabulary
# Instance variable: An instance variable belongs to an object. 
# Private variables: A variable an object can access, but the client cannot. 
# Private method: A method an object can access, but the client cannot. 
# Public variable: A variable a client can access. 