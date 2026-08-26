class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need_dict = {}
        have_dict = {}

        for i in t:
            need_dict[i] = need_dict.get(i, 0) + 1

        l, r = 0, 0
        need = len(need_dict)
        have = 0
        best_len = float("inf")
        best_l = 0
        best_r = 0

        while r < len(s):
            # add s[r] into have_dict
            have_dict[s[r]] = have_dict.get(s[r], 0) + 1

            # check if meet a requirement, if yes, have += 1
            if s[r] in need_dict and have_dict[s[r]] == need_dict[s[r]]:
                have += 1

            while have == need:
                if r - l + 1 < best_len:
                    best_len = r - l + 1
                    best_l = l
                    best_r = r
                have_dict[s[l]] -= 1

                if s[l] in need_dict and have_dict[s[l]] < need_dict[s[l]]:
                    have -= 1

                l += 1
            r += 1
        if best_len == float("inf"):
            return ""

        return s[best_l : best_r + 1]
