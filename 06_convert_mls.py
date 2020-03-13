
# Ask user for unit
# Check that unit is in dictionary

# If unit in dictionary, convert to mL

# If no unit given/unit is unknown, leave as is.

# Functions go here:
def unit_checker():
    unit_tocheck = input("Unit? ")

    # Abbreviation lists:
    teaspoon = ["tsp", "teaspoon", "t"]
    tablespoon = ["tbs", "tablespoon"," T"," tbsp"]
    cup = ["c", "cups", "C"]
    ounce = ["oz"]
    pint = ["p"]
    quart = ["q"]
    pound = ["lb", "lbs"]

    if unit_tocheck == "":
        print("You chose {}".format(unit_tocheck))
        return unit_tocheck
    elif unit_tocheck == "T" or unit_tocheck.lower() in tablespoon:
        return "tbs"
    elif unit_tocheck.lower() in teaspoon:
        return "tsp"
    elif unit_tocheck in cup:
        return "cup"
    elif unit_tocheck.lower() in ounce:
        return "ounce"
    elif unit_tocheck.lower() in pint:
        return "pint"
    elif unit_tocheck.lower() in quart:
        return "quart"
    elif unit_tocheck.lower() in pound:
        return "pound"

# Main routine goes here:
unit_central = {
    "tsp": 5,
    "tbs": 15,
    "cup": 237,
    "ounce": 28.35,
    "pint": 473,
    "quart": 946,
    "pound": 454
}

keep_going = ""
while keep_going == "":

    amount = eval(input("How much? "))
    amount = float(amount)

    unit = unit_checker()

    if unit in unit_central:
        mult_by = unit_central.get(unit)
        amount = amount * mult_by
        print("Amount in mL {:.2f}".format(amount))
    else:
        print("{} is unchanged".format(amount))

    keep_going = input("<enter> or q")