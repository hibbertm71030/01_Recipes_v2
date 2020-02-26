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


# loop to ask users to enter an ingredient

# ask user for ingredient (via not blank function)

# if exit code is typed...

# check that list contains at least 2 items

# if list contains at least 2 items break out of loop

# if exit code is not entered, add ingredient to list

# output list