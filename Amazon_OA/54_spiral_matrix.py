# https://leetcode.com/problems/spiral-matrix/


def spiralOrder(matrix):
    # Credits -> https://leetcode.com/problems/spiral-matrix/solution/
    # Idea -> We have to visit all the cells
    # i.e. we have to visit R*C cells
    # We make a turn(clockwise) when we are about to go out of bounds /
    # when we have visited a cell previously

    # Time Complexity: O(R * C)
    # Space -> O(1)

    if not matrix:
        return []

    R = len(matrix)
    C = len(matrix[0])

    visited = [[False] * C for _ in range(R)]

    answer = []

    # Clockwise directions for new row and new columns
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    # Current row and current column and direction
    r, c, di = 0, 0, 0

    for _ in range(R * C):
        visited[r][c] = True
        answer.append(matrix[r][c])
        new_r, new_c = r + dr[di], c + dc[di]

        if 0 <= new_r < R and 0 <= new_c < C and not visited[new_r][new_c]:
            r, c = new_r, new_c
        else:
            di = (di + 1) % 4
            r, c = r + dr[di], c + dc[di]