# Given inorder and postorder traversal of a tree, construct the binary tree.
#
# Note:
# You may assume that duplicates do not exist in the tree.
#
# For example, given
#
# inorder = [9,3,15,20,7]
# postorder = [9,15,7,20,3]
# Return the following binary tree:
#
#     3
#    / \
#   9  20
#     /  \
#    15   7


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """

        # Credits -> https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/discuss/34814/A-Python-recursive-solution
        # Similar logic to #105
        # But in post order traversal the root node is present at the last
        if not inorder or not postorder:
            return None

        root = TreeNode(postorder.pop())

        # Note: Instead of calling the index() function we can store the indices in a
        # global dictionary
        j = inorder.index(root.val)

        root.right = self.buildTree(inorder[j+1:], postorder)
        root.left = self.buildTree(inorder[:j], postorder)

        # Credits -> https://leetcode.com/submissions/detail/168931477/
        def buildTree_best_leet_code(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        index = {}
        for i, x in enumerate(inorder):
            index[x] = i

        def helper(in_start, in_end, post_start, post_end):
            if post_end < post_start:
                return None
            root = TreeNode(postorder[post_end])
            index_root_inorder = index[postorder[post_end]]
            left_in_end = index_root_inorder - 1
            len_left = left_in_end - in_start
            root.left = helper(in_start, left_in_end, post_start, post_start + len_left)
            root.right = helper(index_root_inorder + 1, in_end, post_start + len_left + 1, post_end - 1)
            return root

        return helper(0, len(inorder) - 1, 0, len(postorder) - 1)


        return root
