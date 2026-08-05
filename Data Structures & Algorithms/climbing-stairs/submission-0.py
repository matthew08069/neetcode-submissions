class Solution:
    def climbStairs(self, n: int) -> int:
        # n = 1, return 1
        # n = 2, return 2
        # n = 3, return 3
        # n = 4, return 5
        # 1, 1, 1, 1
        # 2, 2
        # 1, 2, 1
        # 2, 1, 1
        # 1, 1, 2
        #climbStairs(n) = climbStairs(n - 1) + climbStairs(n - 2)

        result = 0
        # base case
        # n = 1, n = 2
        if n == 1:
            return 1
        if n == 2:
            return 2

        result = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return result

        