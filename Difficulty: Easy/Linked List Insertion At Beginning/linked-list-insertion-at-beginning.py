"""
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
"""

class Solution:
    def insertAtFront(self, head, x):
        #code here
        new_node = Node(x)

        curr = head

        new_node.next = curr
        head = new_node

        return head
        
