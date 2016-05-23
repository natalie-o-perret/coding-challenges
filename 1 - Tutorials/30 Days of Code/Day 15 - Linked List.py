class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 


class Solution: 
    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    #Complete this method
    def insert(self, head, data): 
        node = Node(data)
        if head is None:
            head = node
        else:
            current = head
            while(current.next is not None):
                current = current.next
            current.next = node
        return head

mylist= Solution()
T = int(input())
head = None
for i in range(T):
    data = int(input())
    head = mylist.insert(head, data)    
mylist.display(head);     