class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        for i in range(len(arr)):
            # Check if i is at the last index
            if i == len(arr) - 1:
                arr[i] = -1
                break
            arr[i] = max(arr[i+1:])
        return arr