#include "lists.h"
/**
  *insert_node - Inserts num to linked list
  *@head: Head pointer to the list
  *@number: Number inserted
  *
  *Return: Null if function fails else pointer to new Node
  */
linstint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *current;

	/*allocate memory and check for errors*/
	current = malloc(sizeof(listint_t));
	if (current == NULL)
	{
		return (NULL);
		free(current);
	}
	current->n = number;/*number is assigned to the new node*/

	if (node == NULL || node->n >= number)
	{
		/*add to the end of the new node*/
		current->next = node;
		*head = current;
		return (current);
	}
	while (node && node->next && node->next->n < number)
	/*add to the beginning*/
	node = node->next;
	current->next = node->next;
	node->next = current;

	return (current);
}
