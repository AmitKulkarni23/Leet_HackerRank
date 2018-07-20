# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its level order traversal as:
# [
#   [3],
#   [9,20],
#   [15,7]
# ]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Run time 48 ms
    def levelOrder_iterative(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if root is None:
            return []

        level = [root]
        ans = []

        while level:
            inter_level = []
            val = []

            for node in level:
                val.append(node.val)

                if node.left:
                    inter_level.append(node.left)

                if node.right:
                    inter_level.append(node.right)


            ans.append(val)

            level = inter_level

        return ans

    #Runtime : 40 ms
    def levelOrder_recursive(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        # Credits -> https://leetcode.com/submissions/detail/164701448/
        res = []
        if root == None:
            return []

        self.dfs(res, root, 0)

        return res

    def dfs(self,res, node, level):
        if node == None:
            return
        if level >= len(res):
            res.append([])
        res[level].append(node.val)
        self.dfs(res, node.left, level + 1)
        self.dfs(res, node.right, level + 1)
