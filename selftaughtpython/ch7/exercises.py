# 1. Print each item in the following list: 
# ["The Walking Dead", "Entourage", "The Sopranos", "The Vampire Diaries"]
tv_shows = ["The Walking Dead", 
            "Entourage", 
            "The Sopranos", 
            "The Vampire Diaries"]
for show in tv_shows: 
    print(show)

# 2. Print all the numbers from 25 to 50 
for i in range(25, 51):
    print(i)

# 3. Print each item in the list from the first challenge and their indexes 
for i, show in enumerate(tv_shows):
    print(i)
    print(show)

# 4. Write a program with an infite loop (with the option to type q to quit) 
# and a list of numbers.  Each time through the loop ask the user to guess a 
# number on the list and tell them whether or not they guessed correctly 
list_numbers = [38, 21, 66, 781]
while True: 
    print("Type q to quit...")
    guess = input("Guess a number: ")
    if guess == 'q': 
        break
    guess = int(guess)
    if guess in list_numbers:
        print("Correct, guess another...")
    else: 
        print("Incorrect, guess again...")

# 5. Multiply al the numbers in the list [8, 19, 148, 4] with all of the 
# numbers in the list [9, 1, 33, 83]
numbers1 = [8, 19, 148, 4]
numbers2 = [9, 1, 33, 83]
multiplied = []

for multiplicand in numbers1: 
    for multiplier in numbers2: 
        multiplied.append(multiplicand * multiplier)

print(multiplied)