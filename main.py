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


# TODO: 1. variables for resources of the coffee machine
# define and initialise variables
water = 300
milk = 200
coffee = 100
money = 0.0

# TODO: 2. ability to print a report on remaining resource in the machine, and money
response = input("What would you like? (espresso, latte, cappuccino)? ")

if response == "report":
    # print a report of resources remaining
    print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}")
elif response == "espresso":
    exit()
    # check resources
    # ask money
    # check money
    # update resources (make coffee)
    # print enjoy coffee
elif response == "latte":
    exit()
    # check resources
    # ask money
    # check money
    # update resources (make coffee)
    # print enjoy coffee
elif response == "cappuccino":
    exit()
    # check resources
    # ask money
    # check money
    # update resources (make coffee)
    # print enjoy coffee
elif response == "off":
    exit()


# TODO: 3. on order check if there are sufficient resource to make the item.
# TODO: 3.1 if not then indicate insufficient resources
# TODO: 3.2 if there are sufficient resource to make the drink, process coins

# TODO: 4 PROCESS COINS: ask user to enter a quantity of each denomination
# TODO: 4.1 if funds insufficient advise user funds insufficient then refund
# TODO: 4.2 if funds sufficient, calculate change, update resources in machine, dispense and thank customer