"""
Merge two sorted linked lists.
Head could be None as well for empty list
"""
from . import Node


def merge_lists_iterative(head_a, head_b):
	node_a = head_a
	node_b = head_b
	pass


def merge_lists_recursive(head_a, head_b):
	if not head_a and not head_b:
		pass


# 1 -> 3 -> 5 -> 6 -> NULL
# 2 -> 4 -> 7 -> NULL

head_a = Node(1)
head_a.next = Node(3)
head_a.next.next = Node(5)
head_a.next.next.next = Node(6)

head_b = Node(2)
head_b.next = Node(4)
head_b.next.next = Node(7)
