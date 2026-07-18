# 3. Longest Substring Without Repeating Characters

class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        maxi = 0
        frequency = {}

        while right<len(s):
            while frequency.get(s[right],-1) != -1:
                # shift the left pointer 
                del frequency[s[left]] 
                left += 1
            
            frequency[s[right]] = 1
            curr_len = right-left+1
            if curr_len>maxi:
                maxi = curr_len
            right += 1
        return maxi  
    

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        maxi = 0
        seen = {}  # Maps character -> its last seen index

        for right, char in enumerate(s):
            # Jump the left pointer only if the duplicate is inside our current window
            # seen[char] >= left
            # Without this check, the left pointer can accidentally move backward, which breaks the sliding window.
            if char in seen and seen[char] >= left:
                left = seen[char] + 1
            
            seen[char] = right
            maxi = max(maxi, right - left + 1)
        return maxi
            