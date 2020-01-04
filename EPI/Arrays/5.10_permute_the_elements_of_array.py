"""
Given an array of A of n elements and a permutation P, apply P to A
Example: P  [2, 0, 1, 3]
A = ['a', 'b', 'c', 'd']

Output : ['b', 'c', 'a', 'd']

i.e. from A, a goes to position 2 in the result, b goes to position 0,
c goes to position 1 and d goes to position 3
"""

"""
Brute Force: Simple to apply P to A, if additional space is allowed
B[P[i]] = A[i] -> O(n) / O(n)
What if you can't create extra space?

Interviewer: What if you could only modify P?
P = [2, 0, 1, 3], A = ['a', 'b', 'c', 'd']
Step 1: Swap -> A[2] <-> A[0] and swap P[2] <-> P[0]
        P = [1, 0, 2, 3], A = ['c', 'b', 'a', 'd']
Step 2: Swap -> A[1] <-> A[0] and swap P[0] <-> P[1]
        P = [0, 1, 2, 3], A = ['b', 'c', 'a', 'd']

Since P is is in order, we are done
"""

def apply_permutation(P, A):
    for i in range(len(A)):
        while P[i] != i:
            next_idx = P[i]
            A[i], A[next_idx] = A[next_idx], A[i]
            P[i], P[next_idx] = P[next_idx], P[i]


P = [2, 0, 1, 3]
A = ['a', 'b', 'c', 'd']
apply_permutation(P, A)
print(P)
print(A)
