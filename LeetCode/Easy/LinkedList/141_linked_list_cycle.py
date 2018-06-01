# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # Credits : https://leetcode.com/problems/linked-list-cycle/solution/

        if head is None or head.next is None:
            # No cycle ( for 0 or 1 elements)
            return False

        # Initialize the 2 pointers
        slow = head
        fast = head.next

        while slow != fast:
            if fast is None or fast.next is None:
                # That means teh fast pointer has reached teh end of the linked list and there was no cyc;e
                return False

            slow = slow.next
            fast = fast.next.next

        return True
