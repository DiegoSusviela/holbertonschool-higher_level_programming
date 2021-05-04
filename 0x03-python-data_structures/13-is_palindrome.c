#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * rev - asdasd
 * @head: asdasd
 *
 * Return: asdasd
 */
listint_t *rev(listint_t **head)
{
	listint_t *ant = NULL, *sig = NULL;

	while (*head)
	{
		sig = (*head)->next;
		(*head)->next = ant;
		ant = *head;
		*head = sig;
	}
	*head = ant;
	return (*head);
}

/**
 * is_palindrome - asdasd
 * @head: asdasd
 *
 * Return: asdasd
 */


int is_palindrome(listint_t **head)
{
	listint_t *loc1 = *head, *loc2 = *head, *aux = NULL;
	
	if (!*head)
		return (1);

	while (loc1->next && loc1->next->next)
	{
		loc2 = loc2->next;
		loc1 = loc1->next->next;
	}
	loc2 = rev(&loc2);
	aux = loc2;
	loc1 = *head;

	while (loc1 && loc2)
	{
		if (loc2->n != loc1->n)
			return (0);
		loc2 = loc2->next;
		loc1 = loc1->next;
	}
	rev(&aux);
	return (1);
}