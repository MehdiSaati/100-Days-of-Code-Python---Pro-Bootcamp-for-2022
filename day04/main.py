# Rock Paper Scissors
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# put them into a list for easier access
game_image = [rock, paper, scissors]
# change the data type now
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors."))
print("You Choice : \n")
print(game_image[user_choice])
# computer's choice
computer_choice = random.randint(0, 2)
print("Computer Choice :")
print(game_image[computer_choice])

# cases when the player wins: (rock and scissors) or (paper and rock) or (scissors and paper)
# evaluate the result
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
elif user_choice == 0 and computer_choice == 2:
    print("Result : \n")
    print('''
    
           _       
 __      _(_)_ __  
 \ \ /\ / / | '_ \ 
  \ V  V /| | | | |
   \_/\_/ |_|_| |_|
                   

    ''')
elif user_choice == 2 and computer_choice == 0:
    print("You Lose")
elif user_choice < computer_choice :
    print("You Lose")
elif user_choice > computer_choice :
    print("Result : \n")
    print('''
    
           _       
 __      _(_)_ __  
 \ \ /\ / / | '_ \ 
  \ V  V /| | | | |
   \_/\_/ |_|_| |_|
                   

    ''')
elif user_choice == computer_choice :
    print("It's a draw")

input(">")