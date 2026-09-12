class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        l, r = len(s) - 2, len(s) - 1

        while l >= 0:
            score += abs(ord(s[r]) - ord(s[l]))
            l -= 1
            r -= 1

        return score