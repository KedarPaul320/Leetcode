class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        def backtrack(remain, start, path):
            if remain == 0:
                result.append(path)
                return
            for i in range(start, len(candidates)):
                if candidates[i] > remain:
                    continue
                backtrack(remain - candidates[i], i, path + [candidates[i]])
        
        candidates.sort()
        result = []
        backtrack(target, 0, [])
        return result