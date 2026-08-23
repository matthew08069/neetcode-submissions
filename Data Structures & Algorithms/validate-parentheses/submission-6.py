class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False

        stack = []

        for c in s:
            if c == ")":
                if not stack:
                    return False
                p = stack.pop()
                if p != "(":
                    return False
            elif c == "}":
                if not stack:
                    return False
                p = stack.pop()
                if p != "{":
                    return False
            elif c == "]":
                if not stack:
                    return False
                p = stack.pop()
                if p != "[":
                    return False
            else:
                stack.append(c)

        return not stack
