def add(*args):
    sum = 0
    # print(args)
    # print(type(args))
    # print(args[1])
    for number in args:
        sum += number
    return sum


print(add(5, 8, 4, 6, 5, 2, 3))


def calculate(n, **kwargs):
    print(kwargs)
    # print(type(kwargs))
    # print(kwargs["add"])
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(5, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get('seats')
my_car = Car(make="Nissan", model="GTR")
print(my_car.color)
input(">")



