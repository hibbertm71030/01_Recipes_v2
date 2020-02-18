# to do

# ask user for servings made by recipe (and check this is a number more than 0.25
# ask user for servings desired (check this is a number)
# calculate the scale factor
# warn the user if the sf is less than 0.25 or more than 4

# functions go here



# main routine goes here

serving_size = float(input("What is the recipe serving size? "))
desired_size = float(input("How many servings are needed "))

scale_factor = desired_size / serving_size

print("Scale Factor: {}" .format(scale_factor))