"""
 Print elements of a linked list in reverse order as standard output
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
	   self.data = data
	   self.next = next_node

 
"""

def ReversePrint(head):
	if head:
		stack = [head]
		while stack[-1].next:
			node = stack[-1]
			stack.append(node.next)
		while stack:
			node = stack.pop()
			print(node.data)


def Recursive_ReversePrint(head):
	if head:
		ReversePrint(head.next)
		print(head.data)
