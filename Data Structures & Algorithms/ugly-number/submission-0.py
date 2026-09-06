class Solution:
    def isUgly(self, n: int) -> bool:
        res = True
        
        while res:
            if n == 1:
                res = True
                break
            if n % 2 == 0:
                n = n/2
            elif n % 3 == 0:
                n = n/3
            elif n % 5 == 0:
                n = n/5
            else:
                res = False
                break
        return res