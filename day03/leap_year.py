# Leap year project
print("Welcome Leap Year Project")
year = int(input("Which year do you want check : "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
            input(">")
        else:
            print("Not Leap!")       
    else:
        print("Leap year.")
else:
    print("Not Leap!")
   