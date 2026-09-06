class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res = []
        i = 0
        

        while len(res) < len(nums) * 2:
            res.append(nums[i])
            i+=1
            if i == len(nums):
                i = 0
        return res