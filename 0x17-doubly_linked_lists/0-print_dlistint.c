#include "lists.h"
#include <stdio.h>

/**
 * print_dlistint - will prints all elements of a dlistint_t list.
 * @h: is the head of a doubly linked list
 * Return: outputs the number of nodes
 */

size_t print_dlistint(const dlistint_t *h)
{
	const dlistint_t *ptr = h;
	size_t n = 0;

	while (ptr && ptr->prev)
		ptr = ptr->prev;
	while (ptr)
	{
		printf("%d\n", ptr->n);
		n++;
		ptr = ptr->next;
	}
	return (n);
}
