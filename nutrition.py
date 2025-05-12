def main():
    # Dictionary of fruits and their corresponding calorie values
    fruit_calories = {
        "apple": 130,
        "avocado": 50,
        "banana": 110,
        "blackberries": 43,
        "blueberries": 57,
        "cantaloupe": 50,
        "cherries": 100,
        "coconut": 200,
        "cranberries": 46,
        "grapefruit": 60,
        "grapes": 90,
        "kiwifruit": 90,
        "lemon": 15,
        "mango": 150,
        "nectarine": 60,
        "orange": 80,
        "peach": 59,
        "pear": 100,
        "pineapple": 50,
        "plum": 70,
        "strawberries": 50,
        "sweet cherries": 100
    }

    # Prompt for the fruit input
    fruit = input("Enter a fruit: ").strip().lower()

    # Check if the fruit is in the dictionary
    if fruit in fruit_calories:
        print(f"Calories: {fruit_calories[fruit]}")
    # If the fruit is not in the dictionary, do nothing
    else:
        pass

# Run the program
main()
