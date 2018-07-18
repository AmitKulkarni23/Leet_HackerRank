"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.


Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4

return False

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def __init__(self):
        # Initilailizing a const here
        # so that it is available across all methods
        
        self.MIN_INT = 2 ^ 63 - 1
        
    
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.check_height(root) != self.MIN_INT
        
    
    def check_height(self, node):
        """
        Function that recursively calcualates the height of the
        left sub tree v/s the height of the right subtree       
        """
        
        if not node:
            return -1
        
        left_height = self.check_height(node.left)
        
        if left_height == self.MIN_INT:
            return self.MIN_INT
        
        right_height = self.check_height(node.right)
        
        if right_height == self.MIN_INT:
            return self.MIN_INT
        
        height_dif = left_height - right_height
        if abs(height_dif) > 1:
            # Error case
            return self.MIN_INT
        else:
            return max(left_height, right_height) + 1
        