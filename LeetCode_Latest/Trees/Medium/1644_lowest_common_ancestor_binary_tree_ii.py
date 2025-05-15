# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-ii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        parent_child_dict = {}
        found_p = [False]
        found_q = [False]

        def helper(parent_node, current_node):
            if not current_node:
                return

            if current_node == p:
                found_p[0] = True
            if current_node == q:
                found_q[0] = True

            parent_child_dict[current_node] = parent_node

            helper(current_node, current_node.left)
            helper(current_node, current_node.right)

        helper(None, root)
        
        if not found_p[0] or not found_q[0]:
            return None

        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent_child_dict[p]
        
        while q:
            if q in ancestors:
                return q
            q = parent_child_dict[q]
        
        return None