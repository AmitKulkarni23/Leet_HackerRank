"""
Python file to implement the min-heap
"""

class BinHeap:
    """
    parent p
    left child 2p
    right child 2p + 1
    """
    def __init__(self):
        """
        Since a python list is enough to represent a min heap
        the constructor will just initialize the list and initialize a variable
        to keep track of the size of the heap
        """
        self.heap = [0]
        self.heap_size = 0

    def insert(self, item):
        """
        This is teh method used to add an item to the list
        :param item: an integer
        Note: We will initially append a number to the end of the list
        If the heap property is not maintained, then the item is percolated up
        by comparing it with its parent
        :return:
        """

        # Append the item to the end of the list
        self.heap.append(item)

        # Increment the size of the heap
        self.heap_size += 1

        # percolate up if necessary
        self.percolate_up(self.heap_size)

    def percolate_up(self, i):
        """
        This method restores the heap property
        :param i: the initial heap size
        :return:
        """

        while i // 2 > 0:
            if self.heap[i] < self.heap[i // 2]:
                # Swap elements
                temp = self.heap[i // 2]
                self.heap[i // 2] = self.heap[i]
                self.heap[i] = temp

            i = i // 2

    def extract_min(self):
        """
        Function to extract the minimum element from the tree
        Minimum is always at the root node
        Once extracted the heap property should be restored again
        Take the last item in the list an move it to the root position in the
        list. Push the root position downwards to its appropriate position
        :return:
        """

        retval = self.heap[1]
        self.heap[1] = self.heap[self.heap_size]
        self.heap_size -= 1

        # Now that we have moved the last element to teh first position,
        # pop this element from the list
        self.heap.pop()

        # Call perDown method
        self.perc_down(1)

        return retval

    def perc_down(self, i):
        """
        This function is to percolate the root item downwards towards
        it appropriate position, after extract min has been called
        :param i:
        :return:
        """

        while i * 2 <= self.heap_size:
            # Get the minimum child among the 2 children
            min_child = self.get_min_child(i)

            if self.heap[i] > self.heap[min_child]:
                # Swap / Percolate down
                temp = self.heap[i]
                self.heap[i] = self.heap[min_child]
                self.heap[min_child] = temp

            i = min_child

    def get_min_child(self, i):
        """
        Function that returns the minimum among the 2 children
        :param i:
        :return:
        """

        if i * 2 + 1 > self.heap_size:
            return i * 2
        else:
            if self.heap[i * 2] < self.heap[i * 2 + 1]:
                # left child
                return i * 2
            else:
                # Right child index
                return i * 2 + 1

    def build_heap(self, arr):
        """
        Function to build a heap given an arr of integers
        :param arr:
        :return:
        """
        i = len(arr) // 2
        self.heap_size = len(arr)
        self.heap = [0] + arr[:]

        while i > 0:
            self.perc_down(i)
            i = i - 1


bh_obj = BinHeap()
arr = [10, 15, 16, 2, 3]
bh_obj.build_heap(arr)

print(bh_obj.extract_min())
print(bh_obj.extract_min())

# Citation : Inspired by the awesome post at : http://interactivepython.org/runestone/static/pythonds/Trees/BinaryHeapImplementation.html