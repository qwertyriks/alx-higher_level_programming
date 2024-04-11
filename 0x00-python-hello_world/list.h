#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * the struct listint_s - singly linkedd list
 *
 * @n: integer pointer
 *
 * @next: it points to the next node in line
 *
 * Description: singly linked list alx  node structure
 *
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);

listint_t *add_nodeint(listint_t **head, const int n);
void free_listint(listint_t *head);

int check_cycle(listint_t *list);

#endif /* LISTS_H */
