class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        i, j, k = 0, 1, len(nums) - 1
        res = 0

        while i <= len(nums) - 3:
            if nums[i] + nums[j] + nums[k] < target:
                res += k - j
                j += 1
            elif nums[i] + nums[j] + nums[k] >= target:
                k -= 1
            if j == k:
                i += 1
                j = i + 1
                k = len(nums) - 1

        return res
