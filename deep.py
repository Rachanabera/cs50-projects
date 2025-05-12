# Prompt the user
answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

# Normalize the input by stripping whitespace and converting to lowercase
answer = answer.strip().lower()

# Check if the answer is 42, forty-two, or forty two
if answer == "42" or answer == "forty-two" or answer == "forty two":
    print("Yes")
else:
    print("No")
