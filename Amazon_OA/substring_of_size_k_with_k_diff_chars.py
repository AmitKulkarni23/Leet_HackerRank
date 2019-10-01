# https://leetcode.com/discuss/interview-question/370112
# This is a sliding window problem
# O(n)

def findSubstring(m, k):
    # get the lenght of the linked list
    L = len(m)
    orginalChar = set(list(m))
    substring = []
    for i in range(0, L - k + 1):
        a = set(list(m[i:i + k]))
        oAfter = len(orginalChar - a)
        if ((len(orginalChar) - oAfter) == k):
            if (m[i:i + k] not in substring):
                substring.append(m[i:i + k])
    return substring

print(findSubstring("abcabc", 3))
print(findSubstring("abacab", 3))
print(findSubstring("awaglknagawunagwkwagl", 4))
