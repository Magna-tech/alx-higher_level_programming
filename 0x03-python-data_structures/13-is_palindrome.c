#include "lists.h"

/**
 * is_palindrome - checks if a list is a palindrome
 * @head: pointer to the start of the list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (0);

	return (p_recursive(head, *head));

}


/**
 * p_recursive - Helper function to recursively check palindrome.
 * @left: Pointer to the left side of the linked list.
 * @right: Pointer to the right side of the linked list.
 *
 * Return: 1 if palindrome, 0 otherwise.
 */
int p_recursive(listint_t **left, listint_t *right)
{
	if (right == NULL)
		return (1);

	int result = p_recursive(left, right->next);

	if (!result)
		return (0);

	result = (right->n == (*left)->n);

	*left = (*left)->next;

	return (result);
}
