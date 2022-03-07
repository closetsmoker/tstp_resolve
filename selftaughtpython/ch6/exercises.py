# 1. Print every character in the string "Cammus"

string_1 = "Cammus"
print(string_1)
print(string_1[0])
print(string_1[1])
print(string_1[2])
print(string_1[3])
print(string_1[4])
print(string_1[5])

# 2. Write a program that collects two strings from a users, inserts them into the string: 
# "Yesterday I wrote a [response_one].  I sent it to [response_two]!"

response_one = input("Please enter a noun: ")
response_two = input("Please enter another noun: ")

sentence = "Yeseterday I wrote a {}.  I sent it to {}".format(response_one, response_two)
print(sentence)

# 3. Use a method to make the string "aldous Huxley was born in 1894." grammatically correct 
# by capitalizing the first letter in the sentence. 

sentence = "aldous Huxley was born in 1894.".capitalize()
print(sentence)

# 4. Take the string "Where now? Who now? When now?" and call a method that returns a list that looks like: 
# ["Where now?", "Who now?, "When now?"]
sentence = "Where now? Who now? When now?".split("?")
print(sentence)

# 5. Take the list ["The", "fox", "jumped", "over", "the", "fence", "."] and turn it into a grmmatically correct string. 
fox_list = ["The", 
            "fox", 
            "jumped", 
            "over", 
            "the", 
            "fence", 
            "."]
sentence = " ".join(fox_list)
sentence = sentence[0:-2] + "."
print(sentence)

# 6. Replace every instance of "s" in "A screaming comes across the sky." with a dollar sign 
sentence = "A screaming comes across the sky.".replace("s", "$")
print(sentence)

# 7. Use a method to find the first index of the character "m" in the string "Hemingway". 

string_2 = "Hemingway".index("m")
print(string_2)

# 8. Find a dialogue in yoru favorite book (containg quotes) and turn it into a string 
# no. 

# 9. Create the string "three three three" using concatenation and then again using multiplication 
string_3 = 'three' 
string_3 = string_3 + ' ' + string_3 + ' ' + string_3
print(string_3)
string_3 = 'three '
string_3 = string_3 * 3
print(string_3)

# 10. Slice the string 
# "It was a bright cold day in April, and the clocks were striking thirteen." 
# to only include the characters before the comma. 

sentence = "It was a bright cold day in April, and the clocks were striking thirteen."
sentence = sentence[:34]
print(sentence)
