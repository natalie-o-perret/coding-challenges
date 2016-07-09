"""
Insert Node at the begining of a linked list head input could be None as well for empty list
"""


def insert(head, data):
	node = Node(data)
	node.next = head
	return node
