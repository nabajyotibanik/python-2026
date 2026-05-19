'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def deleteNode(self, head, x):
        #code here
        if x == 1:
            return head.next

        temp = head
        count = 1

        
        while temp is not None and count < x - 1:
            temp = temp.next
            count += 1

        
        if temp is not None and temp.next is not None:
            temp.next = temp.next.next

        return head
        
