#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
int is_palindrome(listint_t **head)
{
    listint_t *last = *head;
    int c = 1;
    while (last->next != NULL)
    {
        last = last->next;
        c++;
    }
    printf("Hello World\n C Value: %d\n", c);
    return 1;
}   

/**
 * print_listint - prints all elements of a listint_t list
 * @h: pointer to head of list
 * Return: number of nodes
 */
size_t print_listint(const listint_t *h)
{
    const listint_t *current;
    unsigned int n; /* number of nodes */

    current = h;
    n = 0;
    while (current != NULL)
    {
        printf("%i\n", current->n);
        current = current->next;
        n++;
    }

    return (n);
}

/**
 * add_nodeint_end - adds a new node at the end of a listint_t list
 * @head: pointer to pointer of first node of listint_t list
 * @n: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */
listint_t *add_nodeint_end(listint_t **head, const int n)
{
    listint_t *new;
    listint_t *current;

    current = *head;

    new = malloc(sizeof(listint_t));
    if (new == NULL)
        return (NULL);

    new->n = n;
    new->next = NULL;

    if (*head == NULL)
        *head = new;
    else
    {
        while (current->next != NULL)
            current = current->next;
        current->next = new;
    }

    return (new);
}

/**
 * free_listint - frees a listint_t list
 * @head: pointer to list to be freed
 * Return: void
 */
void free_listint(listint_t *head)
{
    listint_t *current;

    while (head != NULL)
    {
        current = head;
        head = head->next;
        free(current);
    }
}
/**
 * main - check the code for
 *
 * Return: Always 0.
 */
int main(void)
{
    listint_t *head;

    head = NULL;
    add_nodeint_end(&head, 1);          // 1
    add_nodeint_end(&head, 17);         // 2
    add_nodeint_end(&head, 972);        // 3
    add_nodeint_end(&head, 50);         // 4
    add_nodeint_end(&head, 98);         // 5
    add_nodeint_end(&head, 98);         // 6
    add_nodeint_end(&head, 50);         // 7
    add_nodeint_end(&head, 972);        // 8
    add_nodeint_end(&head, 17);         // 9
    add_nodeint_end(&head, 1);          // 10
    // print_listint(head);

    is_palindrome(&head);

    free_listint(head);
    return 0;
}

