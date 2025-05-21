# https://leetcode.com/problems/shortest-bridge/description/

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        # Idea: Find the first island using DFS
        # Then BFS out that island to find the shortest path(number of steps) to the second island
        # Time complexity - O(n ^ 2) - because of the for loops
        # SPace Complexity - O (n ^ 2) - because of DFS - worst case scearnio we might touch all nodes

        n = len(grid)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = [[0] * n for _ in range(n)]
        queue = deque()

        # DFS to get the first island
        def dfs(r, c):
            if r < 0 or r >= n or c < 0 or c >= n or visited[r][c] or grid[r][c] != 1:
                return
            visited[r][c] = 1
            queue.append((r, c))

            for dr, dc in directions:
                dfs(r + dr, c + dc)
        
        found_first_island = False
        for i in range(n):
            if found_first_island:
                break
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    found_first_island = True
                    break

        # BFS to get the shortest path 
        steps = 0
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                        if grid[nr][nc] == 1:
                            # we have recahed the second island; Return the number of steps
                            return steps
                        visited[nr][nc] = 1
                        queue.append((nr, nc))
            
            steps += 1
        return -1

        
