# You have a map that marks the location of a treasure island. Some of the map area has jagged rocks and dangerous
# reefs. Other areas are safe to sail in. There are other explorers trying to find the treasure. So you must figure
# out a shortest route to the treasure island.
#
# Assume the map area is a two dimensional grid, represented by a matrix of characters. You must start from the
# top-left corner of the map and can move one block up, down, left or right at a time. The treasure island is marked
# as X in a block of the matrix. X will not be at the top-left corner. Any block with dangerous rocks or reefs will
# be marked as D. You must not enter dangerous blocks. You cannot leave the map area. Other areas O are safe to sail
# in. The top-left corner is always safe. Output the minimum number of steps to get to the treasure.

# Input:
# [['O', 'O', 'O', 'O'],
#  ['D', 'O', 'D', 'O'],
#  ['O', 'O', 'O', 'O'],
#  ['X', 'D', 'D', 'O']]
#
# Output: 5
# Explanation: Route is (0, 0), (0, 1), (1, 1), (2, 1), (2, 0), (3, 0) The minimum route takes 5 steps.

# Solution Link -> https://leetcode.com/playground/uQoVfEmr

##################################################################################

# Approach -> BFS
# Time -> O(R * C) -> We might have to visit all the cells before getting to the treasure
# Space -> O(R * C) -> Store all visited cells

from collections import deque


def treasure_island(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    if num_rows == 0 or num_cols == 0:
        # Impossible
        return -1

    q = deque([((0, 0), 0)])  # Each element of dequeu is ((x, y), #_of_steps_to_reach_this_point

    # Mark matrix[0][0] as visited.
    matrix[0][0] = 'D'

    # Directions that we can move in
    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # right, down, left, up

    while q:
        (x, y), steps = q.popleft()

        for dx, dy in directions:
            if 0 <= x + dx < num_rows and 0 <= y + dy < num_cols:
                # Is within bounds
                if matrix[x + dx][y + dy] == 'X':
                    # We have reached the treasure
                    return steps + 1
                elif matrix[x + dx][y + dy] == 'O':
                    # Mark this node as visited
                    matrix[x + dx][y + dy] = 'D'
                    # Add it to the queue
                    q.append(((x + dx, y + dy), steps + 1))

    return -1


treasure_map = [['O', 'O', 'O', 'O'],
                ['D', 'O', 'D', 'O'],
                ['O', 'O', 'O', 'O'],
                ['X', 'D', 'D', 'O']]

map_2 = [['O', 'O', 'O', 'X'],
 ['O', 'O', 'O', 'O'],
 ['O', 'O', 'O', 'O'],
 ['O', 'O', 'O', 'O']]

# print(treasure_island(treasure_map))
print(treasure_island(map_2))
