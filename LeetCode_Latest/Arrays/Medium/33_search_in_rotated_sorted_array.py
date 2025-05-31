# https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) -1

        while l <= r:
            mid = (l+r) // 2

            if nums[mid] == target:
                return mid 
            # Even though the array is rotated, at least one half of the array is always sorted.
            # In each binary search step:
            # Either the left half is sorted, or the right half is sorted.
            # Use that to determine where to search next.
            
            
            if nums[l] <= nums[mid]: # Checks if left is sorted
                # Below condition is needed to check if the target lies in the sorted half
                if nums[l] <= target < nums[mid]:
                    # Search left
                    r = mid - 1
                else:
                    l  = mid  + 1
                    
            else: # Right half is sorted
                # Below condition is needed to check if the target lies in the sorted half
                if nums[mid] < target <= nums[r]:
                    l = mid + 1 # search right
                else:
                    r = mid - 1
        return -1