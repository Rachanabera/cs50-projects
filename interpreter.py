def main():
    # Prompt the user for input
    expression = input("Expression: ").strip()

    # Split the expression into its components
    x, y, z = expression.split()

    # Convert x and z to integers
    x = int(x)
    z = int(z)

    # Perform the calculation based on the operator y
    if y == "+":
        result = x + z
    elif y == "-":
        result = x - z
    elif y == "*":
        result = x * z
    elif y == "/":
        result = x / z

    # Print the result formatted to one decimal place
    print(f"{result:.1f}")


# Ensure that the main function is called when the program runs
if __name__ == "__main__":
    main()
