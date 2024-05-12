"""
Complete the preOrder function in your editor below, which has  parameter: a pointer to the root of a binary tree.
It must print the values in the tree's preorder traversal as a single line of space-separated values.
"""
from . import Node


def traverse_pre_order_recursive(root, action=print):
	if root:
		action(root.data, end=" ")
		traverse_pre_order_recursive(root.left, action)
		traverse_pre_order_recursive(root.right, action)


def traverse_pre_order_iterative(root, action=print):
	if root:
		stack = [root]
		while stack:
			node = stack.pop()
			action(node.data, end=" ")
			if node.right:
				stack.append(node.right)
			if node.left:
				stack.append(node.left)


root = Node("A")
root.left = Node("B")
root.left.left = Node("C")
root.left.right = Node("D")
root.right = Node("E")
root.right.left = Node("G")
root.right.right = Node("F")

traverse_pre_order_iterative(root)
