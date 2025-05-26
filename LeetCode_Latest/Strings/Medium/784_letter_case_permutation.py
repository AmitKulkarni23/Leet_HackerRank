# https://leetcode.com/problems/letter-case-permutation/description/

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        # If it's a digit, append it to all existing strings in the queue. If it's a letter, for each string in the queue: 
        # Append both the lowercase and uppercase versions (branch in two).


        # Time - O(2 ^ L)
        # Space - O(2 ^ L)
        # Why?
        # Every letter in the string introduces a binary choice:
        # You can either make it lowercase or uppercase. So for each letter, you branch in 2 directions.
        
        result = ['']

        for ch in s:
            if ch.isalpha():
                # For each current partial string, branch to lower and upper case
                result = [prefix + c for prefix in result for c in (ch.lower(), ch.upper())]
            else:
                # Just append the digit to each partial string
                result = [prefix + ch for prefix in result]

        return result