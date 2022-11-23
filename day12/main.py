#  Number Guessing Game version 1
from art import logo
import random
print(logo)
print("Welcome to the Number Guessing Game!")
rand_number = random.randint(1, 100)
print("I'm thinking of a number between 1 and 100.")
print(rand_number)
level = ["easy", "hard"]
choise_level = input("Choose a difficulty. Type 'easy' or 'hard' : ")
if choise_level == "easy":
    number_of_guess = 10
elif choise_level == "hard":
    number_of_guess = 5
else:
    print("Invalid entery!")

def check_number():
    print(f"You have {number_of_guess} attempts remaing to guess the number.")
    guess = int(input("Make a guess : "))
    if guess == rand_number:
       return "You win" 
    elif guess > rand_number:
       return "Too heigh"
    elif guess < rand_number:
       return "Too low" 

while number_of_guess > 0 :
    result_game = check_number()
    print (result_game)
    if result_game == "You win":
        break
    number_of_guess -= 1

print("play again??")
input(">")