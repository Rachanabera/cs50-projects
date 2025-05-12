import string

# Function to count letters, words, and sentences
def count_text(text):
    letters = 0
    words = 0
    sentences = 0

    # Loop through the text to count letters, words, and sentences
    for char in text:
        if char.isalpha():
            letters += 1
        elif char in string.punctuation:  # Check for sentence-ending punctuation
            if char in ['.', '!', '?']:
                sentences += 1

    # Split the text into words (spaces between words) and count them
    words = len(text.split())

    return letters, words, sentences

# Main function
def main():
    # Prompt the user for input
    text = input("Text: ")

    # Count the letters, words, and sentences
    letters, words, sentences = count_text(text)

    # Calculate L and S
    L = (letters / words) * 100
    S = (sentences / words) * 100

    # Calculate the Coleman-Liau index
    index = 0.0588 * L - 0.296 * S - 15.8

    # Round the result to the nearest integer
    grade = round(index)

    # Print the grade level
    if grade >= 16:
        print("Grade 16+")
    elif grade < 1:
        print("Before Grade 1")
    else:
        print(f"Grade {grade}")

if __name__ == "__main__":
    main()
