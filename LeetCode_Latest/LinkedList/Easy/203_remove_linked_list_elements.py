# https://leetcode.com/problems/remove-linked-list-elements/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        prev_head = ListNode(-1)
        prev_head.next = head

        iterator_node = prev_head

        while iterator_node.next:
            if iterator_node.next.val == val:
                iterator_node.next = iterator_node.next.next
            else:
                iterator_node = iterator_node.next
        
        return prev_head.next
        