"""
Insert Node at the end of a linked list.
Head pointer input could be None as well for empty list
"""
from . import Node


def tail_insert_iterative(head, data):
	node = Node(data)
	if head:
		current = head
		while current.next:
			current = current.next
		current.next = node
	else:
		head = node
	return head


def tail_insert_recursive(head, data):
	if not head:
		return Node(data)
	else:
		if head.next:
			tail_insert_recursive(head.next, data)
		else:
			head.next = Node(data, None)
		return head

