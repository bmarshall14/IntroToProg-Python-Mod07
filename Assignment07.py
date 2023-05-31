# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Working with pickles and exceptions to store complex data
# Programmer: bmarshall
# Date: 29May2022
# ChangeLog (Who,When,What): none
# ---------------------------------------------------------------------------- #

# load pickle
import pickle


# Processing  --------------------------------------------------------------- #
class Recipe:  # Initialize the variables needed for the recipe class
    def __init__(self, recipe_name: str, ingredients: str, baking_time: float):
        self.recipe_name = recipe_name
        self.ingredients = ingredients
        self.baking_time = baking_time


def make_dictionary(recipe):  # Add recipe to dictionary
    recipe_dict = {
        'recipe_name': recipe.recipe_name,
        'ingredients': recipe.ingredients,
        'baking_time': recipe.baking_time
    }
    return recipe_dict


def baking_with_pickles(recipe, file_name):  # write data obtained from recipe class to a binary file
    try:
        with open(file_name, "wb") as file:
            pickle.dump(recipe, file)
        print("Recipe pickled.\n")
    except IOError as e:  # exception to notify user if data was unable to be saved
        print("Error occurred while saving recipe: {e}")


def save_dictionary_to_text(recipe_dict, file_name):  # write data obtained from recipe class to a binary file
    with open(file_name, "w") as file:
        for key, value in recipe_dict.items():
            file.write(key + ": " + str(value) + "\n")


# Presentation (input/output) --------------------------------------------------------------- #
def get_recipe():  # get data from user to pickle
    #
    recipe_name = input("Enter the name of the baked good item: ")
    ingredients = input("Enter the ingredients in your baked good: ")
    while True:
        baking_time = input("Enter the length it takes to bake a this item in minutes? ")
        try:
            baking_time = float(baking_time)
        except ValueError:  # exception to ensure user input data as float value
            print("Invalid baking time. Please enter a valid number.")
            continue
        else:
            break
    return Recipe(recipe_name, ingredients, baking_time)


def display_recipe(recipe):  # display recipe info back to user
    print("Recipe Details:")
    print(f"Name: {recipe.recipe_name}")
    print(f"Ingredients: {recipe.ingredients}")
    print(f"Baking Time: {recipe.baking_time} minutes")
    print("\nYou can also view your recipe by searching for the following file: recipe.txt" + "\n\nHappy baking!")


# Main body of script  --------------------------------------------------------------- #
# Get recipe details from the user
recipe = get_recipe()

# Create dictionary with user recipe
recipe_dict = make_dictionary(recipe)

# Pickle recipe data
baking_with_pickles(recipe_dict, "recipe.db")

# Display data in pickle to user
display_recipe(recipe)

# Save dictionary to txt file
save_dictionary_to_text(recipe_dict, "recipe.txt")


