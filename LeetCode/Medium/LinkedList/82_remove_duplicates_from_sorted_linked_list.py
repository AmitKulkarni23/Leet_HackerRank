# Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.
#
# Example 1:
#
# Input: 1->2->3->3->4->4->5
# Output: 1->2->5
# Example 2:
#
# Input: 1->1->1->2->3
# Output: 2->3

#######################

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head is None:
            return None

        if head.next is None:
            # If there is only 1 element in the linked list
            return head

        # Create a dummy node
        dummy = ListNode(0)
        dummy.next = head

        # This dummy node is your previous node
        # curr is pointing to head
        prev, cur = dummy, head

        # Iterate through all teh nodes
        while cur:
            if cur.next and cur.val == cur.next.val:
                rem_val = cur.val

                while cur and cur.val == rem_val:
                    cur = cur.next

                prev.next = cur

            else:
                prev, cur = cur, cur.next

        return dummy.next

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
x3 = ListNode(3)
x31 = ListNode(3)
x4 = ListNode(4)
x41 = ListNode(4)
x5 = ListNode(5)


x1.next = x2
x2.next = x3
x3.next = x31
x31.next = x4
x4.next = x41
x41.next = x5

sol = Solution()
sol.printList(x1)

print("####################")
new_head = sol.deleteDuplicates(x1)
sol.printList(new_head)
