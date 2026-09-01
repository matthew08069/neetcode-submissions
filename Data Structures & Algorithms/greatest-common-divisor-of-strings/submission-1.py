class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        s1 = len(str1)
        s2 = len(str2)
        remin = 1

        if str1 + str2 != str2 + str1:
            return ""
        while remin != 0:
            remin = max(s1, s2) % min(s1, s2)
            s1 = min(s1, s2)
            s2 = remin

        return str2[0:s1]

