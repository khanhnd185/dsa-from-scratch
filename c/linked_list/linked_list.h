#ifndef LINKED_LIST_H
#define LINKED_LIST_H

#include <stdint.h>

struct Node {
    int data; 
    struct Node *next; 
};

int ll_length(struct Node* list);
void ll_delete(struct Node** list);
void ll_push(struct Node** head_ref, int new_data);
void ll_insert_after(struct Node* prev_node, int new_data);
void ll_append(struct Node** head_ref, int new_data);
void ll_merge(struct Node* head, struct Node* tail);
struct Node* ll_split(struct Node* head, int pos);
struct Node* ll_access(struct Node* head, int pos);

#endif /* LINKED_LIST_H */
