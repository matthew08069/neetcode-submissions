class Solution:
    def calculate(self, s: str) -> int:
        def helper(i):
            stack = []
            num = 0
            op = "+"

            while i < len(s):
                char = s[i]

                if char.isdigit():
                    num = num * 10 + int(char)

                elif char == "(":
                    num, i = helper(i + 1)

                if char in "+-*/)" or i == len(s) - 1:
                    if op == "+":
                        stack.append(num)
                    elif op == "-":
                        stack.append(-num)
                    elif op == "*":
                        stack.append(stack.pop() * num)
                    elif op == "/":
                        stack.append(int(stack.pop() / num))

                    num = 0
                    op = char

                if char == ")":
                    return sum(stack), i

                i += 1

            return sum(stack), i

        result, _ = helper(0)
        return result