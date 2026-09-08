class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_val = 0
        for i in range(len(arr)-1, -1, -1):
            # Check if i is at the last index
            if i == len(arr) - 1:
                max_val = arr[i]
                arr[i] = -1
                continue
            cur = arr[i]
            arr[i] = max_val
            max_val = max(max_val, cur)
        return arr