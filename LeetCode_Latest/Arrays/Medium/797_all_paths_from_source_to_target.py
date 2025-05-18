# https://leetcode.com/problems/all-paths-from-source-to-target/

class Solution:
    def allPathsSourceTarget(self, graph):
        result = []

        def dfs(node, path):
            if node == len(graph) - 1:
                result.append(list(path))  # Found a path to target
                return

            for neighbor in graph[node]:
                path.append(neighbor)
                dfs(neighbor, path)
                # This is a Directed Acyclic Graph (DAG).

                # Nodes can appear in multiple valid paths, so revisiting them in a new path is correct behavior.
                path.pop()  # Backtrack

        dfs(0, [0])
        return result

        # Let:
        #     n = number of nodes

        #     E = number of edges

        #     P = number of distinct paths from 0 to n - 1

        #     L = average length of those paths

        #     In the worst case:
        #     The graph may have exponentially many valid paths (like a tree-shaped DAG).

        #     For each path, we do:

        #     O(L) work to copy the path into the result

        #     So total work is:

        #     O(P × L)
        #     where:

        #     P is the number of paths from node 0 to n-1

        #     L is the length of each path (up to n)

        #     Worst case:
        #     P = O(2^n) (exponential number of paths if the DAG fans out)

        #     L = O(n) (each path visits every node once)

        #     Worst-case Time Complexity: O(2^n × n)
            


        #     Space Complexity: O(n) for the recursion stack and path storage