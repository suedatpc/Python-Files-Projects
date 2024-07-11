from menu import MENU

money = 0

resources = {
    "water" : 300,
    "milk" : 200,
    "coffee" : 100,
}


def check_resources(ordered_coffee_ingredients):
    for item in ordered_coffee_ingredients:
        if ordered_coffee_ingredients[item] > resources[item]:
            print(f"There is not enough {item}.")
            return False
    return True


def take_coins():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_payment_enough(recieved_money, drink_cost):
    if recieved_money >= drink_cost:
        change = round(recieved_money - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global money
        money += drink_cost
        return True
    else:
        print("Sory that's not enough money. Money refunded.")
        return False
    

def make_coffee(drink_name, ordered_coffee_ingredients):
    for item in ordered_coffee_ingredients:
        resources[item] -= ordered_coffee_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")



is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "off":
        is_on = False
    
    elif choice == "report":
        print(f"Water: {resources['water']} ml")
        print(f"Milk: {resources['milk']} ml")
        print(f"Coffee: {resources['coffee']} ml")
        print(f"Money: ${money}")
    
    else:
        ordered_drink = MENU[choice]
        if check_resources(ordered_drink["ingredients"]):
            payment = take_coins()
            if is_payment_enough(payment, ordered_drink["cost"]):
                make_coffee(choice, ordered_drink["ingredients"])
            