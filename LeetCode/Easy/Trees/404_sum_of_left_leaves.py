# Find the sum of all left leaves in a given binary tree.
#
# Example:
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
# There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        ans = 0

        if root.left:
            if root.left.left is None and root.left.right is None:
                # The left leaf node
                ans += root.left.val
            else:
                ans += self.sumOfLeftLeaves(root.left)

        ans += self.sumOfLeftLeaves(root.right)

        return ans
