# ingredients list

# number checking function
def num_check(question):

    error = "Please enter a number that is more than zero"

    valid = False
    while not valid:
        response = (input(question))

        if response.lower() == "xxx":
            return "xxx"

        else:
            try:
                if float(response) <= 0:
                    print(error)
                else:
                    return response

            except ValueError:
                print(error)



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

# replace line below with component 3 in due course...
scale_factor = eval(input("Scale Factor: "))


# set up empty ingredient list
ingredients = []

# loop to ask users to enter an ingredient
stop = ""
while stop != "xxx":

    amount = num_check("what is the amount for the ingredient? ")


    # stop loop if exit code is typed and there are
    # more than 2 ingredients...
    if amount.lower() == "xxx" and len(ingredients) > 1:
        break

    elif amount.lower() == "xxx" and len(ingredients) <2:
        print("you need at least two ingredients in the list. "
              "please add more ingredients.")

    # if exit code is not entered, add ingredient to list
    else:
        # ask user for ingredient (via not blank function)
        get_ingredient = not_blank("Please type in an ingredient name: ",
                                   "This can't be blank",
                                   "yes")
        amount = float(amount) * scale_factor

        # remove decimal point for whole numbers
        if amount % 1 == 0:
            amount = int(amount)
        elif amount * 10 % 1 == 0:
            amount = "{:.1f}".format(amount)
        else:
            amount = "{:.1f}".format(amount)


        ingredients.append("{} units {}".format(amount, get_ingredient))

# output list
for item in ingredients:
    print(item)