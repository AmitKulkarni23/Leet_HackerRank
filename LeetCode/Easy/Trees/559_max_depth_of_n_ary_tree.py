# Given a n-ary tree, find its maximum depth.
#
# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
#
# Note:
#
# The depth of the tree is at most 1000.
# The total number of nodes is at most 5000.

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):

    # Runtime : 140 ms
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """

        if root is None:
            return 0

        if root.children is None
            return 1

        return max(self.maxDepth(child) for child in root.children) + 1

    # Run time : 100ms
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """

        if not root:
            return 0
        ans=0
        for x in root.children:
            ans=max(ans,self.maxDepth(x))
        return ans+1
