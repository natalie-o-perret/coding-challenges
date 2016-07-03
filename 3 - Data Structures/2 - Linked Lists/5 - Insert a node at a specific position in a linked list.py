"""
 Insert Node at the end of a linked list
 head input could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method. 
"""

# This is a "method-only" submission.
# You only need to complete this method.
def insert(head, data, position):
	node = Node(data)
	if not head:
		head = node
	elif position == 0:
		node.next = head
		head = node
	else:
		previous = None
		current = head
		current_position = 0
		while (current_position < position) and current.next:
			previous = current
			current = current.next
			current_position += 1
		previous.next = node
		node.next = current
	return head
