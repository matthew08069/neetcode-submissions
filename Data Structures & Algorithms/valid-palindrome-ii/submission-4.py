class Solution:
    def validPalindrome(self, s: str) -> bool:
        def palindrome(s):
            l, r = 0, len(s) - 1

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
                if palindrome(s[0:l] + s[l + 1 :]):
                    return True
                    # Try removing s[r]
                else:
                    return palindrome(s[0:r] + s[r + 1 :])
            l += 1
            r -= 1

        return True
