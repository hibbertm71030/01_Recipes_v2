# to do

# ask user for servings made by recipe (and check this is a number more than 0.25
# ask user for servings desired (check this is a number)
# calculate the scale factor
# warn the user if the sf is less than 0.25 or more than 4

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

dodgy_sf = "yes"
while dodgy_sf == "yes":

    serving_size = num_check("What is the recipe serving size? ")
    desired_size = num_check("How many servings are needed? ")

    scale_factor = desired_size / serving_size

    if scale_factor < 0.25:
        dodgy_sf = input("Warning: This scale is very small "
                      "and you may struggle to accurately weigh "
                      "ingredients. \n"
                      "Do you want to change this to make more servings? "
                      "(type 'yes' to change your desired serving size)") .lower()

    elif scale_factor > 4:
        dodgy_sf = input("Warning: This scale factor is quite large "
                      "and you may have issues with mixing bowl/oven space. \n"
                      "Do you want to change this to make a smaller batch? "
                         "(type 'yes' to change your desired serving size)") .lower()
    else:
        dodgy_sf = "no"

print("Scale Factor: {}".format(scale_factor))
