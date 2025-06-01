# https://leetcode.com/problems/clone-binary-tree-with-random-pointer/description/

# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        if not root:
            return None

        node_map = {}

        # Step 1: Clone structure and populate map
        def clone_structure(node):
            if not node:
                return None
            if node in node_map:
                return node_map[node]
            
            copy = NodeCopy(node.val)
            node_map[node] = copy

            copy.left = clone_structure(node.left)
            copy.right = clone_structure(node.right)
            return copy

        # Step 2: Assign random pointers
        def copy_randoms(node):
            if not node:
                return
            copy = node_map[node]
            if node.random:
                copy.random = node_map[node.random]
            copy_randoms(node.left)
            copy_randoms(node.right)

        clone_structure(root)
        copy_randoms(root)

        return node_map[root]

        # Time - O(n) - each node is visited once in both passes
        # Space - O(n) - hashmap