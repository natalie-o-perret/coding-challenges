class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 


class Solution: 
    def insert(self, head, data):
            p = Node(data)           
            if not head:
                head = p
            elif not head.next:
                head.next=p
            else:
                start = head
                while(not start.next):
                    start = start.next
                start.next = p
            return head  
    
    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def remove_duplicates(self, head):
        # Write your code here
        previous = head
        s = set()
        s.add(previous.data)
        current = previous.next
        while current:
            if current.data in s:
                previous.next = current.next
            else:
                s.add(current.data)
                previous = current
            current = current.next
        return head


mylist = Solution()
T = int(input())
head = None
for i in range(T):
    data = int(input())
    head = mylist.insert(head,data)    
head = mylist.remove_duplicates(head)
mylist.display(head)
