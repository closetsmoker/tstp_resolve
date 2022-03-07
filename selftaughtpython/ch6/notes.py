# Chapter 6: String manipulation 

# triple strings 
""" line one 
    line two 
    line three
"""

# strings like lists and tuples are iterable and indexed 
# strings operate on a 0 index
# will spell out the string character by character
author = "Kafka" 
author[0]
author[1]
author[2]
author[3]
author[4]

# if you try to look up a character past the last index python will raise an exception
# you can use negative indexes to search right to left 
author = "Kafka" 
author[-1]
author[-2]
author[-3]
author[-4]
author[0]

# strings like tuple are immutable 
# if you want to change characters in a string, you have to create a new string 
ff = "F. Fitzgerald" 
# create a new string to change it 
ff = "F. Scott Fitzgerald"

# concatenation 
# you can add strings 

"cat" + "in" + "hat"

# you can multiple a string 
"Sawyer" * 3

# upper method will change everything to upper case 
"We hold these truths...".upper()

# lower method will change everything to lower case 
"SO IT GOES...".lower()

# captialize method will capitalize the first letter of a string 
"four score and...".capitalize()

# format method will look for {} and replace them with parameters that you pass 
"William {}".format("Faulkner")

# you can also pass a variable 
last = "Faulkner"
"William {}".format(last)

author = "William Faulkner" 
year_born = "1897"

"{} was born in {}.".format(author, year_born)

# format method useful for creating a string from user input 
n1 = input("Enter a noun: ")
v = input("Enter a verb: ")
adj = input("Enter an adj: ")
n2 = input("Enter a noun: ")

r = """The {} {} the {} {}
    """.format(n1, v, adj, n2)

print(r)

# strings have a method called split, separate one string into two or more string 
# this creates a list with two items in it
"Hello.Yes!".split(".")

# join lets you add new characters between every character in a string 
first_three = "abc" 
result = "+".join(first_three)
result 

# you can turn a list of strings into a single setring by calling the join method on an empty string and passing the list as a param

words = ["The",
         "fox", 
         "jumped", 
         "over", 
         "the", 
         "fence", 
         "."]
one = "".join(words)
one

# you can remove leading and trailing whitespace from a string 
s = "       The         "
s = s.strip()
s

# replace method will replace every occurrence of a string with another string 
equ = "All animals are equal."
equ = equ.replace("a", "@")
print(equ)

# finding an index
# print the index of a character in a string 
"animals".index("m")

# if no match raise an exception 
"animals".index("z")

# if you are not sure if you'll find a match use a try block 
try:
    "animals".index("z")
except: 
    print("Not found")

# in keyword checks if a string is in another string, returns boolean true or false 
"Cat" in "Cat in the hat."
# True
"Bat" in "Cat in the hat" 
# False 

# not keyword will check if a string is not in another string 
"Potter" not in "Harry" 
# True

# string escapes 
"She said \"Surely.\""
'She said \"Surely.\"'

# new lines: \n
print("line1\nline2\nline3")

# slicing: return a new interable from a subset of item sin a different iterable 
# [iterable][[start_index:end_index]]
fict = ["Tolstoy", 
        "Camus", 
        "Orwell", 
        "Huxley", 
        "Austin"]
fict[0:3]

# string slicing 
ivan = "In place of death there was light." 
ivan[0:17]
ivan[17:33]

# if your start index is 0 you can leave the start index empty 
ivan = "In place of death there was light."
ivan[:17]

# if your end index is the last item in the iterable you can leave the end index empty 
ivan = "In place of death there was light."
ivan[17:]

# leave it empty and it'll pring the entire string 
ivan = """In place of death there was light."""
ivan[:]
