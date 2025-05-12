from cs50 import get_int

# Main function
def main():
    # Prompt the user for the height, re-prompt if invalid
    while True:
        height = get_int("Height: ")  # Get input from the user
        # Check if the height is within the valid range
        if height < 1 or height > 8:
            print("Height must be between 1 and 8.")
        else:
            break  # Exit loop if input is valid

    # Loop through each row to print the half-pyramid
    for i in range(1, height + 1):
        # Print spaces for the left side and hashes for the pyramid blocks
        print(" " * (height - i) + "#" * i)

if __name__ == "__main__":
    main()
