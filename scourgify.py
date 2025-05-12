import csv
import sys

def main():
    # Check command-line arguments
    if len(sys.argv) != 3:
        sys.exit("Usage: python scourgify.py input.csv output.csv")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        students = []

        # Open and read the input CSV file
        with open(input_file, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Split the name into last and first, then rearrange
                last, first = row["name"].split(", ")
                students.append({
                    "first": first,
                    "last": last,
                    "house": row["house"]
                })

        # Write to the output CSV file
        with open(output_file, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
            writer.writeheader()
            for student in students:
                writer.writerow(student)

    except FileNotFoundError:
        sys.exit(f"Could not read {input_file}")

if __name__ == "__main__":
    main()
