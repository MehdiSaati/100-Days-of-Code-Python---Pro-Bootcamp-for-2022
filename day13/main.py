# ==========ORIGINAL===========
# Describe Problem
# def my_function():
#     for i in range(1, 20):
#         if i == 20 :
#             print("You got it")
# my_function()

# ==========DEBUGGED===========
# Describe Problem
# def my_function():
      # -------range(a, b) stops at "b - 1"-------
#     for i in range(1, 21):
#         if i == 20 :
#             print("You got it")
# my_function()

# ==========ORIGINAL===========
# Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num])

# ==========DEBUGGED===========
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# -------indices (a.k.a "indexes") in Python start from 0, so we need to either use (0, length)---------
# dice_num = randint(0, 5)
# print(dice_imgs[dice_num])

# ==========ORIGINAL===========
# Play Computer
# year = int(input("What's your year of birth? "))
# if year > 1980 and year <1994:
#     print("You are a millenial.")
# elif year > 1994 :
#     print("You are a Gen 2.")

# ==========DEBUGGED===========
# year = int(input("What's your year of birth? "))
# if year > 1980 and year <1994:
#     print("You are a millenial.")
# --------need to include "=" ---------
# elif year >= 1994 :
#     print("You are a Gen 2.")

# ==========ORIGINAL===========
# Fix the Errors
# age = input("How old are you? ")
# if age > 18:
# print("You are can drive at age {age}.")


# ==========DEBUGGED===========
# ------make sure the input is valid (int) -----------
# age = int(input("How old are you? "))
# if age > 18:
#     # --------need to turn this to an f-string so {age} is not treated as a simple string ------------
#     print(f"You are can drive at age {age}.")

# ==========ORIGINAL===========
# Print is your friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Nmber of words per page : "))
# total_words = pages * word_per_page
# print(total_words)

# ==========DEBUGGED===========
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
#  --------- "==" is a comparison operator, a simple assignment "=" is needed --------
# word_per_page = int(input("Nmber of words per page : "))
# total_words = pages * word_per_page
# print(f"Pages = {pages}")
# print(f"word_per_page = {word_per_page}")
# print(total_words)

# ==========ORIGINAL===========
# Use a Debugger
# def mutate(a_list):
#     b_list = []
#     for item in a_list:
#         new_item = item * 2
#     b_list.append(new_item)
#     print(b_list)
# mutate([1,2,3,5,8,13])

# ==========DEBUGGED===========
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        # ------fixed the indentation so this gets executed when it was intended ------
        b_list.append(new_item)
    print(b_list)
mutate([1,2,3,5,8,13])

input(">")