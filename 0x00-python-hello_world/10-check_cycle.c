#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Checks if a singly-linked list contains a cycle.
 * @list: linked list checked.
 *
 * Return: If there is no cycle - 0 else - 1.
 */
int check_cycle(listint_t *list)
{
	listint_t *head, *link;
	/*check for errors*/
	if (list == NULL || list->next == NULL)
		return (0);

	head = list->next;
	link = list->next->next;

	while (head && link && link->next)
	{
		if (head == link)
			return (1);/*check for cycle*/

		head = link->next;
		link = link->next->next;/*preserve the link*/
	}

	return (0);
}
