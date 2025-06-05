# https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/description/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # Step 1: Build graph and in-degree
        graph = defaultdict(list)
        in_degree = [0] * n

        for u, v in edges:
            graph[u].append(v)
            in_degree[v] += 1

        # Step 2: Initialize ancestor sets for each node
        ancestors = [set() for _ in range(n)]

        # Step 3: Kahn's Topological Sort
        queue = deque([i for i in range(n) if in_degree[i] == 0])

        while queue:
            u = queue.popleft()
            for v in graph[u]:
                # Add current node and its ancestors to v's ancestors
                ancestors[v].add(u)
                ancestors[v].update(ancestors[u])
                # Decrement in-degree and enqueue if ready
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)

        # Step 4: Convert sets to sorted lists
        return [sorted(list(anc)) for anc in ancestors]

        # Time: O(n + e + n²)
            # O(n + e) for topological traversal
            # Worst case: merging sets → O(n²) if each node has many ancestors

        # Space: O(n²)
        # Worst-case ancestor sets: nearly all nodes are connected to each other