import random
import hangman_art

# word_list = ["ardvark", "baboon", "camel"]
# instad import hangman_words
from hangman_words import word_list

# randomly choose a word the word_list
# assign it to a variable caleed chosen_word
chosen_word = random.choice(word_list)
chosen_word_len = len(chosen_word)

# create an empty list called display
# for each letter in the chose_word, add a "_" to display
lives = 6
display = []
for letter in range(chosen_word_len):
    display.append("_")

# Start Game Logo
print(hangman_art.logo)
# ask the user to guess a letter and assign their answer to a variable called guess. 
# make guess a lowercase
end_of_game = False
while not end_of_game :
    guess = input("Guess a letter : ").lower()
    #if the user has enterd a letter already guessed the letter
    if guess in display:
      print(f"Youve already gussed {guess}")
    # check if the letter the user guessed (guess) is one of the letter in the chosen_word
    for position in range(chosen_word_len):
        letter = chosen_word[position]
        if letter == guess:
            # print("Right")
            display[position] = letter
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
    print(display)
    if "_" not in display:
        end_of_game = True
        print("\n You Win")
    # User live status
    print(hangman_art.stages[lives])
input(">")