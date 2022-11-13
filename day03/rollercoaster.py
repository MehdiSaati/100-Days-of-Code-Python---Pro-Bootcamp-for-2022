# rollercoaster project
print(" Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
# check user height
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    # check age for pay
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age >= 45  and age <= 55:
        print("Everything is going to be ok. have a free ride on us")
    else:
        bill = 12
        print("Adult tickets are $12.")
    
    # Check take photo 
    wants_photo = input("Do you want a photo> Y or N. ").lower()
    if wants_photo == "y":
       bill = bill + 3
    
    print(f"Your final bill is ${bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")