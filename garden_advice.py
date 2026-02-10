<<<<<<< HEAD
=======
# Gardening Advice App
# Variable to hold gardening advice
advice = ""

>>>>>>> 8e190d842facc3de9aa9fce5de95c83637e87c00
# Determine advice based on the season
# Function to determine gardening advice based on user input


def get_gardening_advice(season, plant_type):
    """
    This function takes the season and plant type and returns
    a combined string of gardening advice.
    """
    # Variable to hold gardening advice

    advice = ""

    # Determine advice based on the season
    if season == "summer":
        advice += "Water your plants regularly and provide some shade.\n"
    elif season == "winter":
        advice += "Protect your plants from frost with covers.\n"
    else:
        advice += "No advice for this season.\n"

    # Determine advice based on the plant type
    if plant_type == "flower":
        advice += "Use fertiliser to encourage blooms."
    elif plant_type == "vegetable":
        advice += "Keep an eye out for pests!"
    else:
        advice += "No advice for this type of plant."

    return advice

#  Main Program
#  Get User Input


user_season = input("Enter the current season "
                    "(summer/winter): ").lower().strip()
user_plant = input("Enter the plant type (flower/vegetable): ").lower().strip()

# 2. Call the function and store the result
final_advice = get_gardening_advice(user_season, user_plant)

# 3. Print the generated advice
print("\nYour Gardening Advice ")
print(final_advice)

# TODO: Examples of possible features to add:
# - Add detailed comments explaining each block of code.
# - Refactor the code into functions for better readability and modularity.
# - Store advice in a dictionary for multiple plants and seasons.
# - Recommend plants based on the entered season.
