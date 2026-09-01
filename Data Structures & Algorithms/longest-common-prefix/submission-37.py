class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # 2 loops:
        # Outer loop checks each character position of the first word.
        # Inner loop checks that character against all other words.
        # If all match, update res. If any doesn't match, return res.
        for i in range(len(strs[0])):
            for word in strs[1:]:
                if len(word) == i or strs[0][i] != word[i]:
                    return word[:i]
        return strs[0]
