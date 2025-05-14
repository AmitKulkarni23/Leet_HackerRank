# https://leetcode.com/problems/closest-binary-search-tree-value/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root, target):
        # Time: O(n)
        # Space: O(1) - no recursion stack
        closest = root.val
        
        while root:
            # Update closest explicitly based on comparison
            if abs(root.val - target) < abs(closest - target):
                closest = root.val
            elif abs(root.val - target) == abs(closest - target):
                closest = min(closest, root.val)

            # Navigate left or right explicitly
            if target < root.val:
                root = root.left
            else:
                root = root.right
        
        return closest
        
            
