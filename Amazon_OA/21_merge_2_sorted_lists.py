# https://leetcode.com/problems/merge-two-sorted-lists/
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    # Time Complexity - O(N)
    # Space Complexity - O(1)
    prev_node = ListNode(-1)
    prev = prev_node

    while l1 and l2:
        if l1.val <= l2.val:
            prev.next = l1
            l1 = l1.next
        else:
            prev.next = l2
            l2 = l2.next

        prev = prev.next

    prev.next = l1 if l1 else l2
    return prev_node.next
