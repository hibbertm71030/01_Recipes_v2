# conversion function

# functions go here
def general_converter():

    if unit in unit_central:
        mult_by = unit_central.get(unit)
        amount = amount * mult_by
        print("amount in ml {}".format(amount))
    else:
        print("{} is unchanged".format(amount))

unit_central = {
    "tsp" : 5,
    "tbs" : 15,
    "cup" : 237,
    "ounce": 30,
    "oz": 30,
    "pint": 437,
    "quart": 946,
    "pound": 454,
}

keep_going = ""
while keep_going == "":
    amount = eval(input("how much? "))
    amount = float(amount)

    unit = input("unit? ")

    if unit in unit_central:
        mult_by = unit_central.get(unit)
        amount = amount * mult_by
        print("amount in ml {}".format(amount))
    else:
        print("{} is unchanged".format(amount))

    keep_going = input("<enter> or q ")