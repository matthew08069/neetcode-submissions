class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        for i in range(len(digits) - 1, 0, -1):
            # # Last digit plus 1
            # if i == len(digits) - 1 or carry == 1:
            #     digits[i] += 1
            #     carry = 0
            # # if digit = 10
            # if digits[i] == 10:
            #     digits[i] = 0
            #     carry = 1
            # if i == 0 and carry == 1:
            #     prefix = [1]
            #     digits = prefix + digits
            
            if digits[i] < 10:
                return digits
            else:
                digits[i] = 0
                digits[i - 1] += 1
        if digits[0] == 10:
            digits[0] = 0
            digits = [1] + digits
        
        return digits
            