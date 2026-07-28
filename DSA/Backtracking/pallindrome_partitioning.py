# 131. Palindrome Partitioning

"""
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Input: s = "a"
Output: [["a"]]
"""

class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def isPalindrome(left,right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True


        def cut_string(indx):
            if indx==len(s):
                ans.append(path.copy())
                return 

            for i in range(indx,len(s)):

                if isPalindrome(indx,i):
                    
                    path.append(s[indx:i+1])
                    cut_string(i+1)
                    path.pop()
        
        ans = []
        path = []
        cut_string(0)
        return ans
                