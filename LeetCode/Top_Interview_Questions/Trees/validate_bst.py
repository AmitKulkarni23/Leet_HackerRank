"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

"""



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        # Approach : Copy all the elemenst doing an in-order traversal
        # to a list. If list is sorted return true, else return false
        
        # Calling a helper function starting from root
        ele_list = []
        self.copy_in_order_elements(root, ele_list)
        
        return all(ele_list[i] < ele_list[i+1] for i in range(len(ele_list) - 1))
    
    
    def copy_in_order_elements(self, node, ele_list):
        """
        This function performs an in-order traversal and
        appends the elements to the ele_list array
        """
        if not node:
            return
        self.copy_in_order_elements(node.left, ele_list)
        ele_list.append(node.val)
        self.copy_in_order_elements(node.right, ele_list)
        