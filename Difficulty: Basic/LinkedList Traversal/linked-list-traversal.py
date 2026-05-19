"""
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
"""

class Solution:
    def printList(self, head):
        # code here
        temp = head

        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        
        