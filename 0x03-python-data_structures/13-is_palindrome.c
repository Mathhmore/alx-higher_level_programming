#include "lists.h"

/**
 * count - counts number of elements in a singly linked list
 * @cm: list
 * Retern: count
 */
int count(listint_t *cm)
{
	int co;

	while (cm != NULL)
	{
		co++;
		cm = cm->next;
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
	int i = 0, counter, c, c1;
	listint_t *temp, *h, *cm;

	if (*head == NULL)
		return (1);

	temp = *head;
	h = *head;
	cm = *head;
	counter = count(cm);

	c = counter - 1;
	c1 = c * c;
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
