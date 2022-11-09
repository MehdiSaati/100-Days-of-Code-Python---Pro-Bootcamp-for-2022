# Mehdi Saati
print("Wellcome to the mehdi saati first project")

# initialize the variable as empty string

name = ""
city = ""

# simple check to make sure the user has entered somthing

while True:
    print("Please entered your name?")
    name = input("> ")
    #if there's no input, ask again
    if name == "":
        print("you haven't entered anything. Please try again")
    #if there's any input at all, break out of the loop
    else:
         break
    # do the some for city name
while True:
    print("what's your citeis name?")
    city =input("> ")
    if city == "":
        print("You haven't entered anything. Please try again.")
    else:
         break
# output using f-string makes the code much more readable
print(f"Your name {name} and your city {city}.")


