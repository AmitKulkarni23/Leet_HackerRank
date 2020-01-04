"""
Write a program that takes as input a permutation and returns the next
permutation under dictionary ordering. If the permutation is the last
permutation then return an empty array.

Input: [1, 0, 3, 2]
Output: [1, 2, 0, 3]

Input : [3, 2, 1, 0]
Output: []
"""

"""

Brute Force Approach: Calculate all permutations and sort them and return the
successor of the input permutation.

Idea: We want to increase the permutation by as little as possible
Eg: [6, 2, 1, 5, 4, 3, 0]

Step 1: Start from the right and look at the longest decreasing suffix [5, 4, 3, 0]
We cannot get the next permutation by modifying this suffix since it is already
the maximum it can be.

Step 2: Look at the entry e that appears just before the longest decreasing
suffix which e = 1 in the baove case. If there is no such e, then the suffix is
of the type [n-1, n-2, ..., 3, 2, 1, 0](for which ther eis no next permutation)

Step 3: Note that the entry after e is greater than e. There must be some integer
in the suffix that is larger than e. We want to increase the given permutation by
as little as possible. Therefore, swap e with the smallest integer/element in the
suffix that is larger than e

In example: [6, 2, 1, 5, 4, 3, 0]
suffix  = [5, 4, 3, 0]
e = 1
s = 3

Swap e <-> s.
[6, 2, 3, 5, 4, 1, 0]

Step 4: Now, we have ensured that the prefix is the smalles possible for all
permutations greater than the initial permutation.

But the suffix may not be the smallest.
We need to sort the suffix now.

sort(suffix) is not required. Why not?
Since, suffix was initally decreasing, e <-> s will still keep the suffix
decreasing. Therefore just do reverse(suffix)


Algorithm:
1. Find k such that p[k] < p[k + 1] and entries after index k appear in
decreasing order
2. Find the smallest p[l] such that p[l] > p[k](such an l must exist since p[k] < p[k + 1])
3. Swap p[l] <-> p[k]
4. Reverse the sequence after position k
"""

def nextPermutation(self, nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    # Time: O(n)
    # Spce: O(1)

    inversion_point = len(nums) - 2
    while inversion_point >= 0 and nums[inversion_point] >= nums[inversion_point + 1]:
        inversion_point -= 1

    if inversion_point == -1:
        # The whole array is in reversed sorted order
        return nums.reverse()

    # Swap the smallest element after inversion_point that is greater than nums[inversion_point]
    # Since entries after inversion_point are in reverse/decreasing order, if we search in reverse order
    # the first element greater than nums[inversion_point] is the one need to swap with

    for i in reversed(range(inversion_point + 1, len(nums))):
        if nums[i] > nums[inversion_point]:
            # Swap and break
            nums[i], nums[inversion_point] = nums[inversion_point], nums[i]
            break

    # We just need to reverse everything in the suffix(everything after the inversion point)
    nums[inversion_point + 1:] = reversed(nums[inversion_point + 1:])
