# 40. Combination Sum II

"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique 
combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.
"""

class Solution1:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def findCombinations(ind, target):
            # once the target becomes 0, there's no point exploring further.
            if target == 0:
                # Fixed: Converted list to a tuple so it can be added to a set
                my_set.add(tuple(path))
                return
            if ind == len(candidates) or candidates[ind] > target:
                return

            # Pick the current element 
            path.append(candidates[ind])
            findCombinations(ind + 1, target - candidates[ind])
            path.pop()

            # 2. Skip Duplicates Optimization (optional)
            # next_ind = ind + 1
            # while next_ind < len(candidates) and candidates[next_ind] == candidates[ind]:
            #     next_ind += 1

            # Don't pick the current element
            findCombinations(ind + 1, target)

        my_set = set()
        path = []
        candidates.sort()
        findCombinations(0, target)
        
        # Fixed: Converted the tuples inside the set back into lists for the final output
        return [list(item) for item in my_set]


class Solution2:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        def find_combi(indx, target):
            if target == 0:
                ans.append(ds.copy())  # .copy() is needed because lists are passed by reference
                return
                
            for i in range(indx, len(candidates)):
                if i > indx and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > target:
                    break

                ds.append(candidates[i])
                find_combi(i + 1, target - candidates[i], ds, ans)
                ds.pop()

        candidates.sort()
        ans = []
        ds = []
        find_combi(0, target, ds, ans)
        
        return ans

