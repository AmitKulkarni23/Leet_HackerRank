# Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
#
# You may assume no duplicates in the array.
# Input: [1,3,5,6], 5
# Output: 2

# Input: [1,3,5,6], 2
# Output: 1

def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        return self.binary_search(nums, target)

    def binary_search(self, arr, numb):
        """
        Implementation of binary search for the given array
        The given array is sorted. Therfore using binary search to find the element
        """
        first = 0
        last = len(arr) - 1
        found = False
        index = None

        while first<= last and not found:
            # Perform binary search
            mid = (first + last) // 2

            # If the middle item itself is the numb we are looking for
            if arr[mid] == numb:
                found = True
                return mid

            else:
                if arr[mid] > numb:
                    last = mid - 1
                else:
                    first = mid + 1

        return first
