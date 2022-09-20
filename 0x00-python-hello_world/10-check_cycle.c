#include "lists.h"

/**
*check_cycle - checks for a cycle in a singly-linked list
*@list: the list to be checked
*
*Return: 0 if there is no cycle, 1 if there is a cycle
*/
int check_cycle(listint_t *list)
{
	int i = 0, ret;

	while (i <= list->n)
	{
		if (i == list->n)
		{
			if (list->next == NULL)
				ret = 0;
			else
				ret = 1;
			break;
		}
		i++;
		list = list->next;
	}

	return (ret);
}
