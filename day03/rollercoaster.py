# rollercoaster project
print(" Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
# check user height
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    # check age for pay
    if age < 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry, you have to grow taller before you can ride.")