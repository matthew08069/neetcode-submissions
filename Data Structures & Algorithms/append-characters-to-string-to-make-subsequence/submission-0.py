class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        # Two pointers, i and j, each start at the begining of s and t
        # If s[i] == t[j], i += 1, j += 1
        # If s[i] != t[j], i += 1 until s[i] == t[j] or i is at the end of s
        # The len(t) - j is how many chars needed to append to s
        # If j == len(t), return 0, meaning t is already a subsequence of s

        i, j = 0, 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                i += 1

        return len(t) - j
