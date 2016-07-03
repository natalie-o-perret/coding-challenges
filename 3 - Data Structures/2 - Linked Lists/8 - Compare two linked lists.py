"""
 Merge two linked list
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""


def recursive_compare(head_a, head_b):
	if not head_a and not head_b:
		# return True
		return 1
	elif (head_a and head_b) and (head_a.data == head_b.data):
		return recursive_compare(head_a.next, head_b.next)
	else:
		# return False
		return 0


def iterative_compare(head_a, head_b):
	node_a = head_a
	node_b = head_b
	while True:
		if not node_a and not node_b:
			# return True
			return 1
		elif (node_a and node_b) and (node_a.data == node_b.data):
			node_a = node_a.next
			node_b = node_b.next
		else:
			# return False
			return 0
