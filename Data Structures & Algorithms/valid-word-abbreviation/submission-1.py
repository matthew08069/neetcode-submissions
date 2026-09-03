class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        # w = 0
        # num = -1

        # for i in range(len(abbr)):
        #     # Check if abbr[i] is digit
        #     if abbr[i].isdigit():
        #         # Check for leading 0
        #         if num == -1 and int(abbr[i]) == 0:
        #             return False
        #         # If not the first digit, append to num
        #         elif num != -1:
        #             num = num * 10 + int(abbr[i])
        #         else:
        #             num = int(abbr[i])
        #     # When abbr[i] is not a digit and num == -1, check abbr[i] == word[w]
        #     if w < len(word):
        #         if not (num == -1 and abbr[i] == word[w]) and not abbr[i].isdigit():
        #             return False
        #         elif num != -1 and not abbr[i].isdigit():
        #             w += num
        #             if abbr[i] != word[w]:
        #                 return False
        #             num = -1
        #         elif not abbr[i].isdigit():
        #             w += 1
        #         w += num
        # return True if w == len(word) else False

        w = 0
        num = -1

        for i in range(len(abbr)):
            # Build the number
            if abbr[i].isdigit():
                # Leading zero
                if num == -1 and abbr[i] == "0":
                    return False

                if num == -1:
                    num = int(abbr[i])
                else:
                    num = num * 10 + int(abbr[i])

            else:
                # Apply previous number before checking this letter
                if num != -1:
                    w += num
                    num = -1

                # Out of bounds or character doesn't match
                if w >= len(word) or word[w] != abbr[i]:
                    return False

                w += 1

        # If abbreviation ends with a number
        if num != -1:
            w += num

        return w == len(word)
