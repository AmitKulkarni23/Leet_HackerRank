# Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
#
# You should preserve the original relative order of the nodes in each of the two partitions.
#
# Example:
#
# Input: head = 1->4->3->2->5->2, x = 3
# Output: 1->2->2->4->3->5


#######################################

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head:
            return None

        if head.next is None:
            return head

        # Create 2 new nodes
        less_than = ListNode(0)
        # Preseerv teh heads
        less_than_head = less_than

        greater_than = ListNode(0)
        # Preserve teh head
        greater_than_head = greater_than

        cur = head

        while cur:
            if cur.val < x:
                less_than.next = cur
                less_than = cur
            else:
                greater_than.next = cur
                greater_than = cur

            cur = cur.next

        # Greater than head was initialized with 0
        # Therefore
        if greater_than_head.next:
            greater_than_head = greater_than_head.next
        else:
            greater_than_head = None

        # And make the last element in greater_than list to point to NULL
        greater_than.next = None


        # Finally link less_than linked list to greater_than linked list
        less_than.next = greater_than_head

        if less_than_head.next:
            less_than_head = less_than_head.next
            return less_than_head
        else:
            return greater_than_head


    def printList(self, node):
        """
        Helper function to print teh linked list
        """
        temp = node

        while temp:
            print(temp.val)
            temp = temp.next


x1 = ListNode(1)
x2 = ListNode(4)
x3 = ListNode(3)
x4 = ListNode(2)
x5 = ListNode(5)
x6 = ListNode(2)


x1.next = x2
x2.next = x3
x3.next = x4
x4.next = x5
x5.next = x6


sol = Solution()
sol.printList(x1)

print("###############")
new_head = sol.partition(x1, 3)

sol.printList(new_head)
