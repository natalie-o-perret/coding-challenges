"""
Print elements of a linked list in reverse order as standard output.
Head could be None as well for empty list.
"""
from . import Node


def print_reverse_iterative(head):
	if head:
		stack = [head]
		while stack[-1].next:
			node = stack[-1]
			stack.append(node.next)
		while stack:
			node = stack.pop()
			print(node.data)


def print_reverse_recursive(head):
	if head:
		print_reverse_iterative(head.next)
		print(head.data)
