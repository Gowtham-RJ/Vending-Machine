from resource import MENU, resources


def insert_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters: ")) * 0.25
    dimes = int(input("How many dimes: ")) * 0.10
    nickles = int(input("How many nickles: ")) * 0.05
    pennies = int(input("How many pennies: ")) * 0.01
    total = quarters + dimes + nickles + pennies
    return total


def remaining_water(total_water, orders_water):
    final_water = total_water - orders_water
    return final_water


def remaining_milk(total_milk, orders_milk):
    final_milk = total_milk - orders_milk
    return final_milk


def remaining_coffee(total_coffee, orders_coffee):
    final_coffee = total_coffee - orders_coffee
    return final_coffee


water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]
money = 0

end = False
print("Welcome to Coffee Vending Machine")
while not end:
    order = input("What would you like? (espresso/latte/cappuccino): ")

    espresso_water = MENU["espresso"]["ingredients"]["water"]
    espresso_coffee = MENU["espresso"]["ingredients"]["coffee"]
    espresso_cost = MENU["espresso"]["cost"]

    latte_water = MENU["latte"]["ingredients"]["water"]
    latte_coffee = MENU["latte"]["ingredients"]["coffee"]
    latte_milk = MENU["latte"]["ingredients"]["milk"]
    latte_cost = MENU["latte"]["cost"]

    cappuccino_water = MENU["cappuccino"]["ingredients"]["water"]
    cappuccino_coffee = MENU["cappuccino"]["ingredients"]["coffee"]
    cappuccino_milk = MENU["cappuccino"]["ingredients"]["milk"]
    cappuccino_cost = MENU["cappuccino"]["cost"]

    if order == "report":
        print(f"Water: {water}ml")
        print(f"Milk: {milk}ml")
        print(f"Coffee: {coffee}mg")
        print(f"Money: ${money}")
    elif order == "espresso":
        if espresso_water <= water and espresso_coffee <= coffee:
            amount = insert_coins()
            water = remaining_water(water, espresso_water)
            coffee = remaining_coffee(coffee, espresso_coffee)
            if espresso_cost < amount:
                change = amount - espresso_cost
                change = round(change, 2)
                print(f"Here is your ${change} change.")
                print("Here is your Espresso, Enjoy!")
                money += MENU["espresso"]["cost"]
            else:
                print("Sorry Not enough coins.")
        else:
            print("Sorry Not Enough Water.")
    elif order == "latte":
        if latte_water <= water and latte_coffee <= coffee and latte_coffee <= milk:
            amount = insert_coins()
            water = remaining_water(water, latte_water)
            milk = remaining_milk(milk, latte_milk)
            coffee = remaining_coffee(coffee, latte_coffee)
            if latte_cost < amount:
                change = amount - latte_cost
                change = round(change, 2)
                print(f"Here is your ${change} change.")
                print("Here is your Latte, Enjoy!")
                money += MENU["latte"]["cost"]
            else:
                print("Sorry Not enough coins.")
        else:
            print("Sorry Not Enough Water.")
    elif order == "cappuccino":
        if cappuccino_water <= water and cappuccino_coffee <= coffee and cappuccino_coffee <= milk:
            amount = insert_coins()
            water = remaining_water(water, cappuccino_water)
            milk = remaining_milk(milk, cappuccino_milk)
            coffee = remaining_coffee(coffee, cappuccino_coffee)
            if cappuccino_cost < amount:
                change = amount - cappuccino_cost
                change = round(change, 2)
                print(f"Here is your ${change} change.")
                print("Here is Cappuccino, Enjoy!")
                money += MENU["cappuccino"]["cost"]
            else:
                print("Sorry Not enough coins.")
        else:
            print("Sorry Not Enough Water.")
    else:
        print("Come back again")
        end = True
