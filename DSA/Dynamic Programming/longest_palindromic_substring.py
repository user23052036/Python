# 5. Longest Palindromic Substring

"""
Input: s = "babad"
Output: "bab"

Input: s = "cbbd"
Output: "bb"
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:

        def check_palindrome(s):
            n = len(s)
            for i in range(n//2):
                if s[i] != s[n-1-i]:
                    return False
            return True

        def backtrack(start,end):
            if start > end:
                return -1,""

            if dp[start][end] != "":
                return len(dp[start][end]),dp[start][end]

            if check_palindrome(s[start:end+1]):
                dp[start][end] = s[start:end+1]
                return len(dp[start][end]),dp[start][end]
            
            len1,s1 = backtrack(start+1, end)
            len2,s2 = backtrack(start, end-1)

            if len1>=len2:
                dp[start][end] = s1
                return len1,s1
            else:
                dp[start][end] = s2
                return len2,s2
        
        n = len(s)
        dp = [[""]*n for _ in range(n)]
        palindrome = ""
        _,palindrome = backtrack(0,len(s)-1)
        return palindrome