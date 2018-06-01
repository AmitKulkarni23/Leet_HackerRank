# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA and headB:
            a_len = self.get_list_length(headA)
            b_len = self.get_list_length(headB)

            # Now we need to traverse headA (alen - blen) steps forward
            if a_len < b_len:
                a_len, b_len = b_len, a_len
                headA, headB = headB, headA

            # Move headA (a_len - b_len) steps forward
            for i in range(a_len - b_len):
                headA = headA.next


            # Now perform intersection check
            for i in range(b_len):
                if headA == headB:
                    return headA

                headA = headA.next
                headB = headB.next


    def get_list_length(self, node):
        """
        Helper function to get the number of nodes in a linked list
        """
        count = 0
        while node:
            count += 1
            node = node.next

        return count
