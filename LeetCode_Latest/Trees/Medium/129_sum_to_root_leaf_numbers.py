# https://leetcode.com/problems/sum-root-to-leaf-numbers/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root):
        # Time: O(n)
        # Stack - O(h)

        def helper(node, current_sum):
            # If we reach a null node, return 0
            # This is the base case for the recursion
            
            if not node:
                return 0
            current_sum = current_sum * 10 + node.val

            # If we reach a leaf node, return the current sum
            if not node.left and not node.right:
                return current_sum
            
            return helper(node.left, current_sum) + helper(node.right, current_sum)
            
        return helper(root, 0)
