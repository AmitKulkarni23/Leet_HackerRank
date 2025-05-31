# https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/description/
 

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        # 1. Edge Case – Empty List:
        #     Just create a new node that points to itself and return it.

        # 2. Traverse the list:
        #     Keep moving with curr = curr.next and look for the right place.
        #     Stop when:
        #         curr.val <= insertVal <= curr.next.val
        #         OR you're at the rotation point (curr.val > curr.next.val) and:

        #             insertVal >= curr.val (bigger than all values — should go after max)

        #             OR insertVal <= curr.next.val (smaller than all values — should go before min)

        #         If you come full circle without finding a place (i.e., all values are equal), insert anywhere.

        # Time Complexity - O(n) - traverse the whole list
        # Space COmplexity - O(1)

        new_node = Node(insertVal)

        if not head:
            # Circular linked list
            new_node.next = new_node
            return new_node
        
        cur = head

        while True:
            # Noraml ascending insert
            if cur.val <= insertVal <= cur.next.val:
                break

            # Pivot Point
            if cur.val > cur.next.val:
                if insertVal >= cur.val or insertVal <= cur.next.val:
                    break
            
            cur = cur.next

            if cur == head:
                # all values ar equal
                # you have come a full circle
                # insert anywhere
                break
        
        new_node.next = cur.next
        cur.next = new_node

        return head
        
