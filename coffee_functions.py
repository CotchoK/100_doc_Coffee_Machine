# TODO: 3. on order check if there are sufficient resource to make the item.
# TODO: 3.1 if not then indicate insufficient resources
def is_resources_sufficient(water_level, milk_level, coffee_level, selection):
    sufficient_resources = True
    if water_level < selection['water']:
        print("Sorry there is not enough water. Please replenish")
        sufficient_resources = False
    if milk_level < selection['milk']:
        print("Sorry there is not enough milk. Please replenish")
        sufficient_resources = False
    if coffee_level < selection['coffee']:
        print("Sorry there is not enough coffee. Please replenish")
        sufficient_resources = False

    return sufficient_resources


# TODO: 4 PROCESS COINS: ask user to enter a quantity of each denomination
def request_payment():
    quarts = int(input("Please enter number of quarters paid: ")) * 0.25
    dims = int(input("Please enter number of dimes paid: ")) * 0.1
    nicks = int(input("Please enter number of nickels paid: ")) * 0.05
    pens = int(input("Please enter number of pennies paid: ")) * 0.01

    return quarts + dims + nicks + pens


# TODO: 4.1 if funds insufficient advise user funds insufficient then refund
def check_payment(payment, selection):
    income = 0
    if payment < selection['price']:
        print("\nSorry that's not enough money. Money refunded")
    elif payment > selection['price']:
        print(f"\nThank you for your payment. Your change is ${format(payment - selection['price'],'.2f')}")
        income = selection['price']
    elif payment == selection['price']:
        print(f"\nThank you for your payment")
        income = selection['price']

    return income


# TODO: 4.2 if funds sufficient, calculate change, update resources in machine, dispense and thank customer
def make_coffee(wtr, mlk, cff, selection, selection_name):
    new_water_level = wtr - selection['water']
    new_milk_level = mlk - selection['milk']
    new_coffee_level = cff - selection['coffee']

    print(f"Here is your {selection_name}. Enjoy!")

    return new_water_level, new_milk_level, new_coffee_level