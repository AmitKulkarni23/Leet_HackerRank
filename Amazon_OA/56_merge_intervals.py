# https://leetcode.com/problems/merge-intervals/
def merge(intervals):
    # Time Complexity -> O(n log n)
    # Space Complexity -> O (1)

    # Sort the given intervals list by their start time
    intervals.sort(key=lambda item: item[0])

    result = []

    for interval in intervals:
        if len(result) == 0 or result[-1][1] < interval[0]:
            result.append(interval)
        else:
            # Do merging
            result[-1][1] = max(result[-1][1], interval[1])

    return result
