"""
 Delete Node at a given position in a linked list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method. 
"""

def Delete(head, position):
	if head:
		if position == 0:
			head = head.next
		else:
			previous = None
			current = head
			current_position = 0
			while (current_position < position) and (current.next is not None):
				previous = current
				current = current.next
				current_position += 1
			previous.next = current.next
	return head

def Recursive_Delete(head, position):
	if position == 0:
		return head.next
	else:
		head.next = Recursive_Delete(head.next, position - 1)
		return head
