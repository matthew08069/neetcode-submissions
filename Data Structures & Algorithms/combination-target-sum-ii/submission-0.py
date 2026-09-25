class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        candidates.sort()

        def backtracking(start, cur_sum):
            # Base
            if cur_sum == target:
                res.append(path.copy())
                return
            
            for i in range(start, len(candidates)):
                # Skip duplicate branch
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # Pruning   
                if cur_sum > target:
                    break

                # Choose
                path.append(candidates[i])

                # Explore
                backtracking(i + 1, cur_sum + candidates[i])

                # Undo
                path.pop()

        backtracking(0, 0)

        return res


