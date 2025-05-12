import re

def main():
    print(count(input("Text: ")))

def count(s):
    # Use regular expression to match "um" as a standalone word
    # r'\bum\b' ensures "um" is surrounded by word boundaries
    # re.IGNORECASE makes the match case-insensitive
    return len(re.findall(r'\bum\b', s, re.IGNORECASE))

if __name__ == "__main__":
    main()
