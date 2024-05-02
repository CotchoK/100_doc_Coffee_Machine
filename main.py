# ########### Coffee Machine Program ###########

# makes 3 hot flavours (dictionary)
# espresso (50ml water, 18g coffee) $1.50
# latte (200ml water, 24g coffee, 150ml milk) $2.50
# cappuccino (250ml water, 24g coffee, 100ml milk) $3.00

# machine resource capacities
# 300ml water
# 200ml milk
# 100g coffee

# coin operated
# penny = 1c
# nickel = 5c
# dime = 10c
# quarter = 25c

# program requirements
# 1. print report (how much of the resources it has left, coins etc)
# 2. sufficient resource when user orders a drink (print notification of low resources)
# 3. process coins
# 4. check transaction is successful
# 5. make the coffee (and deduct the resources from totals)

# when user orders a coffee.
# print "Please insert coins."
# ask how many quarters, dimes, nickels, pennies (each on a separate line)
# if insufficient funds, money is refunded and drink not dispensed
# if sufficient funds, calc sum of coin values, calculate any change
# print here is your coffee (the actual name of the drink)

# ########### Coffee Machine Program ###########

# imports
import coffee_options as co
import coffee_functions as cf


# TODO: 1. variables for resources of the coffee machine
# define and initialise global variables
WATER_CAPACITY = 300
MILK_CAPACITY = 200
COFFEE_CAPACITY = 100


def run_coffee_machine():
    """
    The program that runs the coffee machine. Will loop as long as the machine is on.
    :return: n/a
    """

    # variables
    money = 0.0
    water = WATER_CAPACITY
    milk = MILK_CAPACITY
    coffee = COFFEE_CAPACITY
    machine_on = True

    while machine_on:

        # TODO: 2. ability to print a report on remaining resource in the machine, and money
        response = input("\nWhat would you like? (espresso, latte, cappuccino)? ")

        if response == "report":
            # print a report of resources remaining
            print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}")
        elif response == "off":  # this ends execution
            exit()
        elif response == "prices":
            cf.check_prices(co.coffee)
        elif response in co.coffee:
            # check resources
            if cf.is_resources_sufficient(water, milk, coffee, co.coffee[response]):
                # ask for payment
                payment_amt = cf.request_payment()
                # check money
                monies_paid = cf.check_payment(payment_amt, co.coffee[response])
                if monies_paid > 0:
                    money = monies_paid
                    # update resources (make coffee)
                    water, milk, coffee = cf.make_coffee(water, milk, coffee, co.coffee[response], response)
            else:
                resources_replenished = input("Enter 'y' after you have replenished supplies. "
                                              "Enter anything else to shut machine down. \n").lower()
                # crude replenishment functionality that expects that all resources are replenished
                if resources_replenished == 'y':
                    water = WATER_CAPACITY
                    milk = MILK_CAPACITY
                    coffee = COFFEE_CAPACITY
                else:
                    machine_on = False


run_coffee_machine()








