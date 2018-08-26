# Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
#
# Example:
#
# Input: [1,2,3,null,5,null,4]
# Output: [1, 3, 4]
# Explanation:
#
#    1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # Credits -> https://leetcode.com/problems/binary-tree-right-side-view/solution/
        # Time Complexity -> O(n)
        # Space Complexity -> O(n)

        # n -> height of the tree

        right_most_val = dict()

        max_depth = -1

        stack = [(root, 0)]

        while stack:

            node, depth = stack.pop()

            if node is not None:
                max_depth = max(depth, max_depth)

                # Set default -> Sets the value to default value
                # if this key is not already present

                # Note: The dict is of the form {depth : node.val}
                right_most_val.setdefault(depth, node.val)

                # Append the left node first( because we want to pop the right node)
                # as we want the right side view
                stack.append((node.left, depth + 1))
                stack.append((node.right, depth + 1))

        return [right_most_val[d] for d in range(max_depth + 1)]
