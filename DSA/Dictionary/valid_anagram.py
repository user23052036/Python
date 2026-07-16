# 242. Valid Anagram

"""
Input: s = "anagram", t = "nagaram"
Output: true

Input: s = "rat", t = "car"
Output: false
"""

class Solution1:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq = [0]*26

        for ch in s:
            freq[ord(ch) - ord('a')] += 1
        for ch in t:
            freq[ord(ch) - ord('a')] -= 1

        for val in freq:
            if val<0:
                return False
        return True
    

class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}
        for ch in s:
            count[ch] = count.get(ch, 0) + 1
        for ch in t:
            if ch not in count:
                return False

            count[ch] -= 1
            if count[ch] == 0:
                del count[ch]
        return len(count) == 0