#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <math.h>

// Function to calculate Coleman-Liau index
int calculate_grade_level(char text[]) {
    int letters = 0;
    int sentences = 0;
    int words = 1; // At least one word in any text

    int n = strlen(text);

    for (int i = 0; i < n; i++) {
        if (isalpha(text[i])) {
            letters++; // Count letters
        }
        if (text[i] == '.' || text[i] == '!' || text[i] == '?') {
            sentences++; // Count sentences
        }
        if (text[i] == ' ') {
            words++; // Count words
        }
    }

    // Calculate averages
    float L = (float)letters / words * 100; // Average number of letters per 100 words
    float S = (float)sentences / words * 100; // Average number of sentences per 100 words

    // Calculate Coleman-Liau index
    float index = 0.0588 * L - 0.296 * S - 15.8;

    // Return the rounded grade level
    return (int)round(index);
}

int main() {
    char text[1000];

    // Prompt user for input text
    printf("Text: ");
    fgets(text, sizeof(text), stdin); // Get the input text

    // Calculate the grade level
    int grade_level = calculate_grade_level(text);

    // Output based on grade level
    if (grade_level < 1) {
        printf("Before Grade 1\n");
    } else if (grade_level >= 16) {
        printf("Grade 16+\n");
    } else {
        printf("Grade %d\n", grade_level);
    }

    return 0;
}
