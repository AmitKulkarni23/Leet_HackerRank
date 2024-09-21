# https://leetcode.com/problems/symmetric-tree/description/
class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        # Approach : Recursive solution
        # For 2 trees to be mirror images of each other, 
        # the node values of the left sub-tree must be equal
        # to the node value of teh right sub-trees
        
        # left subtree of left tree and right subtree of right tree
        # must be mirror images
        
        # right subtree of left tree and left subtree of right tree
        # must be equal
        
        # Calling a helper function is mirror
        return self.is_mirror(root, root)
    
    
    def is_mirror(self, node1, node2):
        """
        Recursively checks if the left subtree is quivalent
        to the right sub-tree
        """
        # if both trees are empty then return True
        if node1 is None and node2 is None:
            return True
        
        # Check for the 
        if node1 and node2:
            if node1.val == node2.val:
                return self.is_mirror(node1.left, node2.right) and self.is_mirror(node1.right, node2.left)
        
        return False