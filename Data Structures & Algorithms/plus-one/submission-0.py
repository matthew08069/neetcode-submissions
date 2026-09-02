class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0

        for i in range(len(digits) - 1, -1, -1):
            # Last digit plus 1
            if i == len(digits) - 1 or carry == 1:
                digits[i] += 1
                carry = 0
            # if digit = 10
            if digits[i] == 10:
                digits[i] = 0
                carry = 1
            if i == 0 and carry == 1:
                prefix = [1]
                digits = prefix + digits
        
        return digits
            