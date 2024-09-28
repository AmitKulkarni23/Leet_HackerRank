# https://leetcode.com/problems/intersection-of-two-arrays/description/

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Time Complexity: O(m + n)
        # Finding the intersection of two sets (using set1 & set2) involves iterating through the smaller set and checking if each element exists in the other set.
        # Since checking membership in a set is 𝑂(1)on average, iterating through the smaller set will take 
        # O(min(m,n)), but in worst-case analysis, we consider the maximum of both sets, so this operation takes O(m+n).
        # Space Complexity - O(m + n)
        # where m and n are lenghts of nums1 and nums2
        set1 = set(nums1)
        set2 = set(nums2)

        return list(set1 & set2)