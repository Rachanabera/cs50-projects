#include <stdio.h>

int main() {
    char name[50]; // Array to store the user's name

    // Prompt the user for their name
    printf("What is your name? ");
    scanf("%49s", name); // Reads up to 49 characters to avoid overflow

    // Print the personalized greeting
    printf("Hello, %s\n", name);

    return 0;
}
