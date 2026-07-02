# 383. Ransom Note

"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by 
using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.
"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_freq = {}
        for ch in magazine:
            magazine_freq[ch] = magazine_freq.get(ch,0)+1
        for ch in ransomNote:
            magazine_freq[ch] = magazine_freq.get(ch,0)-1
            if magazine_freq[ch]<0:
                return False
        return True