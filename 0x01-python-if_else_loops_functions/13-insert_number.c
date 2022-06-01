#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: pointer to the head of the linked list
 * @number: the number to be inserted
 *
 * Return: pointer to the new node or NULL on failure
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *c_node = NULL, *tmp = NULL;

	if (!head)
		return (NULL);

	if (!*head)
	{
		tmp = malloc(sizeof(listint_t));
		tmp->n = number;
		tmp->next = NULL;
		*head = tmp;
		return (tmp);
	}
	
	c_node = *head;
	while (c_node && c_node->next)
	{
		if (c_node->n > number)
		{
			tmp = malloc(sizeof(listint_t));
			tmp->n = c_node->n;
			tmp->next = c_node->next;
			c_node->n = number;
			c_node->next = tmp;
			return (tmp);
		}
		c_node = c_node->next;
	}

	tmp = malloc(sizeof(listint_t));
	tmp->n = number;
	tmp->next = NULL;
	c_node->next = tmp;

	return (tmp);
}
