from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import art

money_mashine = MoneyMachine()
coffe_maker =CoffeeMaker()
menu = Menu()
is_on = True

print(art.logo)
while is_on:
    option = menu.get_items()
    choice = input(f"What would you like? {option} :")
    if choice == "off":
        print("goodbay")
        is_on = False
    elif choice == "report":
        coffe_maker.report()
        money_mashine.report()
    else:
        drink = menu.find_drink(choice) 
        print(drink)

    input(">")
