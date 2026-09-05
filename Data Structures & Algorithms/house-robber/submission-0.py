class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def dfs(i):
            # Base case
            # If house in memo, return the max sum from that house
            if i in memo:
                return memo[i]
            # If there's no more house can be robbed, return that house
            if i >= len(nums):
                return 0
            rob = nums[i] + dfs(i + 2)
            skip = dfs(i + 1)

            memo[i] = max(rob, skip)

            return max(rob, skip)

        return dfs(0)