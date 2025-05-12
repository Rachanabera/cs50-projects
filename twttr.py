def main():
    word = input("Input: ")
    result = shorten(word)
    print(f"Output: {result}")

def shorten(word):
    vowels = "aeiouAEIOU"
    return ''.join([char for char in word if char not in vowels])

if __name__ == "__main__":
    main()
