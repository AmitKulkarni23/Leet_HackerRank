def find_k_largest(nums, k):

    def select(first, last, k_smallest):
        if first == last:
            return nums[first]

        pivot_index = partition(first, last)
        if k_smallest == pivot_index:
            return nums[k_smallest]
        elif k_smallest < pivot_index:
            return select(first, pivot_index - 1, k_smallest)
        else:
            return select(pivot_index + 1, last, k_smallest)

    def partition(first, last):
        # Select the first element in the array as the pivot
        pivot = nums[first]
        left_mark = first + 1
        right_mark = last
        finished = False

        while not finished:
            while left_mark <= right_mark and nums[left_mark] <= pivot:
                left_mark += 1

            while left_mark <= right_mark and nums[right_mark] >= pivot:
                right_mark -= 1

            if right_mark < left_mark:
                finished = True
            else:
                nums[left_mark], nums[right_mark] = nums[right_mark], nums[left_mark]

        # Put the pivot into it's correct position
        nums[first], nums[right_mark] = nums[right_mark], nums[first]
        return right_mark

    # kth largest = N - k smallest
    return select(0, len(nums) - 1, len(nums) - k)

arr = [3, 2, 1, 5, 6, 4]
print(find_k_largest(arr, 3))
