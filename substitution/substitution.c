#include <stdio.h>
#include <string.h>
#include <ctype.h>

// Function to encrypt the message using the substitution cipher
void encrypt(char *plaintext, char *key) {
    for (int i = 0; plaintext[i] != '\0'; i++) {
        if (isalpha(plaintext[i])) {  // Check if character is a letter
            char base = isupper(plaintext[i]) ? 'A' : 'a'; // Handle uppercase and lowercase
            int index = plaintext[i] - base; // Get the index in the alphabet (0-25)
            char encrypted_char = key[index]; // Get the corresponding character from the key

            // Ensure the case of the encrypted letter matches the original
            if (isupper(plaintext[i])) {
                encrypted_char = toupper(encrypted_char); // Make encrypted letter uppercase
            } else {
                encrypted_char = tolower(encrypted_char); // Make encrypted letter lowercase
            }

            plaintext[i] = encrypted_char; // Replace the character in the plaintext
        }
    }
}

int main(int argc, char *argv[]) {
    // Check if the key is provided as a command-line argument
    if (argc != 2) {
        printf("Usage: ./substitution key\n");
        return 1; // Return error if key is not provided
    }

    // Get the key from the command-line argument
    char *key = argv[1];

    // Validate the key: it must be 26 characters long and contain only alphabetic characters
    if (strlen(key) != 26) {
        printf("Key must contain 26 characters.\n");
        return 1;
    }

    for (int i = 0; i < 26; i++) {
        if (!isalpha(key[i])) {
            printf("Key must contain only alphabetic characters.\n");
            return 1;
        }
        key[i] = toupper(key[i]); // Convert the key to uppercase for consistency
    }

    // Check for duplicate characters in the key
    for (int i = 0; i < 25; i++) {
        for (int j = i + 1; j < 26; j++) {
            if (key[i] == key[j]) {
                printf("Key must not contain duplicate characters.\n");
                return 1;
            }
        }
    }

    // Prompt the user for the message to be encrypted
    char plaintext[1000];
    printf("Enter the message to encrypt: ");
    fgets(plaintext, sizeof(plaintext), stdin); // Get the message

    // Encrypt the message using the provided key
    encrypt(plaintext, key);

    // Print the encrypted message (ciphertext)
    printf("ciphertext: %s", plaintext);

    return 0;
}
