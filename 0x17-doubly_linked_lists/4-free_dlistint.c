#include "lists.h"
#include <stdlib.h>

/**
 * free_dlistint - will free a list
 * @head: head of list
 * Return: Void as nothing
 */

void free_dlistint(dlistint_t *head)
{
	dlistint_t *start, *check;

	start = head;
	while (start != NULL)
	{
		check = start->next;
		free(start);
		start = check;
	}
}
