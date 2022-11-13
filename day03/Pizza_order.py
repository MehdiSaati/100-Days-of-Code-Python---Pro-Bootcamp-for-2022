# Pizza Order
print("Welcome to Python Pizza Deliveries!")
bill = 0
size = input("What size pizza do you want? S, M or L\n").lower()
if size == "s":
    bill = 15
elif size == "m":
    bill = 20
elif size == "l":
    bill = 25
# add pepperoni check  
add_pepperoni = input("Do you want pepperoni? Y or N\n").lower()
if add_pepperoni == "y":
    if size == "s":
        bill = bill + 2
    else:
        bill = bill + 3
elif add_pepperoni == "n":
    print("dont pepporoni")
# add extera cheese check
extera_cheese = input("Do you want extera cheese? Y or N\n").lower()
if extera_cheese == "y":
    bill = bill + 1
# final bill
print(f"Your final bill is: ${bill}")
input(">")

 
