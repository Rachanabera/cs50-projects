import validators

def main():
    # Prompt the user for an email address
    email = input("Email: ")

    # Check if the email is valid using the validators library
    if validators.email(email):
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    main()
