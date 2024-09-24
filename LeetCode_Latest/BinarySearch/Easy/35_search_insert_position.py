# https://leetcode.com/problems/search-insert-position/

class Solution:
    def searchInsert(self, nums, target):
        low = 0
        high = len(nums) - 1
        
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return mid
            
            if nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        
        return low


# Why is it at low and not high??
# During binary search, low is always trying to catch up to high, while high is trying to move closer to low.
# When the loop terminates, low will always point to where the target should go in the sorted array.
# If the target is smaller than everything, low will be 0.
# If the target is larger than everything, low will be len(nums).
# If the target falls in the middle, low will point to the index where the target should be inserted to keep the array sorted.