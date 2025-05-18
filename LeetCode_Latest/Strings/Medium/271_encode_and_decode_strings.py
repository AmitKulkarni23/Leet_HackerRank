# https://leetcode.com/problems/encode-and-decode-strings/description/

class Codec:
    def encode(self, strs) -> str:
        """Encodes a list of strings to a single string.
        """
        # Time:  O(N), N = sum of lengths of all strs
        encoded_parts = []
        for s in strs:
            # 1. Get length of s
            length = len(s)
            # 2. Append "<length>#<s>"
            encoded_parts.append(str(length))
            encoded_parts.append('#')
            encoded_parts.append(s)
        # Join all parts into one contiguous string
        return ''.join(encoded_parts)

    def decode(self, s: str):
        """
        Idea: 

        We scan from left to right:
         1. Read up to the next '#' to get the length L.
         2. Read the following L characters as one of the original strings.
         3. Repeat until we reach the end.
        """
        # Time:  O(N), scanning each character once
        res = []
        i = 0
        n = len(s)
        while i < n:
            # 1) Find the delimiter '#' to parse the length
            j = i
            while s[j] != '#':
                j += 1
            # s[i:j] now holds the decimal length
            length = int(s[i:j])

            # 2) Extract the next `length` chars as one string
            start = j + 1
            end = start + length
            res.append(s[start:end])

            # 3) Move `i` past this segment and repeat
            i = end
        return res
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))