class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        res = 0

        for i in range(len(s) - k + 1):
            seen = set()
            for j in range(i, i + k):
                if s[j] in seen:
                    break
                seen.add(s[j])
            if len(seen) == k:
                print(seen)
                res += 1

        return res
