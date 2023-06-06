#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/**
 * insert_node - inserts a node into a singly linked list
 * @head: head of the list
 * @number: number to be inserted
 * Return: the address of the new node, or NULL if it failed
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;
	current = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (current->n > number || *head == NULL)
	{
		new->next = *head;
		*head = new;
	}
	else
	{
		while (current->next != NULL && current->next->n < number)
		{
			current = current->next;
		}
		current->next = new;
	}
	return (new);
}
