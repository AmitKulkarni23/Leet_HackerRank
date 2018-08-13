# Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.
#
# Note: The length of path between two nodes is represented by the number of edges between them.
#
# Example 1:
#
# Input:
#
#               5
#              / \
#             4   5
#            / \   \
#           1   1   5
# Output:
#
# 2
# Example 2:
#
# Input:
#
#               1
#              / \
#             4   5
#            / \   \
#           4   4   5
# Output:
#
# 2
# Note: The given binary tree has not more than 10000 nodes. The height of the tree is not more than 1000.
#

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Credits -> https://leetcode.com/problems/longest-univalue-path/solution/
        self.ans = 0
        self.arrow_len(root)

        return self.ans

    def arrow_len(self, node):
        """
        Helper function
        """
        # base case
        if not node:
            return 0

        left_len = self.arrow_len(node.left)
        right_len = self.arrow_len(node.right)

        left_arrow = right_arrow = 0
        if node.left and node.left.val == node.val:
            left_arrow = left_len + 1

        if node.right and node.right.val == node.val:
            right_arrow = right_len + 1

        self.ans = max(self.ans, left_arrow + right_arrow)

        return max(left_arrow, right_arrow)
