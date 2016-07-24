"""
Complete the preOrder function in your editor below, which has  parameter: a pointer to the root of a binary tree.
It must print the values in the tree's postorder traversal as a single line of space-separated values.
"""


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


root = Node("A")
root.left = Node("B")
root.left.left = Node("C")
root.left.right = Node("D")
root.right = Node("E")
root.right.left = Node("G")
root.right.right = Node("F")

traverse_in_order_iterative(root)
