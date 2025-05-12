import sys

# List to store names
names = []

try:
    while True:
        name = input("Name: ")
        names.append(name)
except EOFError:
    print()  # Move to next line after EOF

# Format the output
if len(names) == 1:
    output = names[0]
elif len(names) == 2:
    output = f"{names[0]} and {names[1]}"
else:
    output = ", ".join(names[:-1]) + f", and {names[-1]}"

print(f"Adieu, adieu, to {output}")
