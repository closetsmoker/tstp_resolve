# 1. Define a class called Apple with four instnace variables that represent four attributes of an apple. 

class Apple(): 
    def __init__self(self, h, w, c):
        self.height = h 
        self.width = w
        self.color = c
        self.fresh = 10
        print("A bushel of apples!")

        def fresh(self, days, temp):
            self.fresh = days * temp

# 2. Create a Circle class with a method called area that calculates and returns its area
#       Then create a cirlce object, call area on it, and print the result, Use pythons pi function in the built-in math module

import math

class Circle(): 
    def __init__(self, r):
        self.radius = r

    def area(self): 
        return math.pi * self.radius ** 2

circle_1 = Circle(2.3)
print(circle_1.area())


# 3. Create a Triangle class with a method called area that calculates and returns its area. 
#       Then create a Triange object, call area on it, and print the result 

class Triangle():
    def __init__(self, b, h):
        self.base = b 
        self.height = h
    
    def area(self):
        return 0.5 * self.base * self.height

triangle_1 = Triangle(7, 4)
print(triangle_1.area())


# 4. Make a Hexagon class with a method called calculate_perimter that calculates and returns its perimter 
#       Then create a hexagon object, call calculate_perimter on it, and print the result. 
## P = 6a where A is the side 

class Hexagon():
    def __init__(self, a): 
        self.side = a

    def perimeter(self):
        return 6 * self.side

hexa = Hexagon(6)
print(hexa.perimeter())

