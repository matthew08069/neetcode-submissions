class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix = [1] * len(nums)
        # suffix = [1] * len(nums)
        # res = [1] * len(nums)

        # for i in range(1, len(nums)):
        #     prefix[i] = nums[i - 1] * prefix[i - 1]

        # for i in range(len(nums) -2, -1, -1):
        #     suffix[i] = nums[i + 1] * suffix[i + 1]

        # for i in range(len(res)):
        #     res[i] = prefix[i] * suffix[i]

        # return res
        res = [1] * len(nums)

        left_product = 1
        for i in range(len(nums)):
            res[i] = left_product
            left_product *= nums[i]

        right_product = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= right_product
            right_product *= nums[i]
            

        return res