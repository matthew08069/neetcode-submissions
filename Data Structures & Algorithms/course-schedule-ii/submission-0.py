class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {c:[] for c in range(numCourses)}
        for cour, preq in prerequisites:
            adj[cour].append(preq)

        res = []
        visit, cycle = set(), set()

        def dfs(cour):
            if cour in cycle:
                return False
            if cour in visit:
                return True

            cycle.add(cour)
            for preq in adj[cour]:
                if dfs(preq) == False:
                    return False
            cycle.remove(cour)
            visit.add(cour)
            res.append(cour)
            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return res
