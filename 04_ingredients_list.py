# ingredients list


# not blank function
def not_blank(question, error_msg, num_ok):
    error = error_msg

    valid = False
    while not valid:
        response = input(question)
        has_errors = ""

        if num_ok != "yes":
            # look at each character in string and if its a number
            for letter in response:
                if letter.isdigit() == True:
                    has_errors = "yes"
                    break

        if response == "":
            print(error)
            continue
        elif has_errors != "":
            print(error)
            continue
        else:
            return response
# main routine

# set up empty ingredient list
ingredients = []

# loop to ask users to enter an ingredient
stop = ""
while stop != "xxx":
    # ask user for ingredient (via not blank function)
    get_ingredient = not_blank("Please type in an ingredient name: ",
                               "This can't be blank",
                               "yes")

    # stop loop if exit code is typed and there are
    # more than 2 ingredients...
    if get_ingredient.lower() == "xxx" and len(ingredients) > 1:
        break

    elif get_ingredient.lower() == "xxx" and len(ingredients) <2:
        print("you need at least two ingredients in the list. "
              "please add more ingredients.")

    # if exit code is not entered, add ingredient to list
    else:
        ingredients.append(get_ingredient)

# output list
print(ingredients)