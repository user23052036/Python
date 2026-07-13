# 409. Longest Palindrome

"""
Given a string s which consists of lowercase or uppercase letters, return the length of the longest 
palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome.

 
Example 1:
Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

Example 2:
Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.
 

Constraints:

1 <= s.length <= 2000
s consists of lowercase and/or uppercase English letters only.
"""

class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = {}
        cnt = 0
        ans = 0

        for ch in s:
            freq[ch] = freq.get(ch,0)+1
        for key,value in freq.items():
            if value%2==0:
                ans += value
            else:
                ans += value-1
                cnt += 1
        if cnt:
            return ans+1
        return ans

# Input
s = input()

# Output
obj = Solution()
print(obj.longestPalindrome(s))