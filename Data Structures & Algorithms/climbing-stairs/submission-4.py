class Solution:
    def climbStairs(self, n: int) -> int:
        # (n-1) + (n-2) = ways to climb nth stairs
        s1 = 1
        s2 = 2

        for _ in range(n - 2):
            temp = s1
            s1 = s2
            s2 = temp + s2
        return s2 if n > 1 else s1