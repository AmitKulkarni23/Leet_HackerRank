# https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root):
        left_height = self.heightOfLeftTree(root)
        right_height = self.heightOfRightTree(root)

        return abs(left_height - right_height) <= 1

    def heightOfLeftTree(self, node):
        if not node:
            return 0
        return self.heightOfLeftTree(node.left) + 1
    
    def heightOfRightTree(self, node):
        if not node:
            return 0
        return self.heightOfRightTree(node.right) + 1