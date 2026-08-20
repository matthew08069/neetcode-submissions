class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # seen = {}

        # for i, num in enumerate(nums):
        #     com = target - num

        #     if com in seen:
        #         return [seen[com], i]
            
        #     seen[com] = i

        seen = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], i]

            seen[num] = i