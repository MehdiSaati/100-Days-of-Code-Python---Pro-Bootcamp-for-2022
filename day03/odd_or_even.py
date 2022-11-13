# project odd or even number
number = input("Which number do you want to check ? \n")
number_as_int = int(number)
# Even number can be divided by 2 whit no remainder
c = number_as_int % 2
if c == 0 :
    print("This is a even number.")
    input(">")
else:
    print("This is an odd number.")
    input(">")