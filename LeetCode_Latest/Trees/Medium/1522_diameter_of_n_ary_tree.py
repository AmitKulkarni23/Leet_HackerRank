# https://leetcode.com/problems/diameter-of-n-ary-tree/description/

"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """

        # Time COmplexity - O(n)
        # Space - O(h)

        self.max_diameter = 0

        def dfs(node):
            if not node:
                return 0

            # Store top two heights from children
            # max1 represents the highest
            # max2 represents the second highest
            max1, max2 = 0, 0

            for child in node.children:
                h = dfs(child)
                if h > max1:
                    max1, max2 = h, max1
                elif h > max2:
                    max2 = h

            # update diameter with the two tallest paths
            self.max_diameter = max(self.max_diameter, max1 + max2)

            # return the height of current node
            return max1 + 1

        dfs(root)
        return self.max_diameter