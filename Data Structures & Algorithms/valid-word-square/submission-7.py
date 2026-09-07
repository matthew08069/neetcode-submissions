class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        for row in range(len(words)):
            for col in range(len(words[row])):
                if col >= len(words):
                    return False

                if row >= len(words[col]):
                    return False
                # check words[row][col] against words[col][row]
                if words[row][col] != words[col][row]:
                    return False

        return True