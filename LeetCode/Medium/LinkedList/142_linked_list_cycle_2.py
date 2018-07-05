# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Hare and Tortoise Problem
        # https://www.youtube.com/watch?v=-YiQZi3mLq0

        if head is None or head.next is None:
            # There is no cycle when there are 0 or 1 elements in teh linked list
            return None

        # Initialize the slow and fast pointers
        slow = head
        fast = head

        while fast != None and fast.next != None:
            if fast is None or fast.next is None:
                # Means teh fast pointer has reached the end of teh linked list
                return None


            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                # Then there is a cycle
                # We need to find teh starting point of teh cycle
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next

                return fast

x1 = ListNode(1)
x2 = ListNode(4)
x3 = ListNode(3)
x4 = ListNode(2)


x1.next = x2
x2.next = x3
x3.next = x1

sol = Solution()
sol.detectCycle(x1)
