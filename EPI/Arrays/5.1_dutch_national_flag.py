"""
Write a program that takes an array A and index i into A, and rearranges the
elements less than A[i] "pivot" appear first, followed by elements equal to the
pivot, followed by elements greater than the pivot.
"""

# Time: O(n)
# Space: O(1)

# Idea: Make/maintain 4 different subarrays
# bottom - elemnts less than pivot
# top - elements greater than pivot
# equal - elements qual to pivot
# unclassified - all elements initailly are "unclassified"
def dutch_national_flag(arr, i):
    pivot_element = arr[i]

    smaller, equal, larger = 0, 0, len(arr) - 1

    while equal < larger:
        if arr[equal] < pivot_element:
            arr[smaller], arr[equal] = arr[equal], arr[smaller]
            smaller += 1
            equal += 1
        elif arr[equal] == pivot_element:
            equal += 1
        else:
            arr[larger], arr[equal] = arr[equal], arr[larger]
            larger -= 1


import random
nums = [7, 18, 19, 6, 5, 10, 3, -18, 14, 6]
i = random.randint(0, len(nums))
print("Index = ", i)
print("nums[i] = ", nums[i])

dutch_national_flag(nums, i)
print(nums)
