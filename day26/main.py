# Walkthrough for the NATO Alphabet Project
import pandas
import os
os.chdir("/Users/mahan/Desktop/100DaysOfCodePython-master/day26/NATO-lphabet")

data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(data.to_dict())

#TODO 1. Create a dictionary in this format 
# {"A": "Alfa", "B":"Bravo"}
phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}
# print(phonetic_dict)

#TODO 2. Craate a list of the phonetic code words from a word that user inputs.
word = input("Enter a word : ").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)
