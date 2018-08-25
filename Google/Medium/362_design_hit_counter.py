# Design a hit counter which counts the number of hits received in the past 5 minutes.
#
# Each function accepts a timestamp parameter (in seconds granularity) and you may assume that calls are being made to the system in chronological order (ie, the timestamp is monotonically increasing). You may assume that the earliest timestamp starts at 1.
#
# It is possible that several hits arrive roughly at the same time.
#
# Example:
#
# HitCounter counter = new HitCounter();
#
# // hit at timestamp 1.
# counter.hit(1);
#
# // hit at timestamp 2.
# counter.hit(2);
#
# // hit at timestamp 3.
# counter.hit(3);
#
# // get hits at timestamp 4, should return 3.
# counter.getHits(4);
#
# // hit at timestamp 300.
# counter.hit(300);
#
# // get hits at timestamp 300, should return 4.
# counter.getHits(300);
#
# // get hits at timestamp 301, should return 3.
# counter.getHits(301);
# Follow up:
# What if the number of hits per second could be very large? Does your design scale?

import collections
class HitCounter(object):
    # Credits -> https://leetcode.com/problems/design-hit-counter/discuss/83477/48ms-Python-Concise-Solution
    # Author -> xueguang
    def __init__(self):
        """
        Initialize your data structure here.
        """
        # Initilaize a dictionary with all element s initialzied to 0
        self.hits = collections.defaultdict(lambda: 0)

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """

        # For each hit increment the hit count in the dictionary
        self.hits[timestamp] += 1

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        # We should return the number of hits in teh past 5 minutes only
        return sum(self.hits[timestamp - i] for i in range(300))


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
