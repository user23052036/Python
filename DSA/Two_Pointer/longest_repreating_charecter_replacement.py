# 424. Longest Repeating Character Replacement

# TLE solution
class Solution1:
    def find_max(self, s:str, left:int, right:int) -> int:
        maxi = 0
        map = [0]*26

        for i in range(left,right+1):
            index = ord(s[i])-ord('A')
            map[index] += 1
            if map[index] > maxi:
                maxi = map[index]
        return maxi

    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        max_len = 0

        while right<len(s):
            curr_len = right-left+1
            max_occurance = self.find_max(s,left,right)
            diff = curr_len - max_occurance

            while diff>k:
                # we have a problem here as the sub-string is not the answer
                left += 1
                curr_len = right-left+1
                max_occurance = self.find_max(s,left,right)
                diff = curr_len - max_occurance
            
            max_len = max(max_len, curr_len)
            right += 1
        return max_len
    


class Solution2:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0]*26
        left = 0
        right = 0
        ans = 0

        curr_len = 0
        max_freq = 0
        diff = 0

        while right<len(s):
            idx = ord(s[right]) - ord('A')
            count[idx] += 1

            curr_len = right-left+1
            max_freq = max(count)
            diff = curr_len - max_freq

            while diff > k:
                count[ord(s[left]) - ord('A')] -= 1

                curr_len -= 1
                max_freq = max(count)
                diff = curr_len - max_freq
                left += 1

            ans = max(ans, curr_len)
            right += 1
        return ans