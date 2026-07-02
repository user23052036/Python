# 1189. Maximum Number of Balloons

"""
Given a string text, you want to use the characters of text to form as many instances of the word 
"balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances 
that can be formed.

Input: text = "nlaebolko"
Output: 1

Input: text = "loonbalxballpoon"
Output: 2

Input: text = "leetcode"
Output: 0
"""

class Solution1:
    def maxNumberOfBalloons(self, text: str) -> int:
        freq = {}
        cnt = 0

        for ch in text:
            freq[ch] = freq.get(ch,0)+1

        cnt = min(freq.get('b',0), freq.get('a',0), 
                  freq.get('l',0)//2, freq.get('o',0)//2,
                  freq.get('n',0))
        return cnt
    

class Solution2:
    def maxNumberOfBalloons(self, text: str) -> int:
        freq = {}
        cnt = 0

        for ch in text:
            freq[ch] = freq.get(ch,0)+1

            if (freq.get('b',0)>=1 and freq.get('a',0)>=1 and
                freq.get('l',0)>=2 and freq.get('o',0)>=2 and freq.get('n',0)>=1):
                # remove the current frequency
                freq['b'] -= 1
                freq['a'] -= 1
                freq['l'] -= 2
                freq['o'] -= 2
                freq['n'] -= 1
                cnt += 1
        return cnt
            
        
            
        