import sys
import os

def main():
    # Check number of command-line arguments
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    filename = sys.argv[1]

    # Check if file is a Python file
    if not filename.endswith(".py"):
        sys.exit("Not a Python file")

    # Check if file exists
    if not os.path.isfile(filename):
        sys.exit("File does not exist")

    count = 0

    try:
        with open(filename, "r") as file:
            for line in file:
                stripped = line.strip()
                # Skip blank lines and lines that are comments
                if stripped == "" or stripped.startswith("#"):
                    continue
                count += 1
        print(count)
    except Exception as e:
        sys.exit(f"Error reading file: {e}")

if __name__ == "__main__":
    main()
