"""
Python file which implements the quick sort algorithm
Basic Algorithm:

quickSort(arr[], low, high)
{
    if (low < high)
    {
        /* pi is partitioning index, arr[pi] is now
           at right place */
        pi = partition(arr, low, high);

        quickSort(arr, low, pi - 1);  // Before pi
        quickSort(arr, pi + 1, high); // After pi
    }
}

ANALAYIS OF QUICK SORT -> https://www.khanacademy.org/computing/computer-science/algorithms/quick-sort/a/analysis-of-quicksort

Worst Case -> In particular, suppose that the pivot chosen
is always either the smallest or the largest element in the nnn-element subarray.
Then one of the partitions will contain no elements and the other partition
will contain n-1 elements, all but the pivot.

For unbalanced partitions:
cn -> c(n - 1) -> c(n - 2)....
cn + c(n - 1) + c(n - 2) + .... = c((n + 1)(n / 2) - 1)
O(n ^ 2)

Best Case: When the partitions are evenly balanced.
cn + 2 * cn / 2 + 4 * cn / 4 + ...
O(n log n)

"""


import random

def quick_sort(arr):
  def select(left, right):
    if left < right:

      pivot_index = random.randint(left, right)
      pivot_index = partition(left, right, pivot_index)

      select(left, pivot_index - 1)
      select(pivot_index + 1, right)


  def partition(left, right, idx):
    pivot_element = arr[idx]

    # Move the pivot element to the very end of the array
    arr[right], arr[idx] = arr[idx], arr[right]
    store_idx = left

    for i in range(left, right):
      if arr[i] < pivot_element:
        arr[store_idx], arr[i] = arr[i], arr[store_idx]
        store_idx += 1

    # Move the pivot element back to it's correct position
    arr[right], arr[store_idx] = arr[store_idx], arr[right]

    return store_idx

  select(0, len(arr) - 1)


nums = [10, 7, -12, 6, 24, 14, 32, -98, 1098]
quick_sort(nums)
print(nums)
