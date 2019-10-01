# https://leetcode.com/problems/spiral-matrix-ii/


def generateMatrix(n):
    # Credits -> https://leetcode.com/problems/spiral-matrix-ii/discuss/22282/4-9-lines-Python-solutions
    # Time - O(n * n) -> need to visit all cells
    # Space - O(1) -> No storage
    # We make a turn(clockwise) when we are about to go out of bounds /
    # when we have visited a cell previously

    # Initilaize matrix will all zeros
    answer = [[0 for c in range(n)] for r in range(n)]

    # If a row is already filled with a value, make a right turn
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    # Start from 0, 0
    r, c, di = 0, 0, 0

    for val in range(n * n):
        answer[r][c] = val + 1
        new_r, new_c = r + dr[di], c + dc[di]

        if 0 <= new_r < n and 0 <= new_c < n and answer[new_r][new_c] == 0:
            r, c = new_r, new_c
        else:
            di = (di + 1) % 4
            r, c = r + dr[di], c + dc[di]

    return answer

