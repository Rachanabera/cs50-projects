def convert(text):
    # Replace emoticons with emojis
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text

def main():
    # Prompt the user for input
    user_input = input("Enter text with emoticons: ")
    # Convert and print result
    print(convert(user_input))

# Call the main function
main()
