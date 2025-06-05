# https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/description/

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        # Time - O(n) - need to visit all nodes in tree
        # Space - O(1)

        # Insight
        # We only need to traverse a subtree if:

        # There is at least one apple in that subtree.

        # For each such subtree, we pay a cost of 2 seconds:
            # 1 second to go down into the subtree
            # 1 second to come back up



        tree = defaultdict(list)

        # Build the adjacency list from the given edge list
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)

        def dfs(node, parent):
            total_time = 0

            # Visit all children (neighbors) of the current node
            for child in tree[node]:
                if child == parent:
                    continue  # Avoid traversing back to parent (prevents cycle)

                # Recursively compute time for this subtree
                child_time = dfs(child, node)

                # If there's any apple in the child’s subtree OR at the child itself,
                # we need to go to that child and return => add 2 to the time
                if child_time > 0 or hasApple[child]:
                    total_time += child_time + 2

            return total_time  # Return the total time spent in this subtree

        return dfs(0, -1)  # Start DFS from root (node 0), with no parent (-1)