#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

#define BLOCK_SIZE 512  // Define the size of each block (512 bytes, typically used in file systems)
#define JPG_HEADER_1 0xFF
#define JPG_HEADER_2 0xD8
#define JPG_HEADER_3 0xFF

int main(int argc, char *argv[])
{
    // Accept a single command-line argument
    if (argc != 2)
    {
        printf("Usage: ./recover FILE\n");
        return 1;
    }

    // Open the memory card file
    FILE *card = fopen(argv[1], "r");
    if (card == NULL)
    {
        printf("Could not open the file.\n");
        return 1;
    }

    // Create a buffer for a block of data (512 bytes)
    uint8_t buffer[BLOCK_SIZE];

    // Initialize a counter for the number of JPEG files
    int jpeg_count = 0;

    // Declare a file pointer for the current JPEG file being created
    FILE *jpg = NULL;

    // While there's still data left to read from the memory card
    while (fread(buffer, 1, BLOCK_SIZE, card) == BLOCK_SIZE)
    {
        // Check if the current block marks the start of a new JPEG file
        if (buffer[0] == JPG_HEADER_1 && buffer[1] == JPG_HEADER_2 && buffer[2] == JPG_HEADER_3)
        {
            // If a JPEG file is already open, close it
            if (jpg != NULL)
            {
                fclose(jpg);
            }

            // Create a new JPEG file with a proper filename (e.g., 000.jpg, 001.jpg, etc.)
            char filename[8]; // Filename will be of the form "000.jpg", "001.jpg", etc.
            sprintf(filename, "%03i.jpg", jpeg_count);
            jpg = fopen(filename, "w");

            // If the JPEG file could not be opened, print an error and exit
            if (jpg == NULL)
            {
                printf("Could not create the JPEG file.\n");
                return 1;
            }

            // Increment the JPEG counter for the next file
            jpeg_count++;
        }

        // If a JPEG file is open, write the current block to the file
        if (jpg != NULL)
        {
            fwrite(buffer, 1, BLOCK_SIZE, jpg);
        }
    }

    // Close the last JPEG file if it's open
    if (jpg != NULL)
    {
        fclose(jpg);
    }

    // Close the memory card file
    fclose(card);

    return 0;
}
