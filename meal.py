def main():
    # Prompt the user for input
    time = input("Enter the time: ").strip()

    # Convert the time to a floating-point number representing the hour
    hours = convert(time)

    # Check the time range and output the corresponding meal time
    if 7 <= hours <= 8:
        print("breakfast time")
    elif 12 <= hours <= 13:
        print("lunch time")
    elif 18 <= hours <= 19:
        print("dinner time")

def convert(time):
    # Split the time into hours and minutes
    hours, minutes = map(int, time.split(":"))

    # Convert the time to a floating-point number representing the hours
    return hours + minutes / 60.0

if __name__ == "__main__":
    main()
