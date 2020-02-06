# Find the length of the longest non-decreasing subsequence
# Eg: [-1, 3, 4, 5, 2, 2, 2, 2]
# Answer : 5 [-1, 2, 2, 2, 2]

# Time: O(n^2)
# Space: O(n)

def longest_non_decreasing_subsequence(arr):
    if not arr:
        return 0

    cache = [1 for _ in range(len(arr))]
    max_so_far = 1

    # Plant j
    for j in range(1, len(arr)):
        # Move i up until j
        for i in range(j):
            # Check for NDS property
            if arr[j] >= arr[i]:
                cache[j] = max(cache[i], cache[j] + 1)

        max_so_far = max(max_so_far, cache[j])
        
    return max_so_far

arr = [-1, 3, 4, 5, 2, 2, 2, 2]
print(longest_non_decreasing_subsequence(arr))
