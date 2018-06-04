# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
#
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
# Example:
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> Returns -3.
# minStack.pop();
# minStack.top();      --> Returns 0.
# minStack.getMin();   --> Returns -2.

# Run time -> 89 ms
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        # Implementing the stack using a list
        self.my_stack = []


    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        # We will be pushing tuples into teh list of type ( x, curmin)
        # Each time a push is encountered teh curmin is changed after comparing it with x

        cur_min = self.getMin()

        if cur_min is None or x < cur_min:
            cur_min = x

        self.my_stack.append((x, cur_min))

    def pop(self):
        """
        :rtype: void
        """
        # Return the last inserted element
        # Return type is void
        self.my_stack.pop()

    def top(self):
        """
        :rtype: int
        """
        # Reurn the last inserted element
        length_of_stack = len(self.my_stack)
        if length_of_stack:
            return self.my_stack[length_of_stack - 1][0]

    def getMin(self):
        """
        :rtype: int
        """
        length_of_stack = len(self.my_stack)
        if length_of_stack:
            return self.my_stack[length_of_stack - 1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# Run time -> 73ms
# class MinStack(object):
#
#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.stack = []
#         self.min_stack = []
#
#     def push(self, x):
#         """
#         :type x: int
#         :rtype: void
#         """
#         self.stack.append(x)
#         if not self.min_stack or self.min_stack[-1] >= x:
#             self.min_stack.append(x)
#
#     def pop(self):
#         """
#         :rtype: void
#         """
#         if self.stack:
#             value = self.stack.pop()
#             if self.min_stack[-1] == value:
#                 self.min_stack.pop()
#
#     def top(self):
#         """
#         :rtype: int
#         """
#         return self.stack[-1] if self.stack else None
#
#     def getMin(self):
#         """
#         :rtype: int
#         """
#         return self.min_stack[-1] if self.min_stack else None
#
#
# # Your MinStack object will be instantiated and called as such:
# # obj = MinStack()
# # obj.push(x)
# # obj.pop()
# # param_3 = obj.top()
# # param_4 = obj.getMin()
