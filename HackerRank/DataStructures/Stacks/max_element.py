"""
You have an empty sequence, and you will be given N queries. Each query is one of these three types:

1 x  -Push the element x into the stack.
2    -Delete the element present at the top of the stack.
3    -Print the maximum element in the stack.

Output: For each type 3 query, print the maximum element in the stack on a new line.
Example:

10
1 97
2
1 20
2
1 26
1 20
2
3
1 91
3

Answer:
26
91

"""

numb_of_ele = int(input())
stack = [0]
for i in range(numb_of_ele):
    # Getting the input line by line and converting it into
    # into a list of length 2
    inputs = list(map(int, input().split(" ")))


    if inputs[0] == 1:
        # That means this is query 1
        # Therfore the number has to be inserted in the stack
        # We will insert only the maximum number here,
        # as we are only corcenred with the maximum number
        stack.append(max(inputs[1], stack[-1]))
    else:
        # If query type is 2, then we have to delete the top most elment of the
        # stack. Using list's pop method
        if inputs[0] == 2:
            stack.pop()
        else:
            # This is query type 3.
            # Have to print the max element present in the stack
            # This is O(1) access as we are going to only
            # get and print the last element in the array
            print(stack[-1])
