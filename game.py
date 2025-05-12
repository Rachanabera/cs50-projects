import random

# Function to get a valid positive integer
def get_positive_int(prompt):
    while True:
        try:
            n = int(input(prompt))
            if n > 0:
                return n
        except ValueError:
            pass

# Get level
level = get_positive_int("Level: ")

# Generate random number between 1 and level
secret = random.randint(1, level)

# Prompt user to guess until correct
while True:
    guess = get_positive_int("Guess: ")
    if guess < secret:
        print("Too small!")
    elif guess > secret:
        print("Too large!")
    else:
        print("Just right!")
        break
