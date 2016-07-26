"""
Insert Node at the beginning of a linked list head input could be None as well for empty list.
"""
from . import Node


def insert(head, data):
	node = Node(data)
	node.next = head
	return node
