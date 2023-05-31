# load pickle
import pickle
import pprint

# Processing  --------------------------------------------------------------- #
class Recipe:  # Initialize the variables needed for the recipe class
    def __init__(self, recipe_name: str, ingredients: str, baking_time: float):
        self.recipe_name = recipe_name
        self.ingredients = ingredients
        self.baking_time = baking_time


def baking_with_pickles(recipe, file_name):  # write data obtained from recipe class to a binary file
    try:
        with open(file_name, "wb") as file:
            pickle.dump(recipe, file)
        print("Recipe saved using a pickle.\n")
    except IOError as e:  # exception to notify user if data was unable to be saved
        print("Error occurred while saving recipe: {e}")


# def pickle_to_text(recipe, file_name):  # convert pickle to a text file for user to view
#   open(file_name, "w")
#   pickle_data = pickle.dumps(recipe)
#    print(f"\nRecipe saved as text to {file_name}")
def pickle_to_text(recipe):
    unpickle = pickle.load(open('recipe.db', "rb"))
    with open('recipe.txt', "a") as f:
        pprint.pprint(unpickle, stream=f)
    print(f"\nRecipe saved as text to recipe.txt")

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


# Main body of script  --------------------------------------------------------------- #
# Get recipe details from the user
recipe = get_recipe()

# Save recipe to a pickle
baking_with_pickles(recipe, "recipe.db")
baking_with_pickles(recipe, "recipe.txt")

# Display data in pickle to user
display_recipe(recipe)

# Convert pickle to text file for user
pickle_to_text(recipe)

