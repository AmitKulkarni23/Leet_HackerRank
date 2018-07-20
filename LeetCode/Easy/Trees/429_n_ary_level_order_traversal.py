Given an n-ary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """

        # Iteartive approach
        ans = []

        if root is None:
            return ans

        level = [root]

        while level:
            inter_level = []

            val = []

            for node in level:
                val.append(node.val)

                for child in node.children:
                    inter_level.append(child)

            ans.append(val)
            level = inter_level

        return ans
