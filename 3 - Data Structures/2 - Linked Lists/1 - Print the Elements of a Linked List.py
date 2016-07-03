"""
 Print elements of a linked list on console
 head input could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node
"""


def iterative_print_list(head):
	if head:
		current = head
		while current:
			print(current.data)
			current = current.next

def recursive_print_list(head):
	if head:
		print(head.data)
		if head.next:
			recursive_print_list(head.next)