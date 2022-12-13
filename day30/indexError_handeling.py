# Index Error Handeling
fruits = ["Apple", "Pear", "Orange"]
#TODO: Catch the exception and make sure the code
def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("fruit pie")
    else:
        print(fruit + " pie")

make_pie(4)
 
