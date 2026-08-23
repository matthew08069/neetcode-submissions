class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in num_set:
            if num - 1 not in num_set:
                count = 1
                next_num = num + 1

                while next_num in num_set:
                    next_num += 1
                    count += 1
                longest = max(longest, count)

        return longest
