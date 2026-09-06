class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # A dictionary with {bi:ai}
        table = {}
        trusters = set()

        for i in trust:
            if i[1] in table:
                table[i[1]].append(i[0])
                trusters.add(i[0])
                continue
            table[i[1]] = [i[0]]
            trusters.add(i[0])

        for canidate in table:
            if len(table[canidate]) == n - 1:
                if not canidate in trusters:
                    return canidate

        return -1
            
            