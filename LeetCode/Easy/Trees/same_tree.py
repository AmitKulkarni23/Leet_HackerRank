"""
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false


Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        
        # Approach: Do an inorder traversal of both the trees
        # and check if the lists obtained are === or not
        
#         # My Solutin
#         # Call inorder traversal helper function on p

#         p_inorder = []
#         self.inorder_helper(p, p_inorder)
        
#         # Call inorder traversal helper function on q
#         q_inorder = []
#         self.inorder_helper(q, q_inorder)
        
#         print("P List ", p_inorder)
#         print("Q List", q_inorder)
#         return p_inorder == q_inorder

        # Discussion solution
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return p == q
        
        
#     def inorder_helper(self, node, inorder_list):
#         """
#         Function which performs inorder traversal and returns the
#         list with inorder elements
#         """
        
#         # Base Case
#         if not node:
#             return "X"
        
#         self.inorder_helper(node.left, inorder_list)
#         inorder_list.append(node.val)
#         self.inorder_helper(node.right, inorder_list)
        
#         return inorder_list
        