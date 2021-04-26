#include "lists.h"

/**
 * siguiente awdkjnakd
 * @origin: wopa
 * Return: 0  or 1
 */

listint_t *siguiente(listint_t *origin)
{
	return (origin->next);
}

/**
 * check_cycle awdkjnakd
 * @list: wopa
 * Return: 0  or 1
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (!list)
		return (0);

	while (fast && siguiente(fast))
	{
		slow = siguiente(slow);
		fast = siguiente(siguiente(fast));
		if (fast == slow)
			return (1);
	}
	return (0);
}
