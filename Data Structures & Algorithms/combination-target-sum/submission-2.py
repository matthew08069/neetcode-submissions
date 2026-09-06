class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def backtrack(start, cur_sum):
            # Base case path is complete
            if cur_sum == target:
                res.append(path.copy())
                return
            elif cur_sum > target:
                return

            for i in range(start, len(nums)):
                path.append(nums[i])
                cur_sum += nums[i]
                backtrack(i, cur_sum)
                path.pop()
                cur_sum -= nums[i]

        backtrack(0, 0)
        return res
