class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def backtrack(start):
            # Base case path is complete
            if sum(path) == target:
                res.append(path.copy())
                return
            elif sum(path) > target:
                return

            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i)
                path.pop()

        backtrack(0)
        return res


