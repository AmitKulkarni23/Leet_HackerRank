"""
Quick Sort:
Quick Sort partitions the collection around the pivot element
smaller_than_pivot....pivot...larger_than_pivot

Even though the array/list isn't completely sorted yet, we know that elements are sorted in correct order
in relation with the pivot i.e. we don't have to compare left array elements with right array elements

Average Case: O(n log n)
Worst Case Scenario: o(n ^ 2).

When does this happen? -> When quick sort picks the worst possible pivot. (Triggers more depths of recursion)

If first element is chosen as pivot, then already sorted array is the worst case
If last element is chosen as pivot and array is reverse sorted then that is the worst case
i.e. if pivot is the smallest or the largest element in the list then quick sort is bad


Better selection of pivot -> Scan through the entire array and find the median
OR
Choose a randomized pivot

"""