# https://leetcode.com/discuss/interview-question/376375
# Solution in the same link as above
# Time -> O(N * H) where N is the number of nodes
# Space -> O(N)


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def insert_into_bst(root, node):
    cur = root
    while cur:
        if cur.val > node.val:
            # make this node the left child
            if cur.left is None:
                cur.left = node
                break
            else:
                cur = cur.left
        else:
            # Make this node the right child of root
            if cur.right is None:
                cur.right = node
                break
            else:
                cur = cur.right


def build_bst(nums, value1, value2):
    root = None
    found_node_1, found_node_2 = False, False
    for num in nums:
        if num == value1:
            found_node_1 = True
        if num == value2:
            found_node_2 = True

        node = TreeNode(num)
        if root is None:
            root = node
            continue

        insert_into_bst(root, node)

    if not found_node_1 or not found_node_2:
        return None

    return root


def bst_distance(nums, value1, value2):
    root = build_bst(nums, value1, value2)

    if root is None:
        return -1

    lca = lowest_common_ancestor(root, value1, value2)
    return get_distance(lca, value1) + get_distance(lca, value2)


def lowest_common_ancestor(root, val1, val2):
    while True:
        if val1 > root.val and val2 > root.val:
            # Both lie in the right sub tree
            root = root.right
        elif val1 < root.val and val2 < root.val:
            root = root.left
        else:
            # 1 value lies in the left subtree and another value lies in right subtree
            return root


def get_distance(source_node, dest_val):
    if source_node.val == dest_val:
        return 0
    node = source_node.left

    if source_node.val < dest_val:
        # Move right
        node = source_node.right

    return 1 + get_distance(node, dest_val)


# print(bst_distance([2, 1, 3], 1, 3))
arr = [20, 10, 5, 15, 30, 25, 35]
print(bst_distance(arr, 10, 30))
