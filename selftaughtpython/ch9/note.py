# import os to get the correct path 
# then build the path 

import os 
os.path.join("Users", "bob", "st.txt")
# will translate to Users/bob/st.txt with appropriate slashes based on the OS 

# the mode you pass to open determines the actions you will be able to perform on the file once it is opened 
# r read only 
# w write only 
# w+ read and write 
# open function will return an object called a file object 

# open the file, write to it, close it 
st = open("st.txt", "w")
st.write("Hi from python")
st.close()

# you can automatically close files by using a with-statement 
# syntax: with open([file_path],[mode]) as [variable_name]: code
with open("st.txt", "w+") as h_file: 
    h_file.write("Hi from Python")

# we can do the same thing with reading the file 
with open("st.txt", "r") as f: 
    print(f.read())

# you can only read a file once without closing it and reopening to get the contents 
# you can save the contents of the file in a variable or a container to use them later. 
file_object = list()

with open("st.txt", "r") as f: 
    file_object.append(f.read())

print(file_object)

# working with CSV files 
import csv 

with open("st.csv", "w", newline=' ') as f:
    w = csv.writer(f, delimiter = ",")
    w.writerow(["one", "two", "three"])
    w.writerow(["four", "five", "six"])

# you can pass r as a parameter to open and then use csv library to read the file 
import csv 

with open("st.csv", "r") as f: 
    r = csv.reader(f, delimter=",")
    for row in r: 
        print(",".join(row))
