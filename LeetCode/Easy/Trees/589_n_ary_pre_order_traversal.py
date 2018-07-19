# Given an n-ary tree, return the preorder traversal of its nodes' values.
#
#
# For example, given a 3-ary tree:

# Return its preorder traversal as: [1,3,5,6,2,4].
#
#
# Note: Recursive solution is trivial, could you do it iteratively?

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorder_recursive(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        final_list = []
        self.preorder_helper(root, final_list)

        return final_list

    def preorder_helper(self, root, final_list):
        """
        A helper function
        """
        if root is not None:
            final_list.append(root.val)
            for child in root.children:
                self.preorder_helper(child, final_list)


    def preorder_iterative(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """

        # We will use a double ended queue
        # Credits -> https://leetcode.com/submissions/detail/164702709/
        
        ret, q = [], collections.deque([root])
        while any(q):
            node = q.popleft()
            ret.append(node.val)
            for child in node.children[::-1]:
                if child: q.appendleft(child)
        return ret
