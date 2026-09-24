class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        # res = 0

        # for i in range(len(s) - k + 1):
        #     seen = set()
        #     for j in range(i, i + k):
        #         if s[j] in seen:
        #             break
        #         seen.add(s[j])
        #     if len(seen) == k:
        #         print(seen)
        #         res += 1

        # return res

        freq = {}
        res = 0
        l, r = 0, k - 1

        if k > len(s):
            return 0

        for i in range(k):
            freq[s[i]] = freq.get(s[i], 0) + 1

        while r < len(s):
            if len(freq) == k:
                res += 1

            r += 1

            if r < len(s):
                freq[s[r]] = freq.get(s[r], 0) + 1

            freq[s[l]] = freq.get(s[l], 0) - 1

            if freq[s[l]] == 0:
                del freq[s[l]]

            l += 1

        return res
