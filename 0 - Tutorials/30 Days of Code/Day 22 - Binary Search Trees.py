class Node:
    def __init__(self, data):
        self.right =self.left = None
        self.data = data


class Solution:
    def insert(self, root, data):
        if root == None:
            return Node(data)
        else:
            if data <= root.data:
                current = self.insert(root.left, data)
                root.left = current
            else:
                current = self.insert(root.right, data)
                root.right = current
        return root

    def getHeight(self, root):
        #Write your code here
        if root:
            left = 0
            right = 0
            if root.left:
                left = 1 + self.getHeight(root.left)
            if root.right:
                right = 1 + self.getHeight(root.right)
            return max(left, right)
        else:
            return 0

T = int(input())
myTree = Solution()
root = None
for i in range(T):
    data = int(input())
    root = myTree.insert(root, data)
height = myTree.getHeight(root)
print(height)       
