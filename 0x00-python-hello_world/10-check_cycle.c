#include "lists.h"

/**
*check_cycle - checks for a cycle in a singly-linked list
*@list: the list to be checked
*
*Return: 0 if there is no cycle, 1 if there is a cycle
*/
int check_cycle(listint_t *list)
{
	int i = 0, j = 0, ret;

	while (list)
	{
		j++;
		list = list->next;
	}

	while (list)
	{
		if (i == j && list->next == NULL)
		{
			ret = 0;
			break;
		}
		else
		{
			ret = 1;
			break;
		}
		i++;
		list = list->next;
	}

	return (ret);
}
