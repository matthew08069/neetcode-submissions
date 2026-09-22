class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # freq = {}
        # for num in nums:
        #     freq[num] = freq.get(num, 0) + 1

        # res = []
        # for num, count in freq.items():
        #     if count > len(nums) / 3:
        #         res.append(num)
        # return res

        # Boyer–Moore Voting
        num1 = None
        count1 = 0

        num2 = None
        count2 = 0

        for num in nums:
            if num == num1:
                count1 += 1
            elif num == num2:
                count2 += 1
            elif count1 == 0:
                num1 = num
                count1 = 1
            elif count2 == 0:
                num2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        recount1 = 0
        recount2 = 0

        for num in nums:
            if num == num1:
                recount1 += 1
            elif num == num2:
                recount2 += 1

        res = []
        if recount1 > len(nums) / 3:
            res.append(num1)
        if recount2 > len(nums) / 3:
            res.append(num2)

        return res

