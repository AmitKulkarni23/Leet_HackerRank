# https://leetcode.com/discuss/interview-question/349617

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.children = None


def maximumAverageSubtree(root):
    if root is None:
        return None

    helper(root)
    return max_node


def helper(node):
    global max_val
    global max_node
    # base case
    if node is None:
        return [0, 0]

    cur_total = node.val
    count = 1
    for child in node.children:
        temp_result = helper(child)
        cur_total += temp_result[0]
        count += temp_result[1]

    average = cur_total / count
    if count > 1 and average > max_val:
        max_val = average
        max_node = node

    return [cur_total, count]


max_node = None
max_val = float("-inf")
