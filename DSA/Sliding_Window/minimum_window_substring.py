# 76. Minimum Window Substring

"""
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s 
such that every character in t (including duplicates) is included in the window. If there is no such 
substring, return the empty string "".


Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"


Input: s = "a", t = "a"
Output: "a"


Input: s = "a", t = "aa"
Output: ""
"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""

        map = [0]*52
        def char_to_indx(ch):
            if 'a'<= ch <='z':
                return ord(ch)-ord('a')
            return ord(ch) - ord('A')+26
        
        def check_map():
            for i in range(52):
                if map[i]>0:
                    return False
            return True
        
        left = 0
        right = 0
        mini_size = float('inf')
        start = mini_size
        end = mini_size

        # store all the t charecters in map
        for ch in t:
            indx = char_to_indx(ch)
            map[indx] += 1
        
        while right<len(s):
            indx = char_to_indx(s[right])
            map[indx] -= 1

            while check_map():
                # update the pointers
                curr_len = right-left+1
                if curr_len < mini_size:
                    mini_size = curr_len
                    start = left
                    end = right
                
                left_indx = char_to_indx(s[left])
                map[left_indx] += 1
                left += 1

            right += 1
        
        if start==float('inf'):
            return ""
        return s[start:end+1]