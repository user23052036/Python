# 1021. Remove Outermost Parentheses

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        counter = 0
        ans = ''
        for i in range(len(s)):
            if s[i]==')':
                counter -= 1
            if counter!=0:
                ans += s[i]
            if s[i]=='(':
                counter += 1
        return ans

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = ''
        left = 0
        right = 0
        open_cnt = 0
        close_cnt = 0

        while right<len(s):
            if s[right]=='(':
                open_cnt += 1
            else:
                close_cnt += 1

            if open_cnt==close_cnt:
                for i in range(left+1,right):
                    ans += s[i]
                left = right+1
            right += 1

        return ans
