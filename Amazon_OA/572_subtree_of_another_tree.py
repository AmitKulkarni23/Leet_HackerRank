# https://leetcode.com/problems/subtree-of-another-tree
# Time Complexity -> O(n ^ 2) -> To find whether a string is in another string
# Space - P(max(m, n)) The depth of recursion tree can go upto n for tree t and m for tree s in worst case

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def isSubtree(s, t):
    """
    :type s: TreeNode
    :type t: TreeNode
    :rtype: bool
    """
    # Credits -> https://leetcode.com/problems/subtree-of-another-tree/discuss/102729/Short-Python-by-converting-into-strings
    return do_pre_order_traversal(t) in do_pre_order_traversal(s)


def do_pre_order_traversal(node):
    """
    Helper function
    """
    if not node:
        return "$"

    return "^" + str(node.val) + "#" + do_pre_order_traversal(node.left) + do_pre_order_traversal(node.right)