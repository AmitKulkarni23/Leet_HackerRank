# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/description/


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # Time - O(n) - traverse through the whole string
        # Space - O(n) for the stack
        
        stack = []  # Each element is (char, count)

        for char in s:
            if stack and stack[-1][0] == char:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([char, 1])

        # Reconstruct the final string
        result = []
        for char, count in stack:
            result.append(char * count)
        return ''.join(result)
            

        