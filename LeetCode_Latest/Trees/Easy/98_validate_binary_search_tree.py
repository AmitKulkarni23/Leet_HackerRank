# https://leetcode.com/problems/validate-binary-search-tree/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root) -> bool:
        # Time Complexity - O(n) - worts case: need to visit all nodes
        # Space Complexity - O(n) - runtime recursion stack will include 1 call to the recursive function each time we visit a node
        def helper(node, left, right):
            if not node:
                return True
            if not (left < node.val < right):
                return False
            
            return helper(node.left, left, node.val) and helper(node.right, node.val, right)
        

        return helper(root, float("-inf"), float("inf"))
