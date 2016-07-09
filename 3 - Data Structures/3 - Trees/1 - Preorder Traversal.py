"""
Complete the preOrder function in your editor below, which has  parameter: a pointer to the root of a binary tree.
It must print the values in the tree's preorder traversal as a single line of space-separated values.
"""


class BinaryTreeNode(object):
	def __init__(self, data=None, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right


def traverse_pre_order_recursive(root):
	if root:
		print(root.data, end=" ")
		traverse_pre_order_recursive(root.left)
		traverse_pre_order_recursive(root.right)


def traverse_pre_order_iterative(root):
	if root:
		stack = [root]
		while stack:
			node = stack.pop()
			print(node.data, end=" ")
			if node.right:
				stack.append(node.right)
			if node.left:
				stack.append(node.left)


root = BinaryTreeNode("A")
root.left = BinaryTreeNode("B")
root.left.left = BinaryTreeNode("C")
root.left.right = BinaryTreeNode("D")
root.right = BinaryTreeNode("E")
root.right.left = BinaryTreeNode("G")
root.right.right = BinaryTreeNode("F")

traverse_pre_order_iterative(root)
