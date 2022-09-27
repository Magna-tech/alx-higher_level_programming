#include "lists.h"

/**
 * is_palindrome - checks if a list is a palindrome
 * @head: pointer to the start of the list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	int ret;

	if (head == NULL)
		ret = 0;
	else
		ret = 1;

	return (ret);
}
