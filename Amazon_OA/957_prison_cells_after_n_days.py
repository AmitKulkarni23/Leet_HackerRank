# https://leetcode.com/problems/prison-cells-after-n-days
# Solution Credits -> https://leetcode.com/problems/prison-cells-after-n-days/discuss/205684/JavaPython-Find-the-Loop-or-Mod-14

# Brute Force
def prisonAfterNDays(cells, N):
    while N > 0:
        N -= 1
        cells_2 = [0] * 8
        for i in range(1, 7):
            cells_2[i] = 1 if cells[i-1] == cells[i+1] else 0

        cells = cells_2

    return cells

# Note: There are only 6 bits / prison cells that are changing
# The first and last prison cells change to 0 and remain at 0
# Therefore we have 6 prison cells that are changing.

# The first time you see a state you store it in the map.
# This state may occur again
# The next time we see the same state we have passed a total of (lastSeen - curVal) states.

# Therefore, the states repeat after every (lastSeen - curVal) iterations.

# We do a curr_N % (lastSeen - curVal) so that we do not repeat the same steps again

# For example:
# N = 100
# We know that state changes after every 14 days
# 100 % 14 = 6.

# There is no need to calculate all states, except from the last 6th state
# 6 % 14, 5 % 14, 4 % 14, 3 %14... are 6, 5, 4 so we need to calculate prison states only for a few days.
# This is a good optimization trick.


def prisonAfterNDays(cells, N):
    N = (N - 1) % 14 + 1

    for N in range(N, 0, -1):
        cells_2 = [0] * 8

        for i in range(1, 7):
            cells_2[i] = 1 if cells[i - 1] == cells[i + 1] else 0

        cells = cells_2

    return cells


