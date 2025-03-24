#include <stdlib.h>
#include "linked_list.h"

/***
    Description: Add a node at the front
    Time Complexity: O(1)
    Auxiliary Space: O(1)
***/
void ll_push(struct Node** head_ref, int new_data)
{
    struct Node* new_node = malloc(sizeof(struct Node));
    new_node->data = new_data;
    new_node->next = (*head_ref);
    (*head_ref) = new_node;
}

/***
    Description: Add a node after a given node
    Time Complexity: O(1)
    Auxiliary Space: O(1)
***/
void ll_insert_after(struct Node* prev_node, int new_data)
{
    if (prev_node == NULL) {
        return;
    }
    struct Node* new_node = malloc(sizeof(struct Node));
    new_node->data = new_data;
    new_node->next = prev_node->next;
    prev_node->next = new_node;
}

/***
    Description: Add a node at the end
    Time complexity: O(N)
    Auxiliary Space: O(1)
***/
void ll_append(struct Node** head_ref, int new_data)
{
    struct Node* new_node = malloc(sizeof(struct Node));
    struct Node *last = *head_ref;

    new_node->data = new_data;
    new_node->next = NULL;

    if (*head_ref == NULL)
    {
        *head_ref = new_node;
        return;
    }

    while (last->next != NULL)
    {
        last = last->next;
    }

    last->next = new_node;
    return;
}

/***
    Description: Free all nodes in list
    Time Complexity: O(N)
***/
void ll_delete(struct Node** plist)
{
    struct Node* tmp;
    struct Node* list = *plist;

    while (list != NULL) {
        tmp = list;
        list = list->next;
        free(tmp);
    }

    *plist = NULL;
}

/***
    Description: Count number of nodes
    Time Complexity: O(N)
***/
int ll_length(struct Node* list)
{
    int len = 0;

    while (list != NULL) {
        len++;
        list = list->next;
    }

    return len;
}

struct Node* ll_tail(struct Node* head)
{
    if (head == NULL) {
        return head;
    }

    while (head->next != NULL) {
        head = head->next;
    }

    return head;
}

void ll_merge(struct Node* head, struct Node* tail)
{
    if (head == NULL) {
        return;
    }

    head = ll_tail(head);
    head->next = tail;
}

struct Node* ll_access(struct Node* head, int pos)
{
    if (head == NULL) {
        return head;
    }

    for (int i = 0; i < pos; i++) {
        head = head->next;
    }
    return head;
}

/***
    Description: Split a list
    pos: from 1->N-1: return tail
         else: keep head and return NULL
    Return: tail
***/
struct Node* ll_split(struct Node* head, int pos)
{
    struct Node* ret;
    int len = ll_length(head);

    if ((len < 1) || (pos < 1) || (pos >= len)) {
        return NULL;
    }

    pos = pos - 1;
    head = ll_access(head, pos);
    ret = head->next;

    head->next = NULL;
    return ret;
}


