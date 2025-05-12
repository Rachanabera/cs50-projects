import sys
import os
from PIL import Image, ImageOps

def main():
    # Check for correct number of arguments
    if len(sys.argv) != 3:
        sys.exit("Too few command-line arguments" if len(sys.argv) < 3 else "Too many command-line arguments")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Allowed extensions
    allowed_exts = [".jpg", ".jpeg", ".png"]

    # Extract and normalize extensions
    input_ext = os.path.splitext(input_file)[1].lower()
    output_ext = os.path.splitext(output_file)[1].lower()

    # Check for valid extensions
    if input_ext not in allowed_exts or output_ext not in allowed_exts:
        sys.exit("Invalid output")

    # Check if extensions match
    if input_ext != output_ext:
        sys.exit("Input and output have different extensions")

    # Check if input file exists
    if not os.path.isfile(input_file):
        sys.exit("Input does not exist")

    try:
        # Open the input image and shirt overlay
        input_image = Image.open(input_file)
        shirt = Image.open("shirt.png")

        # Resize and crop the input image
        input_image = ImageOps.fit(input_image, shirt.size)

        # Paste the shirt onto the input image using shirt as mask
        input_image.paste(shirt, (0, 0), shirt)

        # Save the final image
        input_image.save(output_file)

    except Exception as e:
        sys.exit("An error occurred")

if __name__ == "__main__":
    main()
