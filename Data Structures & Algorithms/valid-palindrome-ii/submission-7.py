class Solution:
    def validPalindrome(self, s: str) -> bool:
        def palindrome(l, r):
            while l <= r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        l, r = 0, len(s) - 1

        while l <= r:
            if s[l] != s[r]:
                # Try removing s[l]
                if palindrome(l+1, r):
                    return True
                else:
                    # Try removing s[r]
                    return palindrome(l, r-1)
            l += 1
            r -= 1

        return True
