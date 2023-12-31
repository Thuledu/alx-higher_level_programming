#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * checks_cycle - program checks if a linked list contains a cycle
 * @list: linked list to check
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */
int checks_cycle(listint_t *list)
{
	listint_t *fast, *slow;

	if (list == NULL || list->next == NULL)
	{
		return (0);
	}

	slow = list->next;
	fast = list->next->next;

	while (slow && fast && fast->next)
	{
		if (slow == fast)
		{
			return (1);
		}
		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}
