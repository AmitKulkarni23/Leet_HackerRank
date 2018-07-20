# Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.
#
# Example:
#
# Input:
#
#    1
#     \
#      3
#     /
#    2
#
# Output:
# 1
#
# Explanation:
# The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).
# Note: There are at least two nodes in this BST.


# Idea -> We will do an in-order traversal and find the min of absolute difference between adjacent nodes
# Why will this work -> becuase the samllest larger number to i is at index i + 1


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        final_list = []
        self.inorder_helper(root, final_list)

        return min([abs(a - b) for a, b in zip(final_list, final_list[1:])])

    def inorder_helper(self, node, final_list):
        """
        A helper function
        """
        if node.left:
            self.inorder_helper(node.left, final_list)

        final_list.append(node.val)

        if node.right:
            self.inorder_helper(node.right, final_list)

        return final_list
