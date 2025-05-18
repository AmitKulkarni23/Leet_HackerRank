# https://leetcode.com/problems/course-schedule-ii/

from collections import defaultdict
from collections import deque
from typing import List
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Topological Sort - Kahn's alrgorithm
        # Time: O (V + E)
        # Step 1: Build graph and in-degree
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        
        for dest, src in prerequisites:
            graph[src].append(dest)
            in_degree[dest] += 1
        
        # Step 2: Start with nodes having in-degree 0
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        order = []
        
        while queue:
            course = queue.popleft()
            order.append(course)
            
            for neighbor in graph[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # Step 3: Check if all courses are in the result
        if len(order) == numCourses:
            return order
        else:
            return []  # cycle detected