# https://leetcode.com/problems/binary-tree-vertical-order-traversal/

from collections import defaultdict, deque

class Solution:
    # Time Complexity - O(n log n) -> Sorting takes this
    # Space Complexity - O(n) - since all nodes are visited and stored in a map
    def verticalOrder(self, root):
        if not root:
            return []

        # Column to list of nodes
        col_map = defaultdict(list)
        
        # Queue stores tuples of node and its column index
        queue = deque([(root, 0)])

        while queue:
            node, col = queue.popleft()
            
            col_map[col].append(node.val)
            
            if node.left:
                queue.append((node.left, col - 1))
            
            if node.right:
                queue.append((node.right, col + 1))

        # Sort columns and return ordered values
        return [col_map[col] for col in sorted(col_map)]