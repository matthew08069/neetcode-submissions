class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        min_arr_size = float("inf")
        cur_sum = 0

        for r in range(len(nums)):
            cur_sum += nums[r]
            while cur_sum >= target:
                min_arr_size = min(min_arr_size, r - l + 1)
                cur_sum -= nums[l]
                l += 1

        return min_arr_size if min_arr_size != float("inf") else 0
