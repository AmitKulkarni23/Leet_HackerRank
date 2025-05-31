# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # Time - O(log n)
        # Space - O(1)
        
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return True

            # Skip duplicates on both ends
            # Why skip? - You can’t determine which side is sorted.
            # But you also know that:
            # You’re not going to learn anything new from keeping these same values in your window.
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1

            # Left half is sorted
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            # Right half is sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return False