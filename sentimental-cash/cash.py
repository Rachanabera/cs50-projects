# cash.py

# Function to get a valid user input
def get_valid_input():
    while True:
        try:
            # Prompt the user for how much change is owed (in dollars)
            change_owed = input("Change owed: ")

            # Check if input is empty
            if not change_owed:
                print("Invalid input. Please enter a valid amount.")
                continue

            # Convert the input to a float
            change_owed = float(change_owed)

            # Ensure the input is not negative
            if change_owed < 0:
                print("Invalid input. Please enter a positive value.")
                continue

            return change_owed
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

# Get the valid input from the user
change_owed = get_valid_input()

# Convert the amount to cents
cents = round(change_owed * 100)

# Initialize the coin count
coins = 0

# List of coin values in cents (quarters, dimes, nickels, pennies)
coin_values = [25, 10, 5, 1]

# Loop through each coin denomination and count the coins needed
for coin in coin_values:
    coins += cents // coin  # Add the number of coins of this denomination
    cents %= coin           # Reduce the remaining cents

# Output the minimum number of coins
print(coins)
