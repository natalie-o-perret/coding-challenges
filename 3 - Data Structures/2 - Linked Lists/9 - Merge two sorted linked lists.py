"""
 Merge two linked lists
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""


class Node(object):
	def __init__(self, data=None, next_node=None):
		self.data = data
		self.next = next_node


def merge_lists(head_a, head_b):
	node_a = head_a
	node_b = head_b
	node = Node()
	while True:
		if node_a and node_b:
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
