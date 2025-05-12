import sys
import os
import csv
from tabulate import tabulate

def main():
    # Check for the correct number of arguments
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    filename = sys.argv[1]

    # Check if it's a .csv file
    if not filename.lower().endswith(".csv"):
        sys.exit("Not a CSV file")

    # Check if file exists
    if not os.path.isfile(filename):
        sys.exit("File does not exist")

    try:
        with open(filename, newline='') as file:
            reader = csv.reader(file)
            table = list(reader)

            # First row is the header
            headers = table[0]
            rows = table[1:]

            # Print the formatted table
            print(tabulate(rows, headers, tablefmt="grid"))

    except Exception as e:
        sys.exit(f"Error reading file: {e}")

if __name__ == "__main__":
    main()
