class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [[nums[0]]]

        seen = set()
        path = []
        res = []

        def backtrack():
            if len(path) == len(nums):
                res.append(path.copy())
                return
            for num in nums:    
                if num in seen:
                    continue

                path.append(num)
                seen.add(num)

                
                backtrack()

                path.pop()
                seen.remove(num)

        backtrack()
        return res