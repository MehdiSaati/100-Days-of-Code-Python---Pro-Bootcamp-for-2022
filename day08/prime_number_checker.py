# Prime number checker
n = int(input("Check this number : "))

def prime_checker(number):
    is_prime = True
    for i in range(2, number-1):
        if number % i == 0:
           is_prime = False

    if is_prime :
        print("It's a prime bumber.")
    else:
        print("It's not a prime number!")
prime_checker(number=n)
input(">")