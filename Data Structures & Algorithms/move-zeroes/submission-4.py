class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, 0

        while l <= r and r < len(nums):
            if nums[l] != 0:
                l += 1
                r += 1
            elif nums[r] == 0:
                r += 1
            else:
                nums[l] = nums[r]
                nums[r] = 0
                l += 1
                r += 1
