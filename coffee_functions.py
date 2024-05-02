# TODO: 3. on order check if there are sufficient resource to make the item.
# TODO: 3.1 if not then indicate insufficient resources
def is_resources_sufficient(water_level, milk_level, coffee_level, selection):
    """
    Checks to see if there are sufficient resources available to make the requested beverage.
    Will print message if certain resources are insufficient advising user to replenish resources
    :param water_level: the current water level of the coffee machine at the time of order
    :param milk_level: the current milk level of the coffee machine at the time of order
    :param coffee_level: the current coffee level in the coffee machine at the time of order
    :param selection: the coffee selected
    :return: boolean indicating if resources are sufficient or not
    """
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
    """
    Prompts user for the denominations of money added towards the payment of the coffee
    :return: sum of the payment made
    """
    quarts = int(input("Please enter number of quarters paid: ")) * 0.25
    dims = int(input("Please enter number of dimes paid: ")) * 0.1
    nicks = int(input("Please enter number of nickels paid: ")) * 0.05
    pens = int(input("Please enter number of pennies paid: ")) * 0.01

    return quarts + dims + nicks + pens


# TODO: 4.1 if funds insufficient advise user funds insufficient then refund
def check_payment(payment, selection):
    """
    Checks the amount paid against the cost of the coffee ordered
    :param payment: the payment amount paid by the customer
    :param selection: the coffee selected by the customer
    :return:
    """
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
    """
    Makes the coffee and updates the resources based on what was required to make the coffee ordered
    :param wtr: the water level of the coffee machine at the time of the order
    :param mlk: the milk level in the coffee machine at the time of the order
    :param cff: the coffee level in the coffee machine at the time of the order
    :param selection: the dictionary item (coffee) selected by the customer
    :param selection_name: the actual name of the coffee selected by the customer
    :return: the updated water, milk and coffee levels after making the coffee
    """
    new_water_level = wtr - selection['water']
    new_milk_level = mlk - selection['milk']
    new_coffee_level = cff - selection['coffee']

    print(f"Here is your {selection_name}. Enjoy!")

    return new_water_level, new_milk_level, new_coffee_level


def check_prices(coffees):
    """
    Checks the prices of the items available in the coffee machine to order
    :param coffees: the dictionary of coffees available
    :return: n/a
    """
    for key in coffees:
        print(f"{key} = ${format(coffees[key]['price'],'.2f')}")
