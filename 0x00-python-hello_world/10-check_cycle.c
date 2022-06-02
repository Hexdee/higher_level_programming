#include "lists.h"
#include <stdlib.h>

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: the list to check
 *
 * Return: 1 if there's a cycle, 0 otherwise
 */

int check_cycle(listint_t *list)
{
	listint_t *c_node = NULL;

	if (!list)
		return (0);

	c_node = list;

	while (c_node)
	{
		if (is_cycle(c_node))
			return (1);
		c_node = c_node->next;
	}

	return (0);
}

/**
 * is_cycle - check if a singly linked node create a cycle
 * @node: the node to check
 *
 * Return: 1 if there's a cycle, 0 otherwise
 */

int is_cycle(listint_t *node)
{
	listint_t *start = node;

	node = node->next;
	while (node)
	{
		if (node == start)
			return (1);
		node = node->next;
	}
	return (0);
}
