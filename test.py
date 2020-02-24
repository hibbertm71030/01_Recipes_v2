
# functions go here

# number checking function
def num_check(question):

    error = "Please enter a number that is more than zero"

    valid = False
    while not valid:
        try:
            response = float(input(question))

            if response <= 0:
                print(error)
            else:

                return response


        except ValueError:
            print(error)



# main routine goes here

serving_size = float(input("What is the recipe serving size? "))
desired_size = float(input("How many servings are needed "))
serving_size = num_check("What is the recipe serving size? ")
desired_size = num_check("How many servings are needed? ")

scale_factor = desired_size / serving_size
