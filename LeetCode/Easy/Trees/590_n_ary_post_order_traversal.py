Given an n-ary tree, return the postorder traversal of its nodes' values.

Note: Recursive solution is trivial, could you do it iteratively?


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """

        if root is None:
            return []

        ans = []
        stack = [root]

        while stack:
            top_node = stack.pop()

            ans.append(top_node.val)

            # Extend the stack
            # stack = stack + [child for child in top_node.children]
            stack.extend(node.children)


        return ans[::-1]
