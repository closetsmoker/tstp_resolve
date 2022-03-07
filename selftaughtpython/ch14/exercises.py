# 1. Add a square_list class variable to a class called Square so that everytime you 
# create a new Square object, the new object gets added to the list. 

class Square():
    square_list = []


    def __init__(self, l):
        self.side = l
        self.square_list.append(self)


    def print_size(self):
        return self.side * 4

sq1 = Square(4)
sq2 = Square(7)
sq3 = Square(9)
print(Square.square_list)

# 2. Change the Square class so that when you print a Square object, a message prints
# telling you the len of each of the four sides of the shape. For example, if you create 
# a square with Square(29) and print it, Python should print 29 by 29 by 29 by 29. 

class Square(): 
    square_list = []


    def __init__(self, l):
        self.side = l 
        self.square_list.append(self)
    
    def calculate_size(self): 
        return self.side * 4
    
    def print_size(self): 
        print("""{} by {} by {} by {}
              """.format(self.side, self.side, self.side, self.side))

sq4 = Square(77)
sq4.print_size()
sq5 = Square(44)
sq5.print_size()
    

# 3. Write a function that takes two objects as parameters and returns True if they are 
# the same object, and False if not. 

def object_compare(object1, object2):
    return object1 is object2

obj1 = Square(23)
obj2 = Square(24)

print(object_compare(obj1, obj2))

