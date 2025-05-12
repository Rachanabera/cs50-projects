import sys
import csv

# Helper function to find the longest run of an STR in a DNA sequence
def longest_match(sequence, subsequence):
    max_run = 0
    subsequence_length = len(subsequence)

    for i in range(len(sequence)):
        count = 0
        # Look for a consecutive match of subsequence
        while sequence[i:i+subsequence_length] == subsequence:
            count += 1
            i += subsequence_length

        max_run = max(max_run, count)

    return max_run

def main():
    # Ensure the correct number of command-line arguments
    if len(sys.argv) != 3:
        print("Usage: python3 dna.py data.csv sequence.txt")
        sys.exit(1)

    # Read the command-line arguments
    csv_filename = sys.argv[1]
    dna_filename = sys.argv[2]

    # Read the CSV file
    with open(csv_filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        # Store the STR sequences and names
        str_list = reader.fieldnames[1:]  # Skip the 'name' column
        individuals = [row for row in reader]

    # Read the DNA sequence file
    with open(dna_filename, 'r') as dnafile:
        dna_sequence = dnafile.read().strip()

    # Compute the longest run for each STR
    str_counts = {}
    for str_sequence in str_list:
        str_counts[str_sequence] = longest_match(dna_sequence, str_sequence)

    # Check for a match in the CSV file
    for individual in individuals:
        match = True
        for str_sequence in str_list:
            if str_counts[str_sequence] != int(individual[str_sequence]):
                match = False
                break
        if match:
            print(individual["name"])
            return

    print("No match")

if __name__ == "__main__":
    main()
