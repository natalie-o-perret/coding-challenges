class Node(object):
	def __init__(self, data=None, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right


def traverse_recursive_preorder(node):
	if node:
		yield node.data
		yield from traverse_recursive_preorder(node.left)
		yield from traverse_recursive_preorder(node.right)


def traverse_iterative_preorder(node):
	if node:
		stack = [node]
		while stack:
			node = stack.pop()
			yield node.data
			if node.right:
				stack.append(node.right)
			if node.left:
				stack.append(node.left)


def traverse_recursive_inorder(node):
	if node:
		yield from traverse_recursive_inorder(node.left)
		yield node.data
		yield from traverse_recursive_inorder(node.right)


def traverse_iterative_inorder(node):
	if node:
		stack = []
		while stack or node:
			if node:
				stack.append(node)
				node = node.left
			else:
				node = stack.pop()
				yield node.data
				node = node.right


def traverse_recursive_postorder(node):
	if node:
		yield from traverse_recursive_postorder(node.left)
		yield from traverse_recursive_postorder(node.right)
		yield node.data


def traverse_iterative_postorder(node):
	if node:
		stack = []
		while stack or node:
			if node:
				stack.append(node)
				node = node.left
			else:
				# if right child exists and traversing node from left child, then move right
				node = stack[-1]
				yield node.data
				node = node.right


g = Node("G")
f = Node("F", None, g)
e = Node("E")
d = Node("D")
c = Node("C", f)
b = Node("B", d, e, )
a = Node("A", b, c)

print(*traverse_iterative_preorder(a), sep=", ")
print(*traverse_recursive_preorder(a), sep=", ")
print(*traverse_recursive_inorder(a), sep=", ")
print(*traverse_iterative_inorder(a), sep=", ")
