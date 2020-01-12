# https://leetcode.com/discuss/interview-question/411357/

"""
Given a 2D grid, each cell is either a zombie 1 or a human 0.
Zombies can turn adjacent (up/down/left/right) human beings into zombies every hour.
Find out how many hours does it take to infect all humans?

Example:

Input:
[[0, 1, 1, 0, 1],
 [0, 1, 0, 1, 0],
 [0, 0, 0, 0, 1],
 [0, 1, 0, 0, 0]]

Output: 2

Explanation:
At the end of the 1st hour, the status of the grid:
[[1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1],
 [0, 1, 0, 1, 1],
 [1, 1, 1, 0, 1]]

At the end of the 2nd hour, the status of the grid:
[[1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1]]
"""
import collections
def orangesRotting(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    # Time: O(R * C) -> In worst case we will be traversing the entire grid
    # Space: O(R* C) -> All grid elements could end up in the queue
    
    answer = 0
    cols = len(grid[0])
    rows = len(grid)

    q = collections.deque()
    human = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                q.append((i, j))

            if grid[i][j] == 0:
                human += 1

    seen = set()
    minutes = 0
    while q:
        for _ in range(len(q)):
            r, c = q.popleft()
            candidates = [(r+1, c), (r, c+1), (r-1, c), (r, c-1)]

            if (r, c) not in seen:
                seen.add((r, c))
                for cand_r, cand_c in candidates:
                    if 0 <= cand_r < rows and 0 <= cand_c < cols and grid[cand_r][cand_c] == 0:
                        grid[cand_r][cand_c] = 1
                        q.append((cand_r, cand_c))
                        human -= 1

        minutes += 1

    if human == 0:
        return max(0, minutes-1)

    return -1

grid = [[0, 1, 1, 0, 1],
 [0, 1, 0, 1, 0],
 [0, 0, 0, 0, 1],
 [0, 1, 0, 0, 0]]

print(orangesRotting(grid))
