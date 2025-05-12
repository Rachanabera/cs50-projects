#include <stdio.h>
#include <string.h>
#include <ctype.h>

// Function to calculate the Scrabble score of a word
int calculate_score(const char* word) {
    // Define the Scrabble score for each letter
    int letter_values[26] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

    int score = 0;

    // Loop through each character in the word
    for (int i = 0; word[i] != '\0'; i++) {
        char ch = toupper(word[i]); // Convert character to uppercase for consistency

        // Check if the character is a letter and calculate its score
        if (ch >= 'A' && ch <= 'Z') {
            score += letter_values[ch - 'A']; // Subtract 'A' to get the index
        }
    }

    return score;
}

int main() {
    char player1_word[100], player2_word[100];

    // Prompt Player 1 for their word
    printf("Player 1, enter your word: ");
    scanf("%s", player1_word);

    // Prompt Player 2 for their word
    printf("Player 2, enter your word: ");
    scanf("%s", player2_word);

    // Calculate the scores for both players
    int player1_score = calculate_score(player1_word);
    int player2_score = calculate_score(player2_word);

    // Display the scores
    printf("Player 1's score: %d\n", player1_score);
    printf("Player 2's score: %d\n", player2_score);

    // Determine and display the winner
    if (player1_score > player2_score) {
        printf("Player 1 wins!\n");
    } else if (player2_score > player1_score) {
        printf("Player 2 wins!\n");
    } else {
        printf("Tie!\n");
    }

    return 0;
}
