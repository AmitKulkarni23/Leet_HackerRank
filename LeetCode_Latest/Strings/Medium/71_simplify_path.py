# https://leetcode.com/problems/simplify-path/description/

class Solution:
    def simplifyPath(self, path: str) -> str:
        # Time: O(N) where N is the number of cahacters in path -> we have to traverse through all the characters to solve the problem
        # Space: O(N) for maintaining stack
        stack = []

        portions = path.split("/")

        for portion in portions:
            if portion == "..":
                # this means we have to move one directory up
                # Pop an entry from stack
                if stack:
                    stack.pop()
            elif portion == "." or not portion:
                # There is a no operation needed here
                # It's as if you are in the current directory
                continue
            else:
                # Valida directory name
                stack.append(portion)
        
        return "/" + "/".join(stack)



                



        