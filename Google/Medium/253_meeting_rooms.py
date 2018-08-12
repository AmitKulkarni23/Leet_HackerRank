# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.
#
# Example 1:
#
# Input: [[0, 30],[5, 10],[15, 20]]
# Output: 2
# Example 2:
#
# Input: [[7,10],[2,4]]
# Output: 1

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        # Credits -> https://leetcode.com/problems/meeting-rooms-ii/discuss/67860/My-Python-Solution-With-Explanation

        # Create and maintain 2 lists of start times and end times
        start = []
        end = []

        for item in intervals:
            start.append(item.start)
            end.append(item.end)

        # Sort the 2 lists
        start.sort()
        end.sort()

        s = e = available = 0
        num_rooms_req = 0

        while s < len(start):
            if start[s] < end[e]:
                if available = 0:
                    # There are no rooms available
                    # We require a new room
                    num_rooms_req += 1
                else:
                    # There are rooms available
                    # Take one of them
                    available -= 1

                s += 1
            else:
                # Meeting ended
                # Room becomes available
                available += 1
                e += 1
        return num_rooms_req
