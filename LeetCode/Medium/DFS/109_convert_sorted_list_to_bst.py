# Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
#
# For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
#
# Example:
#
# Given the sorted linked list: [-10,-3,0,5,9],
#
# One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:
#
#       0
#      / \
#    -3   9
#    /   /
#  -10  5


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """

        # Algorithm 1:(O(n logn)))
        # 1) Get middle of linked list and make it root
            # - Do this recursively for the left half and right half
          # 2) Get middle of left half and make left child of root
          # 3) Get middle of right half and make right child of root
        # Why n logn -> We will traverse the whole linked list in parts
        # and there are logn levels in a balanced BST
        # Credits -> https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/discuss/35476/Share-my-JAVA-solution-1ms-very-short-and-concise.

        if not head:
            return None

        return self.helper(head, None)


    def helper(self, start, end):
        """
        A helper function
        """
        if not start:
            return None

        if start == end:
            return None

        slow = fast = start
        while fast != end and fast.next != end:
            slow = slow.next
            fast = fast.next.next

        node = TreeNode(slow.val)
        node.left = self.helper(start, slow)
        node.right = self.helper(slow.next, end)

        return node

        # Credits -> https://leetcode.com/submissions/detail/168935097/
        # Runtime : 108 ms
        def sortedListToBST_best_leet_code_sol(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        def buildBST(l, r):
            if l > r:
                return None
            m = (l + r) / 2
            root = TreeNode(nums[m])
            root.left = buildBST(l, m - 1)
            root.right = buildBST(m + 1, r)
            return root
        return buildBST(0, len(nums) - 1)
