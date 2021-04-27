#include "lists.h"

/**
 * insert_node - awdad
 * @head: adad
 * @number: adada
 *
 * Return: returns
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *loc = *head;
	listint_t *nuevo = NULL;

	nuevo = malloc(sizeof(listint_t));
	if (!nuevo)
		return (NULL);

	nuevo->n = number;
	nuevo->next = NULL;
	if (!*head)
	{
		*head = nuevo;
		return (nuevo);
	}
	if (nuevo->n < loc->next->n)
	{
		nuevo->next = *head;
		*head = nuevo;
		return (nuevo);
	}
	while (loc->next != NULL && loc->next->n < nuevo->n)
		loc = loc->next;
	nuevo->next = loc->next;
	loc->next = nuevo;
	return (nuevo);
}
