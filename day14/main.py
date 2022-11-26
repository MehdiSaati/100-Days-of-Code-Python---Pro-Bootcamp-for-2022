# Higher Lower Game
import art
import random
from game_data import data
from replit import clear

def format_data(account):
    """Take the account data and return the printable format."""
    account_name =  account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f" {account_name} a {account_description}, from {account_country} "

def check_answer(guess, a_followers, b_followers):
    """Take the user guess and follower count and return if they got it right."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


score = 0
game_should_continue = True
account_b = random.choice(data)
# Display art
print(art.logo)

# make the game repeatable.
while game_should_continue:
    # making account at position B become the next account at position A
    # Genrate a random account from rhe game data
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)
    
    # Formate the account data into printable format.
    print(f"Compare A :{format_data(account_a)}")
    print(art.vs)
    print(f"Compare A :{format_data(account_b)}")

    # Ask user for a guess.
    guess = input("How has more followers? Type 'A' or 'B': ").lower()


    # Check if user is correct.
    ## Get follower count of ech account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    ## user if statment to check if user is correct.
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

# clear the screen between rounds.
    clear()
    print(art.logo)

    # Give user feedback on their guess.
    # score keeping.
    if is_correct:
        score += 1
        print(f"You're right Current score : {score}")
    else:
        game_should_continue = False
        print(f"Dorry, tha's worng. Final score: {score}")




 