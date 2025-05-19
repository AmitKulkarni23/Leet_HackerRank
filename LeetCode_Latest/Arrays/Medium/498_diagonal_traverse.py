# https://leetcode.com/problems/diagonal-traverse/

import collections
from typing import List
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # Time : O(m * n) - All elements in the matrix have to be visited
        # Space: O(m * n) - The dictionary    
        
        # Group elements by row + col
        # All elements that have the same row + col will belong to the same diagonal
        result = []
        diag_dict = collections.defaultdict(list)
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                diag_dict[i + j].append(mat[i][j])
        
        # All the even row + col will be appended to the dictionary in reverse manner
        # defaultdict(<type 'list'>, {0: [1], 1: [2, 4], 2: [3, 5, 7], 3: [6, 8], 4: [9]})
        # Reverse if k % 2 == 0
        print(diag_dict)
        for k in diag_dict:
            if k % 2 == 0:
                result += diag_dict[k][::-1]
            else:
                result += diag_dict[k]
        
        return result