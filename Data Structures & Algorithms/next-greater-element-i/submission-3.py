class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1Idx = {}
        for i, num in enumerate(nums1):
            nums1Idx[num] = i
        # nums1Idx = {
        #                 4: 0,
        #                 1: 1,
        #                 2: 2
        #             }
        res = [-1] * len(nums1)

        for i in range(len(nums2)):
            if nums2[i] in nums1Idx:
                for j in range(i+1, len(nums2)):
                    if nums2[j] > nums2[i]:
                        idx = nums1Idx[nums2[i]]
                        res[idx] = nums2[j]
                        break

        # stack = []
        # for i in range(len(nums2)):
        #     cur = nums2[i]
        #     while stack and cur > stack[-1]:
        #         val = stack.pop()
        #         idx = nums1Idx[val]
        #         res[idx] = cur
        #     if cur in nums1Idx:
        #         stack.append(cur)
        return res