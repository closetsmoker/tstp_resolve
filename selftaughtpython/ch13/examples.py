# Good design adds value faster than it adds cost
#
# four pillars of object oriented programming 
# encapsulation
# abstraction 
# polymorphism 
# inheritence 
# 
# let's look at encapsulation 
# objects group  varaibles and methods in a single unit - an object 
# example below: 

from re import L


class Rectangle():
    def __init__(self, w, l):
        self.width = w
        self.length = l 
    
    def area(self):
        return self.width * self.length

# length and width hold the objects state
# encapsulation hides the class's internal data to prevent a client from directly accessing it
# example below: 

class Data:
    def __init__(self):
        self.nums = [1, 2, 3, 4, 5]
    
    def change_data(self, index, n):
        self.nums[index] = n

# example of accessing elements within the object 

class Data: 
    def __init__(self): 
        self.nums = [1, 2, 3, 4, 5]
    
    def change_data(self, index, n):
        self.nums[index] = n

data_one = Data()
# access the list directly within the object 
data_one.nums[0] = 100
print(data_one.nums)

data_two = Data()
data_two.change_data(0, 100)
print(data_two.nums)

# we can create private methods within a class
# python does not have private pariables, the common naming convention for handling this is proceeding the variable with 
# an underscore example: _unsafe_var
# HLE below: 

class PublicPrivateExample: 
    def __init__(self):
        self.public = "safe"
        self._unsafe = "unsafe" 
    
    
    def public_method(self):
        # clients can use this 
        pass 


    def _unsafe_method(self):
        # clients shouldn't use this 
        pass

# Abstraction: taking away or removing characteristics from something in order to reduce it to a set of essential characteristics 
# No good example for this one :(
# 
# Polymorphism: the ability to present the same interface for differing underlying forms (data types)
# Example: 

print("Hello, World")
print(200)
print(200.1)

# we can use the same print function in order to grab three different data types and display it in the terminal 
# we can use the built in type function to check data types

type("Hello World!")
type(200)
type(200.1)

# no polymorphism example 
# (shapes objects, whatever)

#shapes = [tr1, sq1, cr1]
#for a_shape in shapes:
#    if type(a_shape) == "Triangle":
#        a_shape.draw_triangle()
#    elif type(a_shape) == "Square":
#        a_shape.draw_square()
#    elif type(a_shape) == "Circle":
#        a_shape.draw_circle()
#    else:
#        pass 

# with polymorphism 
#shapes = [tr1, 
#          sw1, 
#          cr1]
#for a_shape in shapes: 
#    a_shape.draw()

# Inheritence: When you create a class it can inherit methods and variables from another class. 
# The class that is inherited from is the parent class 
# The class that inherits is the child class. 
#
# here is a class that models a shape 

class Shape(): 
    def __init__(self, w, l): 
        self.width = w 
        self.len = l

    
    def print_size(self):
        print("""{} by {}
             """.format(self.width, 
                        self.len))


my_shape = Shape(20, 25)
my_shape.print_size()

# let's create a square now that inherits the features of the Shape class 

class Shape(): 
    def __init__(self, w, l): 
        self.width = w 
        self.len = l 
    

    def print_size(self):
        print("""{} by {}
              """.format(self.width, self.len))

class Square(Shape):
    pass

a_square = Square(20, 20)
a_square.print_size()

# you can define methods and variables in a child class without affecting the parent class 
# another example

class Shape(): 
    def __init__(self, w, l):
        self.width = w 
        self.len = l 
    

    def print_size(self):
        print("""{} by {}
              """.format(self.width, self.len))


class Square(Shape):
    def area(self):
        return self.width * self.len


a_square = Square(30, 30)
# we can access the parent object method
a_square.print_size()
print(a_square.area())

# When a child class inherits a method from a parent class, you can override it by defining a 
# new method with the same name as the inherited method. A Child class's ability to change the 
# implementation of a method inherited from its parent class is called method overriding 

class Shape(): 
    def __init__(self, w, l):
        self.width = w 
        self.len = l 
    

    def print_size(self):
        print("""{} by {}
              """.format(self.width, self.len))


class Square(Shape):
    def area(self):
        return self.width * self.len
    

    def print_size(self):
        print("""I am {} by {}
              """.format(self.width, self.len))

a_square = Square(20, 20)
a_square.print_size()

# Composition: models the "has a" relationship by storage an object as a variable in another object. 
# You can use composition to represent the relationship between a dog and its owner 
# example below: 

class Dog():
    def __init__(self, name, breed, owner):
        self.name = name 
        self.breed = breed 
        self.owner = owner 


class Person(): 
    def __init__(self, name): 
        self.name = name 

ian = Person("Ian Howard")
momo = Dog("Momo", "Lab", ian)
print(momo.owner.name)

# Vocabulary
# The four pillars of object-oriented programming: The four main concepts in object-oriented 
#   programming: inheritance, polymorphism, abstraction, and encapsulation
# Inheritance: In genetic inheritance, you inherit attributes like eye color from your 
#   parent. Similarly, when you create a class, it can inherit methods and variables from
#   another class. The parent class is the class that is inherited from. The child class inherits
# Method overriding: A child class's ability to change the implementation of a method inherited 
#   from its parent class. 
# Polymorphism: Polymorphism is "the ability (in programming) to present the same interface for
#   differing underlying forms (data types)."
# Abstraction: The process of "taking away or removing characteristics from something in order 
#   to reduce it to a set of essential characteristics."
# Client: The code outside of the class that uses the object 
# Encapsulation: Encapsulation refers to two concepts
#   1. Objects group variables (state) and methods (for altering state) in a single unit - the object 
#   2. Hiding a class's internal data to prevent the client, the person using the code, from accessing it
# Composition: Composition models the "has a" relationship by storing an object as a variable in 
#   another object