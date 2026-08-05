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
        # brute force
        # climbStairs(n) = climbStairs(n - 1) + climbStairs(n - 2)

        # result = 0
        # # base case
        # # n = 1, n = 2
        # if n == 1:
        #     return 1
        # if n == 2:
        #     return 2

        # result = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        # return result 

        # # DP top-down
        # # add cache
        # # base case
        # # n = 1, n = 2
        # def dpTopDown(n, cache):
        #     if n == 1:
        #         return 1
        #     if n == 2:
        #         return 2
        #     if n in cache:
        #         return cache[n]

        #     cache[n] = dpTopDown(n - 1, cache) + dpTopDown(n - 2, cache)
        #     return cache[n]
        # cache = {}
        # return dpTopDown(n, cache)

        # DP bottom up
        one, two = 1, 1

        for i in range(n - 1):
            temp = two
            two = one + two
            one = temp
        return two