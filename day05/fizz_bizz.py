# Fizz Buzz Exercise
print("Wellcome to Fizz Buzz")
for number in range (1, 101):
    # Divisble by both 3 and 5
    if number % 3 == 0 and number % 5 == 0 :
        print("FizzBuzz")
    # Divisible by 3
    if number % 3 == 0:
        print("Fizz")
    # Divisible by 3
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
input(">")