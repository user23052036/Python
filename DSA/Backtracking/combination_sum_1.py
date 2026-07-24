# 39. Combination Sum

"""
Given an array of distinct integers candidates and a target integer target, return a list of all 
unique combinations of candidates where the chosen numbers sum to target. You may return the 
combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique
 if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less 
than 150 combinations for the given input.


Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

Input: candidates = [2], target = 1
Output: []
"""

class Solution1:
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



class Solution2:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def findCombinations(ind, target):
            # Found a valid combination
            if target == 0:
                ans.append(path.copy())
                return

            # Reached the end of the array
            if ind == len(candidates):
                return

            # Since the array is sorted, no later element can fit either
            if candidates[ind] > target:
                return

            # Pick the current element (can pick it again)
            path.append(candidates[ind])
            findCombinations(ind, target - candidates[ind])
            path.pop()

            # Don't pick the current element
            findCombinations(ind + 1, target)

        candidates.sort()   # Sort first

        ans = []
        path = []
        findCombinations(0, target)
        return ans



class Solution3:
    def combinationSum(self, candidates: List[int], target: int):
        def findCombinations(start, target):
            # Found a valid combination
            if target == 0:
                ans.append(path.copy())
                return

            # Try every candidate starting from 'start'
            for i in range(start, len(candidates)):
                # Since the array is sorted, no need to check further
                if candidates[i] > target:
                    break

                path.append(candidates[i])
                findCombinations(i, target - candidates[i]) # Pass 'i' (not i + 1) because we can reuse 
                path.pop()

        candidates.sort()

        ans = []
        path = []
        findCombinations(0, target)
        return ans