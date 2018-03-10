"""
In Order traversal of a tree

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        # If root is None, then return an empty list
        if not root:
            return []
    
        # Calling helper function with an empty array first
        inorder_traversal = []
        
        return self.inorder_helper(root, inorder_traversal)
        
    
    def inorder_helper(self,node, inorder_traversal):
        """
        Helper function which actually does teh inorder traversal
        and appends element to the list inorder_traversal apssed as argument
        """
        
        if not node:
            return
        
        # Left raversal
        self.inorder_helper(node.left, inorder_traversal)
        # Append node to list
        inorder_traversal.append(node.val)
        #Right sub_tree traversal
        self.inorder_helper(node.right, inorder_traversal)
        
        
        return inorder_traversal