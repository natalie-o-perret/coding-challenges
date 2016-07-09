"""
Complete the preOrder function in your editor below, which has  parameter: a pointer to the root of a binary tree.
It must print the values in the tree's postorder traversal as a single line of space-separated values.
"""

class BinaryTreeNode(object):
	def __init__(self, data=None, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right


def traverse_in_order_recursive(root):
	if root:
		traverse_in_order_recursive(root.left)
		traverse_in_order_recursive(root.right)
		print(root.data, end=" ")


def traverse_in_order_iterative(root):
	if root:
		stack = [root]
		node = root
		while node:
			if node.left:
				stack.append(node)
				node = node.left
			else:
				print(node.data)
				node = stack.pop()


root = BinaryTreeNode("A")
root.left = BinaryTreeNode("B")
root.left.left = BinaryTreeNode("C")
root.left.right = BinaryTreeNode("D")
root.right = BinaryTreeNode("E")
root.right.left = BinaryTreeNode("G")
root.right.right = BinaryTreeNode("F")

traverse_in_order_iterative(root)
