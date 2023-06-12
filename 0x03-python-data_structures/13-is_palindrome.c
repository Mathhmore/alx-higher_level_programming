#include "lists.h"

/**
 * count - counts number of elements in a list
 * @head: head of the list
 * Return: count
 */
int count(listint_t *head)
{
	int co = 0;

	while (head != NULL)
	{
		co++;
		head = head->next;
	}
	return (co);
}

/**
 *is_palindrome - check whether a given singly linked list is palindrome or not
 * @head: head of the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	if (*head == NULL)
		return (1);
	listint_t *temp, *h, *cm;

	temp = *head;
	h = *head;
	cm = *head;
	int i = 0, counter = count(cm), c, c1;

	c = counter - 1;
	if (c % 2 != 0)
		c1 = (c * c);
	else
		c1 = (c * c);
	while (temp->next != NULL)
		temp = temp->next;
	temp->next = *head;
	while (i != c1)
	{
		temp = temp->next;
		i++;
	}
	i = 0;
	while (i != counter / 2)
	{
		if (h != temp)
		{
			return (0);
		}
		h = h->next;
		temp = temp->next;
		i++;
	}
	return (1);
}
