# Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.
#
# Example:
#
# MovingAverage m = new MovingAverage(3);
# m.next(1) = 1
# m.next(10) = (1 + 10) / 2
# m.next(3) = (1 + 10 + 3) / 3
# m.next(5) = (10 + 3 + 5) / 3


class MovingAverage(object):
    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """

        # Credits -> https://leetcode.com/problems/moving-average-from-data-stream/discuss/81489/Simple-Python-solution-based-on-Circular-Array-real-O(1)-time-next()
        # We will maintain a list
        self.my_list = [0] * size
        self.size = size
        self.idx = 0
        self.my_sum = 0

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        # Each time next is called, increment the index
        self.idx += 1

        # We want a moving window
        self.my_sum -= self.my_list[self.idx % self.size]

        self.my_list[self.idx % self.size] = val

        self.my_sum += val

        # return the average
        return self.my_sum / float(min(self.idx, self. size))

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
