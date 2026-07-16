# https://neetcode.io/problems/string-encode-and-decode/question

class Solution:

    def encode(self, strs: List[str]) -> str:
        encode = ""

        for word in strs:
            encode += str(len(word)) + '#' + word
        return encode

    def decode(self, s: str) -> List[str]:
        res = []
        i=0
        while i<len(s):
            j=i
            while s[j]!= '#':
                j+=1
            digit = int(s[i:j])
            res.append(s[j+1:j+1+digit])
            i = j+1+digit
        return res