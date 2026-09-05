class Solution:
    def calculate(self, s: str) -> int:
        operator = ["+", "-", "*", "/"]
        res = []
        num = 0
        op = "+"

        for i in range(len(s)):
            char = s[i]

            if char.isdigit():
                num = num * 10 + int(char)

            if char in operator or i == len(s) - 1:
                if op == "+":
                    res.append(num)
                elif op == "-":
                    res.append(-num)
                elif op == "*":
                    num = res.pop() * num
                    res.append(num)
                elif op == "/":
                    num = int(res.pop() / num)
                    res.append(num)

                op = char
                num = 0

        return sum(res)
