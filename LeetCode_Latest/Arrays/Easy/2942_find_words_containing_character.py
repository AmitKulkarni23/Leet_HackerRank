# https://leetcode.com/problems/find-words-containing-character/

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        output = []

        for idx, ch in enumerate(words):
            if x in ch:
                output.append(idx)
        
        return output