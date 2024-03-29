#include "lists.h"

/**
*check_cycle - checks for a cycle in a singly-linked list
*@list: the list to be checked
*
*Return: 0 if there is no cycle, 1 if there is a cycle
*/
int check_cycle(listint_t *list)
{
	listint_t *i = list, *j = list;

	while (i && j && j->next)
	{
		i = i->next;
		j = j->next->next;
		if (i == j)
		{
			return (1);
		}
	}

	return (0);
}
