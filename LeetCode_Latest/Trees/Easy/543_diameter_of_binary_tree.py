# https://leetcode.com/problems/diameter-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root):
        # Diameter = depth(left_subtree) + depth(right_subtree)
        
        def helper(node):
            if not node:
                return 0
            left = helper(node.left)
            right = helper(node.right)
            
            # We maintain a global maximum diameter value (self.max_diameter). At every node, we:
            # Compute the current diameter: left_height + right_height.
            # Update self.max_diameter if the current diameter is larger than the previous maximum found.
            self.max_diameter = max(self.ans, left + right)
            
            # we must return the height of the subtree rooted at the current node.
            return max(left, right) + 1
        
        self.max_diameter = 0
        helper(root)
        return self.ans