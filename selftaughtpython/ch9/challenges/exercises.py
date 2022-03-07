# 1. Find a file on your coputer and print its contents using Python 
with open("file1.txt", "r") as f: 
    print(f.read())

# 2. Write a program that asks a user a question, and saves their answers to a file. 
user_input = input(("Input some text: \n"))

with open("user.txt", "w+") as user_f: 
    user_f.write(user_input)

# 3. Take the items in this list of lists:
# [["Top Gun", "Risky Business", "Minority Report"] "[Titanic", "The Revenant", "Inception"], ["Training Day", "Man on Fire", "Flight"]]
# write them to a csv file 
# the data from each list should be a row in the file, with each item in the list separate by a comma 
import csv

csv_list = [["Top Gun", "Risky Business", "Minority Report"], 
            ["Titanic", "The Revenant", "Inception"], 
            ["Training Day", "Main on Fire", "Flight"]]

with open("file3.csv", "w", newline='') as f:
    w = csv.writer(f, delimiter=",")
    w.writerows(csv_list)

# another way to do this 
import csv 

action_movies = [["Top Gun", "Risky Business", "Minority Report"], 
                 ["Titanic", "The Revenant", "Inception"], 
                 ["Training Day", "Main on Fire", "Flight"]]

with open("movies.csv", "w") as movies: 
    writer = csv.writer(movies, delimiter=",")
    for movie in action_movies: 
        writer.writerow(movie)
