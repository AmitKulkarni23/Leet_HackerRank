# Remove all elements from a linked list of integers that have value val.
#
# Example:
#
# Input:  1->2->6->3->4->5->6, val = 6
# Output: 1->2->3->4->5

#################

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """

        if not head:
            return None

        if head.val == val and head.next is None:
            # If there is only 1 element and that element == val
            return None

        dummy_node = ListNode(0)
        dummy_node.next = head
        head = dummy_node

        while dummy_node.next:
            if dummy_node.next.val == val:
                dummy_node.next = dummy_node.next.next
            else:
                dummy_node = dummy_node.next

        return head.next

    def printList(self, node):
        """
        Helper function to print teh linked list
        """
        temp = node

        while temp:
            print(temp.val)
            temp = temp.next


x1 = ListNode(1)
x2 = ListNode(2)
x3 = ListNode(6)
x4 = ListNode(3)
x5 = ListNode(4)
x6 = ListNode(5)
x7 = ListNode(6)


x1.next = x2
x2.next = x3
x3.next = x4
x4.next = x5
x5.next = x6
x6.next = x7
x7.next = None


sol = Solution()
sol.printList(x1)

print("################")

new_head = sol.removeElements(x1, 6)
print(sol.printList(new_head))
