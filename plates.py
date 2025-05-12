import sys

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")
        sys.exit(1)  # This ensures the program exits with code 1


def is_valid(s):
    # Rule 1: Length must be between 2 and 6 characters
    if not (2 <= len(s) <= 6):
        return False

    # Rule 2: The plate must start with at least two letters
    if not s[:2].isalpha():
        return False

    # Rule 3: Numbers must come only at the end, and first number cannot be '0'
    number_started = False
    for char in s:
        if char.isdigit():
            if not number_started:
                number_started = True
                if char == '0':
                    return False
        elif number_started:
            return False  # letters after digits are not allowed

    # Rule 4: No periods, spaces, or punctuation (only alphanumeric)
    if not s.isalnum():
        return False

    return True


if __name__ == "__main__":
    main()
