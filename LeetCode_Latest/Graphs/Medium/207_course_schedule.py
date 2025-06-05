from collections import defaultdict, deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Topological Sort - Kahn's algroithm
        # Time: O(N + E) where N = numCourses and E = prerequisites.length
        # Space: O(N + E) for adjacency list and in-degree array

        graph = defaultdict(list)
        in_degree = [0] * numCourses

        # Build graph: bi → ai means bi must be taken before ai
        for ai, bi in prerequisites:
            graph[bi].append(ai)
            in_degree[ai] += 1

        # Start with all courses that have no prerequisites
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        completed = 0

        while queue:
            course = queue.popleft()
            completed += 1
            for neighbor in graph[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return completed == numCourses 
