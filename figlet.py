import sys
import random
from pyfiglet import Figlet

figlet = Figlet()

# Handle 0 or 2 arguments
if len(sys.argv) == 1:
    font = random.choice(figlet.getFonts())
elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"]:
    if sys.argv[2] in figlet.getFonts():
        font = sys.argv[2]
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")

# Prompt user for input
text = input("Input: ")

# Set font and print output
figlet.setFont(font=font)
print("Output:")
print(figlet.renderText(text))
