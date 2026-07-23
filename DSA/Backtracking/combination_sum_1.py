# 39. Combination Sum


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def findCombinations(ind, target):
            # once the target becomes 0, there's no point exploring further.
            if target == 0:
                ans.append(path.copy())
                return
            if ind == len(candidates):
                return

            # Pick the current element (can pick it again)
            if candidates[ind] <= target:
                path.append(candidates[ind])
                findCombinations(ind, target - candidates[ind])
                path.pop()

            # Don't pick the current element
            findCombinations(ind + 1, target)

        ans = []
        path = []
        findCombinations(0, target)
        return ans