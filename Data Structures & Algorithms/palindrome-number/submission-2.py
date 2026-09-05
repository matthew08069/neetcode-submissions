class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = x
        new_x = 0

        while num > 0:
            new_x = new_x * 10 + (num % 10)
            num = int(num / 10)
        if new_x != x:
            return False
        return True
