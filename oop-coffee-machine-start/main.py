from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu1 = Menu()
coffee = CoffeeMaker()
money = MoneyMachine()
is_on = True

while is_on:
    choice = input(f"Please enter your choice : {menu1.get_items()} :")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee.report()
        money.report()
    else:
        drink =menu1.find_drink(choice)
        print(drink)
        if coffee.is_resource_sufficient(drink) and money.make_payment(drink.cost):
                coffee.make_coffee(drink)
                coffee.report()
                money.report()


