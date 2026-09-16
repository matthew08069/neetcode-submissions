class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # l = 0
        # min_arr_size = float("inf")
        # cur_sum = 0

        # for r in range(len(nums)):
        #     cur_sum += nums[r]
        #     while cur_sum >= target:
        #         min_arr_size = min(min_arr_size, r - l + 1)
        #         cur_sum -= nums[l]
        #         l += 1

        # return min_arr_size if min_arr_size != float("inf") else 0
        prefix_sum = [0]

        for i in range(len(nums)):
            prefix_sum.append(prefix_sum[i] + nums[i])

        n = len(nums)
        res = n + 1
        for i in range(n):
            l, r = i, n
            while l < r:
                mid = (l + r) // 2
                curSum = prefix_sum[mid + 1] - prefix_sum[i]
                if curSum >= target:
                    r = mid
                else:
                    l = mid + 1
            if l != n:
                res = min(res, l - i + 1)

        return res % (n + 1)