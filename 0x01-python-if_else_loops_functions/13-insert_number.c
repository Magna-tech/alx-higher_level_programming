#include "lists.h"

/**
 * insert_node - inserts new node to a list
 * @head: the current head of the list
 * @number: the number to be inserted
 *
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp;


	temp = malloc(sizeof(listint_t));
	if (temp == NULL)
		return (NULL);

	temp->n = number;
	temp->next = *head;
	*head = temp;

	return (temp);
}
