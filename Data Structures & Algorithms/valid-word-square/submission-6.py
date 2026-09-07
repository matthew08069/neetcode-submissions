class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        # words[row][column]
        i, j = 0, 0

        # Start at words[0][0]
        # Check if each chars equal
        # Return False if not equal
        # Move to next words[1][1]
        # If not return False
        # Return True

        # Boundary is the len(words[row])

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