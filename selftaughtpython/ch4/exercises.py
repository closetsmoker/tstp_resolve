# 1. write a function that takes a number as an input and returns that number squared 
def squared():
    a =  input("Input a number: ")
    a = int(a)
    a = a ** a
    print(a)

squared()

# 2. create a function that accepts a string as a parameter and prints in 
def print_string():
    string = input("Input a message: ")
    string = str(string)
    print(string)

print_string()

# 3. Write a function that takes three required paramters and two optional paramters
def big_function(a, string_b, c, d=1, e=2): 
#    a = input("Input a number: ")
    a = str(a)
#    string_b = input("Input a string: ")
    string_b = str(string_b)
#    c = input("Input a number: ")
    c = str(c)
    d = str(d)
    e = str(e)
    print(a + string_b + c + d + e)
    return a, string_b, c, d, e

a = 1
string_b = "gobba gool" 
c = 2

big_function(a, string_b, c)

# 4. Write a program with two functions The first function should take an integer as a parameter and return the result of the integer divided by 2
# The second function should take an integer asa parameter and return the result of the integer multiplied by 4 
# Call the first function, save the result as a variable, and pass it as a parameter to the second funiction 
def function_one(x):
    int(x) 
    return x / 2

def function_two(x):
    int(x)
    return x * 4

function_one_result = function_one(2)
function_two_result = function_two(function_one_result)
print(function_two_result)

# 5. Write a function that convert a string to a float and returns the result. Use exception handling to catch the exception that could occur. 
def function_float():
    float_input = input("Input a number: ")
    floated_input = float(float_input)
    return floated_input

#result = function_float()
#print(result)

try: 
    result = function_float()
    print(result)
except ValueError:
    print("Please enter a valid number.")

# 6. add a docstring to all of your functions 
# no