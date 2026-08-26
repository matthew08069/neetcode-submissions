class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        count = {}
        max_window = 0

        while r < len(s):
            count[s[r]] = count.get(s[r], 0) + 1

            max_freq = max(count.values())
            replacemets = (r - l + 1) - max_freq
            while replacemets > k:
                count[s[l]] -= 1
                l += 1
                replacemets = (r - l + 1) - max_freq
            else:
                max_window = max(max_window, r - l +1)
                r += 1
        return max_window
