#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * insert_node - Program that inserts a number into a sorted singly-linked list.
 * @head: A pointer to the head of linked list.
 * @number: Number to insert.
 * Return: NULL (failure), Otherwise - a pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;
	listint_t *run;

	run = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
	{
		return (NULL);
	}
	new->n = number;

	if (node == NULL || node->n >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}

	while (run->next != NULL)
	{
		if ((run->next)->n >= number){
			new->next = run->next;
			run->next = new;
			return (new);}
		
		run = run->next;
	}
	new->next = NULL;
	run->next = new;
	return (new);
}

