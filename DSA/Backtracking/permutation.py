# 46. Permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack():
            if len(nums)==len(path):
                ans.append(path.copy())
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                
                # choose the current
                used[i] = True
                path.append(nums[i])

                backtrack()

                used[i] = False
                path.pop()
        
        used = [False]*len(nums)
        path = []
        ans = []
        
        backtrack()
        return ans