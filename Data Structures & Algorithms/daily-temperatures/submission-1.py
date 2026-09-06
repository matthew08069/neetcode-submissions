class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # # First loop stop at the 2nd last index
        # for i in range(len(temperatures) - 1):
        #     for j in range(i + 1, len(temperatures)):
        #         if temperatures[j] > temperatures[i]:
        #             temperatures[i] = j - i
        #             break
        #         if j == len(temperatures) - 1:
        #             temperatures[i] = 0
        #     if i == len(temperatures) - 2:
        #         temperatures[i + 1] = 0
        # return temperatures

        # Monotonic
        res = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                index = stack.pop()
                res[index] = i - index
            stack.append(i)

        return res