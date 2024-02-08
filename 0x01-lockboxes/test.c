#include <stdio.h>
#include <stdlib.h>

#define TABLE_SIZE 10

// Structure to represent a key-value pair
struct KeyValue {
    int key;
    int value;
    struct KeyValue* next;
};

// Structure to represent the hash table
struct HashTable {
    struct KeyValue* table[TABLE_SIZE];
};

// Hash function to determine the index in the hash table
int hashFunction(int key) {
    return key % TABLE_SIZE;
}

// Function to insert a key-value pair into the hash table
void insert(struct HashTable* hashTable, int key, int value) {
    int index = hashFunction(key);

    // Create a new key-value pair
    struct KeyValue* newNode = malloc(sizeof(struct KeyValue));
    newNode->key = key;
    newNode->value = value;
    newNode->next = NULL;

    // Insert the new node at the beginning of the linked list
    newNode->next = hashTable->table[index];
    hashTable->table[index] = newNode;
}

// Function to search for a key in the hash table
int search(struct HashTable* hashTable, int key) {
    int index = hashFunction(key);

    // Search for the key in the linked list at the specified index
    struct KeyValue* current = hashTable->table[index];
    while (current != NULL) {
        if (current->key == key) {
            return current->value;  // Key found, return the corresponding value
        }
        current = current->next;
    }

    return -1;  // Key not found
}

int main() {
    // Create and initialize the hash table
    struct HashTable myHashTable;
    for (int i = 0; i < TABLE_SIZE; i++) {
        myHashTable.table[i] = NULL;
    }

    // Insert key-value pairs into the hash table
    insert(&myHashTable, 42, 100);
    insert(&myHashTable, 17, 200);
    insert(&myHashTable, 29, 300);

    // Search for keys in the hash table
    int result1 = search(&myHashTable, 42);
    int result2 = search(&myHashTable, 17);
    int result3 = search(&myHashTable, 29);

    // Print the results
    printf("Value for key 42: %d\n", result1);
    printf("Value for key 17: %d\n", result2);
    printf("Value for key 29: %d\n", result3);

    // Remember to free allocated memory when you're done

    return 0;
}
