"""
 Insert Node at the end of a linked list 
 head pointer input could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
	 def __init__(self, data=None, next_node=None):
			 self.data = data
			 self.next = next_node
 
 return back the head of the linked list in the below method
"""

def iterative_tail_insert(head, data):
		node = Node(data)
		if head:
				current = head
				while current.next:
						current = current.next
				current.next = node
		else:
				head = node
		return head

def recursive_tail_insert(head, data):
	if not head:
		return Node(data)
	else:
		if head.next:
			recursive_tail_insert(head.next, data)
		else:
			head.next = Node(data, None)
		return head