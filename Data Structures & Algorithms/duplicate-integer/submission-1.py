class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        tmp = set(nums)

        if len(tmp) != len(nums):
            return True
        return False