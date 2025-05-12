def main():
    # Get user input
    dollars = input("How much was the meal? ")
    percent = input("What percentage would you like to tip? ")

    # Convert and calculate the tip
    tip = dollars_to_float(dollars) * percent_to_float(percent)

    # Display the result
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    # Remove the dollar sign and convert to float
    return float(d.replace("$", ""))

def percent_to_float(p):
    # Remove the percent sign and convert to float (divide by 100 to get decimal)
    return float(p.replace("%", "")) / 100

# Call main
main()
