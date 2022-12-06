# Create a letter using starting_letter.docx
import os
#for each name in invited_names.text
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

# Get the current working directory
os.chdir(r"/Users/mahan/Desktop/100DaysOfCodePython-master/day24/mail_merge")

PLACEHOLDER ="[name]"

with open("./input/Names/invitied_names.txt") as names_file:
    names = names_file.readlines()

with open("input/Letters/starting_letter.docx") as letter_file:
    contents = letter_file.read()

for name in names:
    stripped_name = name.strip()
    new_letter = contents.replace(PLACEHOLDER, stripped_name)
    with open(f"./output/ReadyToSend/letter_for_{stripped_name}.docx", "w") as completed_letter:
        completed_letter.write(new_letter)





