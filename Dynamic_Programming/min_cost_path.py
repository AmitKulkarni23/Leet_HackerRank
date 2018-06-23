# Given a cost matrix cost[][] and a position (m, n) in cost[][], write a function
# that returns cost of minimum cost path to reach (m, n) from (0, 0).
# Each cell of the matrix represents a cost to traverse through that cell.
# Total cost of a path to reach (m, n) is sum of all the costs on that path
# (including both source and destination). You can only traverse down, right
# and diagonally lower cells from a given cell, i.e., from a given cell (i, j),
# cells (i+1, j), (i, j+1) and (i+1, j+1) can be traversed. You may assume that
# all costs are positive integers.

# Credits: https://www.geeksforgeeks.org/dynamic-programming-set-6-min-cost-path/

###########################

import sys
def min_cost_path(cost_arr, m, n):
    """
    Function that returns the min cost to react cost_arr[m][n] from (0, 0)

    Idea: the path to reach (m,n) should through either of (m-1, n), (m,n -1) or (m-1, n-1)
    Therefore take the minimum of these three

    Time Complexity : Exponential
    """
    if m < 0 or n < 0:
        return sys.maxsize
    if m == 0 and n == 0:
        return cost_arr[m][n]

    else:
        return cost[m][n] + min(min_cost_path(cost_arr, m,n-1),
                                min_cost_path(cost_arr, m -1, n),
                                min_cost_path(cost_arr, m-1, n-1))


def min_cost_path_memoized(cost_arr, m, n, R, C):
    """
    Function that returns the min cost to react cost_arr[m][n] from (0, 0)

    Bottom Up approach.
    Memoize
    """

    # Build a temporary array
    # total cost is an array of size (R) x C
    # where R -> is teh number of columns and
    # C -> number of columns
    total_cost = [[0 for _ in range(C)] for _ in range(R)]


    total_cost[0][0] = cost_arr[0][0]


    # Now we will initilize teh first column of the total column matrix
    for i in range(1,m+1):
        total_cost[i][0] = total_cost[i -1][0] + cost[i][0]

    # Similarly cumulatively initialize teh first row
    for j in range(1,n+1):
        total_cost[0][j] = total_cost[0][j-1] + cost[0][j]

    # Lets print the total_cost matrix
    # print(total_cost)

    # Calculate all teh other elements
    for i in range(1, m+1):
        for j in range(1, n+1):
            total_cost[i][j] = cost[i][j] + min(total_cost[i-1][j-1], 
                                    total_cost[i][j-1],
                                    total_cost[i-1][j])


    return total_cost[m][n]


# Examples:
cost= [ [1, 2, 3],
        [4, 8, 2],
        [1, 5, 3] ]
# print(min_cost_path(cost, 2, 2))
print(min_cost_path_memoized(cost, 2, 2, 3, 3))
