import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    # Regular expression to match IPv4 format
    if not re.match(r"^\d+\.\d+\.\d+\.\d+$", ip):
        return False

    # Split by dot and check each part
    parts = ip.split(".")
    if len(parts) != 4:
        return False

    for part in parts:
        if not part.isdigit():
            return False
        number = int(part)
        if number < 0 or number > 255:
            return False

    return True

if __name__ == "__main__":
    main()
