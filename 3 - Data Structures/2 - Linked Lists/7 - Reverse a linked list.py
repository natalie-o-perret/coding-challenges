"""
Reverse a linked list, head could be None as well for empty list
Return back the head of the linked list in the below method.
"""
from . import Node


def reverse_iterative(head):
	# e.g. A > B > C > D
	if head:
		current_node = head  # current = A
		next_node = current_node.next  # next = A.next = B
		current_node.next = None  # A > None
		while next_node:
			tmp = next_node.next  # tmp = B.next = C
			next_node.next = current_node  # B.next = current = A
			head = current_node = next_node  # head = current = B
			next_node = tmp  # next = tmp = C
	return head


def reverse_stack(head):
	# e.g. A > B > C > D
	if head:
		stack = [head]
		while stack[-1].next:
			node = stack[-1]
			stack.append(node.next)
		# stack = [D, C, B, A]
		head = stack.pop()  # head = D
		current = head  # current = head = D
		while stack:
			node = stack.pop()  #
			current.next = node
			current = current.next
		current.next = None
	return head


def reverse_recursive(head):
	if not head:
		return head
	else:
		head = reverse_recursive(head.next)
	return head
