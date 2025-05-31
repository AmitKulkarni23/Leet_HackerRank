# https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/


class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        # We need the resultant array to be sorted
        # We will use two pointer solution
        # If we used hashmap then we would need to sort the final result which would lead to O(N log N) complexity where N is the number of elements in hashmap
        n1, n2 = len(nums1), len(nums2)
        ptr1, ptr2 = 0, 0

        result = []
        while ptr1 < n1 and ptr2 < n2:
            if nums1[ptr1][0] == nums2[ptr2][0]:
                result.append([nums1[ptr1][0], nums1[ptr1][1] + nums2[ptr2][1]])
                ptr1 += 1
                ptr2 += 1
            
            elif nums1[ptr1][0] < nums2[ptr2][0]:
                result.append(nums1[ptr1])
                ptr1 += 1
            else:
                result.append(nums2[ptr2])
                ptr2 += 1
        
        while ptr1 < n1:
            result.append(nums1[ptr1])
            ptr1 += 1

        while ptr2 < n2:
            result.append(nums2[ptr2])
            ptr2 += 1

        return result
    

# Time Complexity - O(N + M) where N and M are the number of elements in nums1 and nums2 respectively