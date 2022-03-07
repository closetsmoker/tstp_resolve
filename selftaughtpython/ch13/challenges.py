# 1. Create Rectangle and Square classes with a method called calculate_perimeter that 
# calculates the perimeter of the shapes they represent. Create Rectangle and Square 
# objects and call the method on both of them. 

class Rectangle():
    def __init__(self, w, l):
        self.width = w 
        self.length = l 
    

    def calculate_perimeter(self):
        return 2 * (self.width + self.length)

class Square(): 
    def __init__(self, w, l):
        self.width = w 
        self.length = l


    def calculate_perimeter(self):
        return 4 * self.length


new_rectangle = Rectangle(2, 4)
print(new_rectangle.calculate_perimeter())


new_square = Square(4, 2)
print(new_square.calculate_perimeter())

# 2. Define a method in your Square class called change_size that allows you to pass in
# a number that increases or decreases (if the number is negative) each side of a Square 
# object by that number

class Square(): 
    def __init__(self, w, l):
        self.width = w 
        self.length = l 


    def calculate_perimeter(self):
        return 4 * self.length

    def change_size(self, n):
        self.length = n

second_square = Square(2, 4)
print(second_square.calculate_perimeter())
second_square.change_size(5)
print(second_square.calculate_perimeter())


# 3. Create a class called Shape. Define a method in it called what_am_i that prints 
# "I am a shape" when called. Change your Square and Rectangle classes from the previous 
# challenges to inherit from Shape, create Square and Rectangle objects, and call the
# new method on both of them 

class Shape(): 
    def __init__(self):
        pass


    def what_am_i(self):
        print("I am a shape")

class Square(Shape): 
    def __init__(self, l):
        self.length = l

class Rectangle(Shape):
    def __init__(self, w, l):
        self.width = w 
        self.length = l


shape_square = Square(7)
shape_square.what_am_i()


shape_rectangle = Rectangle(7, 12)
shape_rectangle.what_am_i()

# 4. Create a class called Horse and a class called Rider. Use composition to model a
# horse that has a rider.

class Horse():
    def __init__(self, name, color, rider):
        self.name = name 
        self.color = color 
        self.rider = rider 


class Rider():
    def __init__(self, name):
        self.name = name


eileen = Rider("Eileen Thomason")
black_beautiy = Horse("Black Beauty", "Black", eileen)
print(black_beautiy.rider.name)