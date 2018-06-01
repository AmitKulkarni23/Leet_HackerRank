# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # We will only iterate through the linked list is head is not null
        if head:
            current_node = head

            while current_node and current_node.next:
                if current_node.val == current_node.next.val:
                    current_node.next = current_node.next.next
                else:
                    current_node = current_node.next

            return head
