class Solution:
    def insertPos(self, head, pos, val):
        new_node = Node(val)

        # Case 1: insert at beginning
        if pos == 1:
            new_node.next = head
            return new_node

        temp = head
        count = 1

        # move to (pos - 1)th node
        while temp is not None and count < pos - 1:
            temp = temp.next
            count += 1

        # insert new node
        new_node.next = temp.next
        temp.next = new_node

        return head
      
      