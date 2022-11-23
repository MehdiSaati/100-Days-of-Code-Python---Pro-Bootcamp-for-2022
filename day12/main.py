#  Number Guessing Game version 1
from art import logo
from art import win
from art import lose
import random
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# Funcation to check user's guess against actual answer
def check_annswer(guess, answer, turns):
    """ checkes answer against guess. returns rhe number of turns remaining."""
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")
        print(win)

# Make function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard' : ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():   
    # Chiising a random number between 1 and 100.
    print(logo)
    print("Welcome to the Number Guessing Game!")
    answer = random.randint(1, 100)
    print("I'm thinking of a number between 1 and 100.")
    # print(f"Passst, the correct answer is {answer}")

    turns = set_difficulty()
    # Repeat the guess funtionality if they get it wrong.
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaing to guess the number.")

        # Let the user guess a number
        guess = int(input("Make a guess : "))

        # Track th number of turns and reduce by 1 if they get it wrong.
        turns = check_annswer(guess, answer, turns)
        if turns == 0:
            print("You've run put of guesses, you lose.")
            print(lose)
            return
        elif guess != answer:
            print("Guess again.")
game()

