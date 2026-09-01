class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        # 2 loops:
        # Outer loop checks each character position of the first word.
        # Inner loop checks that character against all other words.
        # If all match, update res. If any doesn't match, return res.
        # if len(strs) == 1:
        #     return strs[0]

        for i in range(len(strs[0])):
            for word in strs[0:]:
                if len(word) <= i or strs[0][i] != word[i]:
                    return res
            res = strs[0][: i + 1]
        return res
