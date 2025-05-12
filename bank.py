def main():
    greeting = input("Greeting: ")
    print(value(greeting))

def value(greeting):
    greeting = greeting.lower()  # Convert the greeting to lowercase for case insensitivity

    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
