def add(*args):
    sum = 0
    # print(args)
    # print(type(args))
    # print(args[1])
    for number in args:
        sum += number
    return sum


print(add(5, 8, 4, 6, 5, 2, 3))

