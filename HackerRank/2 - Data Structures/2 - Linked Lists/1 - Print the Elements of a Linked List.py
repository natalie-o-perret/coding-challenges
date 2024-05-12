"""
Print elements of a linked list on console.
Head input could be None as well for empty list
"""
from . import Node


def print_list_iterative(head):
	if head:
		current = head
		while current:
			print(current.data)
			current = current.next


def print_list_recursive(head):
	if head:
		print(head.data)
		print_list_recursive(head.next)
