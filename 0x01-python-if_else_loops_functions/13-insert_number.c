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
	listint_t *next_node = NULL, *tmp = NULL;

	if (head)
		next_node = *head;
	else
		return (NULL);

	while (next_node) 
	{
		if (next_node->n > number)
		{
			tmp = malloc(sizeof(listint_t));
			tmp->n = number;
			tmp->next = next_node->next;
			next_node->next = tmp;
			return (tmp);
		}
		next_node = next_node->next;
	}

	return (NULL);
}
