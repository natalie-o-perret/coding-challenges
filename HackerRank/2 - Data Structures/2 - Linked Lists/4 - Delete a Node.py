"""
Delete Node at a given position in a linked list.
"""
from . import Node


def delete_iterative(head, position):
	if head:
		if position == 0:
			head = head.next
		else:
			previous = None
			current = head
			current_position = 0
			while (current_position < position) and (current.next is not None):
				previous = current
				current = current.next
				current_position += 1
			previous.next = current.next
	return head


def delete_recursive(head, position):
	if position == 0:
		return head.next
	else:
		head.next = delete_recursive(head.next, position - 1)
		return head
