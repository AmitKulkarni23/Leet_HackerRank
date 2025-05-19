# https://leetcode.com/problems/shortest-path-in-binary-matrix/description/

from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid):
        # Time Complexity: O(n²), since each cell is visited at most once.
        # Space Complexity: O(n²), for the visited set and queue.

        # Why BFS over DFS?
        # BFS is used here because we are looking for the shortest path in an unweighted grid.
        # In BFS, we explore all neighbors at the present depth prior to moving on to nodes at the next depth level.
        # Think of a maze
          # DFS is like one person going all the way down one tunnel until they hit a dead end, then turning back.
          # BFS is like sending out waves of people in all directions at once, one step at a time.
          # So the first person to reach the end using BFS took the shortest possible number of steps.

        n = len(grid)
        if grid[0][0] != 0 or grid[n-1][n-1] != 0:
            return -1

        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),          (0, 1),
                      (1, -1),  (1, 0),  (1, 1)]

        queue = deque([(0, 0, 1)])  # (row, col, path_length)
        visited = set((0, 0))

        while queue:
            row, col, path_len = queue.popleft()
            if (row, col) == (n - 1, n - 1):
                return path_len

            for dr, dc in directions:
                r, c = row + dr, col + dc
                if 0 <= r < n and 0 <= c < n and grid[r][c] == 0 and (r, c) not in visited:
                    visited.add((r, c))
                    queue.append((r, c, path_len + 1))

        return -1
                