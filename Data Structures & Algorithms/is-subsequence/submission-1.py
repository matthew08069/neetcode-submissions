class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_pointer, t_pointer = 0, 0

        while s_pointer < len(s) and t_pointer < len(t):
            # If char at s == char at t, incerement both pointers
            if s[s_pointer] == t[t_pointer]:
                s_pointer += 1
                t_pointer += 1
            # If they are not the same, search for the next match in t
            else:
                t_pointer += 1

        if s_pointer < len(s):
            return False
        return True
