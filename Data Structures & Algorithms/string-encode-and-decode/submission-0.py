class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""

        for word in strs:
            res += str(len(word)) + "#" + word

        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        j = i
        res = []

        while i < len(s):
            if s[j] == "#":
                length = int(s[i:j])
                word = s[j + 1 : j + 1 + length]
                res.append(word)
                i = j + 1 + length
                j = i
            else:
                j += 1

        return res
