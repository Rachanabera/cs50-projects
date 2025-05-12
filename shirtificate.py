from fpdf import FPDF
from PIL import Image

class Shirtificate(FPDF):
    def header(self):
        # Set font: Arial bold 24
        self.set_font("Arial", "B", 24)
        self.cell(0, 20, "CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align="C")

def main():
    name = input("Name: ")

    pdf = Shirtificate(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    # Load the shirt image and get size (for centering)
    image_path = "shirtificate.png"

    # Add shirt image (full width, scale to 190mm wide)
    pdf.image(image_path, x=10, y=40, w=190)

    # Set font for name
    pdf.set_font("Arial", "B", 24)
    pdf.set_text_color(255, 255, 255)  # White text

    # Overlay name on shirt (approximate position)
    pdf.set_xy(0, 110)
    pdf.cell(210, 20, f"{name} took CS50", align="C")

    # Output PDF
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
