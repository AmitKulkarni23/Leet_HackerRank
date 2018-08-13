# Given a collection of intervals, merge all overlapping intervals.
#
# Example 1:
#
# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
# Example 2:
#
# Input: [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considerred overlapping.

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """

        # Credits -> https://leetcode.com/problems/merge-intervals/solution/

        # If we sort the intervals by their start value,
        # then each set of intervals that can be merged will appear
        # as a contiguous "run" in the sorted list.

        # Then, we insert the first interval into our merged list and continue
        # considering each interval in turn as follows: If the current interval
        # begins after the previous interval ends, then they do not overlap and
        # we can append the current interval to merged. Otherwise, they do overlap,
        # and we merge them by updating the end of the previous interval if it is
        # less than the end of the current interval.

        # Sort the list by start times
        intervals.sort(key=lambda x:x.start)

        merged = []

        for item in intervals:
            # If merged list is empty or if the current interval
            # under considertaion does not overlap with the last
            # item in the merged list, just append this interval to the merged list
            if len(merged) == 0 or merged[-1].end < item.start:
                merged.append(item)

            else:
                # This means that there is overlap
                merged[-1].end = max(merged[-1].end, item.end)


        return merged
