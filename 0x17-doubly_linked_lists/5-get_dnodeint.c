#include "lists.h"

/**
 * get_dnodeint_at_index - gets the node by index
 * @head: header to list
 * @index: the index of element
 * Return: the element by index
 */

dlistint_t *get_dnodeint_at_index(dlistint_t *head, unsigned int index)
{
	unsigned int c;

	for (c = 0; c < index && head->next; c++)
	{
		head = head->next;
	}
	if (c < index)
		return (NULL);
	return (head);
}
