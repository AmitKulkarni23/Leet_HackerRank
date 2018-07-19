# Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its bottom-up level order traversal as:
# [
#   [15,7],
#   [9,20],
#   [3]
# ]


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # Credits -> https://leetcode.com/problems/binary-tree-level-order-traversal-ii/discuss/34978/Python-solutions-(dfs-recursively-dfs+stack-bfs+queue).

        # Crate a list of tuples of the type (node, level)
        # where level is the level the node is at
        stack = [(root, 0)]

        # The final lits that will be returned
        res = []

        # Do this until there are elements in the stack
        while stack:
            node, level = stack.pop()
            if node:
                # Insert a new empty list at position 0 in the res list
                if len(res) < level+1:
                    res.insert(0, [])
                # Now append this nodes value to the last [] in the [[]]
                res[-(level+1)].append(node.val)

                # Append to stack node.right and node.left
                stack.append((node.right, level+1))
                stack.append((node.left, level+1))


        return res
