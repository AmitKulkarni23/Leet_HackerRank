# https://leetcode.com/problems/fixed-point/description/

class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        low = 0
        high = len(arr) - 1
        result = -1

        while low <= high:
            mid = low + (high - low) // 2

            if arr[mid] == mid:
                result = mid
                # Problem specifically asks for smallest index; So continue searching left
                high = mid -1
            elif arr[mid] > mid:
                high = mid - 1
            else:
                low = mid + 1
        
        return result
        