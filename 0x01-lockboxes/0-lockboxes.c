#include <stdio.h>
#include <stdlib.h>

/**
 * Functions
 * One to populate the listOfBoxes
 * One to populate the listOfKeys for each box
 * One to print for checking
 */
/*
typedef struct keysInABox
{
	int key;
	struct keysInABox *next;
};

typedef struct listOfBoxes
{
	int index;
	struct listOfBoxes *next;
	struct listOfBoxes *prv;
	struct keysInABox *listOfKeys;
};


struct listOfBoxes populateList(int *array){
	int len = 0;
	struct listOfBoxes *head, *new;

	head = new = malloc(sizeof(struct listOfBoxes));
	for (len = 0; array[len] != NULL; len++)
	for (int i = 0; i < len; i++){
		new->index = 0;
		new->next = NULL;
		new->prv = head;
	}
	return *head;
}

int main(){
	struct listOfBoxes *list;

    int array[][3] = {{1, 4, 6}, {2}, {0, 4, 1}, {5, 6, 2}, {3}, {4, 1}, {6}};
	*list = populateList(array);
}
*/

struct Key{
	int key;
	struct key* next;
	struct key* prv;
};

struct HashTable{
	struct key* table[150];
};

void insert(int *array, struct HashTable* hashTable, int key){
	
}
