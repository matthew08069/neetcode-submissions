class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(cur, open_count, close_count):

            if open_count == n and close_count == n:
                # Complete
                res.append(cur)
                return

            if open_count < n:
                # Add "("
                backtrack(cur + "(", open_count + 1, close_count)

            if close_count < open_count:
                # Add ")"
                backtrack(cur + ")", open_count, close_count + 1)

        backtrack("", 0, 0)

        return res
