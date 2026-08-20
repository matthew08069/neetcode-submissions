class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check_list = []

        for i in nums:
            if not i in check_list:
                check_list.append(i)
            elif i in check_list:
                return True
        
        return False
