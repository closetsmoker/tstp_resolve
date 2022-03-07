# 1. Modify the game, so a word is selected randomly from a list of words.
# we are going to create a list of words so it wont be "truly" random 
# but for the purpose of going through this exercise it should be fine.
import random

def hangman(): 
    word_list = ["momo", "vivvie", "bebop", "closet", "smoker"]
    random_number = random.randint(0, 4)
    word = word_list[random_number]
    wrong_guesses = 0
    stages = ["", "________      ", "|      |      ", "|      0      ", "|     /|\     ", "|     / \     ", "|"]
    remaining_letters = list(word)
    letter_board = ["__"] * len(word)
    win = False
    print("Welcome to Hangman")
    while wrong_guesses < len(stages) - 1:
        print("\n")
        guess = input("Guess a letter, lest your man hang!")
        if guess in remaining_letters:
            character_index = remaining_letters.index(guess)
            letter_board[character_index] = guess
            remaining_letters[character_index] = '$'
        else:
            wrong_guesses += 1
        print((" ".join(letter_board)))
        print("\n".join(stages[0: wrong_guesses + 1]))
        if "__" not in letter_board: 
            print("You win! The board was:")
            print(" ".join(letter_board))
            win = True
            break 
    if not win: 
        print('\n'.join(stages[0: wrong_guesses]))
        print('You lose! The word was {}'.format(word))

hangman()