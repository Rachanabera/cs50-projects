def main():
    # Prompt the user for input (camelCase string)
    camel_case = input("Enter variable name in camel case: ").strip()

    # Convert camel case to snake case
    snake_case = convert_to_snake_case(camel_case)

    # Output the result in snake_case
    print(snake_case)

def convert_to_snake_case(camel_case):
    snake_case = []

    for i, char in enumerate(camel_case):
        # If the character is uppercase, convert to lowercase and add an underscore
        if char.isupper():
            if i > 0:  # Don't add an underscore at the beginning
                snake_case.append('_')
            snake_case.append(char.lower())
        else:
            snake_case.append(char)

    # Join the list into a string and return it
    return ''.join(snake_case)

if __name__ == "__main__":
    main()
