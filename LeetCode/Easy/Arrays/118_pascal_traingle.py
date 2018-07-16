# Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
#
# In Pascal's triangle, each number is the sum of the two numbers directly above it.
#
# Example:
# Input: 5
# Output:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]


# THIS IS GIVING ME MEMORY LIMIT EXCEEDED
import pprint
def generate(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    # Corner cases
    if numRows == 0:
        return []

    if numRows == 1:
        return [[1]]

    if numRows == 2:
        return [[1], [1, 1]]

    # Create the final list
    # Thsi will be the list that will be returned
    final_list = [[1], [1, 1]]

    # How many intermediate lists should be added to teh final list
    new_len = numRows - 2

    while new_len:

        # j -> represents the number of elemnets to be present
        # in this intermediate list
        # In Pascal's traingle the number of elements are
        # 1, 2, 3, 4, 5, 6 etc..
        j = len(final_list) + 1
        inter_med_list = []

        # The first will always be 1
        inter_med_list.append(1)

        # Now we need to populate the middle elements
        # Take the last list in teh final_list
        # and traverse through the elements

        # Counter to know teh position where we will be inserting the element
        # in the intermediate list


        for x in range(len(final_list[-1]) - 1):
            y = x + 1
            inter_med_list.append(final_list[-1][x] + final_list[-1][y])

        # The last element of the intermedite list is 1
        inter_med_list.append(1)
        final_list.append(inter_med_list)
        # Decrement i
        new_len -= 1
    return final_list

pprint.pprint(generate(6))
