# Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.
#
# Note that the row index starts from 0.
#
#
# In Pascal's triangle, each number is the sum of the two numbers directly above it.
#
# Example:
#
# Input: 3
# Output: [1,3,3,1]


def getRow(self, rowIndex):
    """
    :type rowIndex: int
    :rtype: List[int]
    """

    # Credits -> https://leetcode.com/problems/pascals-triangle-ii/discuss/38473/Java-O(k)-solution-with-explanation
    k = []

    for row in range(rowIndex+1):
        k.append(1)
        for i in reversed(range(1, len(k)-1)):
            k[i] = k[i-1]+k[i]
    return k
