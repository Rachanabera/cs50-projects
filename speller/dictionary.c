#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>
#include <strings.h>
#include <stdlib.h>
#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// Number of buckets in hash table (using 26 for simplicity)
const unsigned int N = 26;

// Hash table (bucket array)
node *table[N];

// Global variable to keep track of the number of words loaded
unsigned int word_count = 0;

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // Hash the word to get its hash value
    unsigned int index = hash(word);

    // Access the linked list at the hashed index
    node *cursor = table[index];

    // Traverse the linked list
    while (cursor != NULL)
    {
        // Compare the current node's word with the input word (case-insensitive)
        if (strcasecmp(cursor->word, word) == 0)
        {
            return true; // Word found
        }

        // Move to the next node
        cursor = cursor->next;
    }

    // If we reach here, the word is not in the dictionary
    return false;
}

// Hash function: hashes a word to a number
unsigned int hash(const char *word)
{
    unsigned long hash_value = 0;
    int i = 0;

    // Iterate over each character in the word
    while (word[i] != '\0')
    {
        // Add ASCII values of the characters (converted to lowercase for case-insensitivity)
        hash_value = (hash_value * 31 + tolower(word[i])) % N;
        i++;
    }

    // Return the computed hash value within the range of hash table size
    return hash_value % N;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // Open dictionary file
    FILE *source = fopen(dictionary, "r");
    if (source == NULL)
    {
        fprintf(stderr, "Could not open file %s.\n", dictionary);
        return false;
    }

    // Buffer to store each word
    char word[LENGTH + 1];

    // Read each word from the dictionary file
    while (fscanf(source, "%45s", word) != EOF)
    {
        // Create a new node for each word
        node *new_node = malloc(sizeof(node));
        if (new_node == NULL)
        {
            fclose(source);
            return false;
        }

        // Copy the word into the node
        strcpy(new_node->word, word);
        new_node->next = NULL;

        // Hash the word to find the hash table index
        unsigned int index = hash(word);

        // Insert the node into the hash table
        new_node->next = table[index];
        table[index] = new_node;

        // Increment the word count
        word_count++;
    }

    // Close the dictionary file
    fclose(source);
    return true;
}

// Returns the number of words in the dictionary, if loaded
unsigned int size(void)
{
    return word_count; // Return the precomputed count
}

// Unloads dictionary from memory, returning true if successful
bool unload(void)
{
    // Iterate over each bucket in the hash table
    for (int i = 0; i < N; i++)
    {
        // Get the head of the linked list at this bucket
        node *cursor = table[i];

        // Traverse the linked list and free each node
        while (cursor != NULL)
        {
            node *temp = cursor; // Save the current node
            cursor = cursor->next; // Move to the next node
            free(temp); // Free the saved node
        }
    }

    return true; // All memory successfully freed
}
