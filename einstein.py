# Define the speed of light
c = 300000000

def main():
    # Prompt user for mass
    mass = int(input("Mass (in kg): "))
    # Calculate energy using E = mc^2
    energy = mass * c ** 2
    # Print energy as an integer
    print(energy)

# Call the main function
main()
