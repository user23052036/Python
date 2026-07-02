# 1209. Remove All Adjacent Duplicates in String II

"""
Example 1:
Input: s = "abcd", k = 2
Output: "abcd"
Explanation: There's nothing to delete.


Example 2:
Input: s = "deeedbbcccbdaa", k = 3
Output: "aa"
Explanation: 
First delete "eee" and "ccc", get "ddbbbdaa"
Then delete "bbb", get "dddaa"
Finally delete "ddd", get "aa"


Example 3:
Input: s = "pbbcggttciiippooaais", k = 2
Output: "ps"
 

Constraints:

1 <= s.length <= 105
2 <= k <= 104
s only contains lowercase English letters.
"""

from collections import deque
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = deque()
        for ch in s:
            if stack:
                # unpacking
                charecter,freq = stack[-1]

                if charecter == ch:
                    # removing top k frequency
                    if freq+1 == k:
                        temp = freq
                        while temp>0:
                            stack.pop()
                            temp -= 1
                    else:
                        stack.append((ch,freq+1))
                else:
                    stack.append((ch,1))
            else:
                stack.append((ch,1))

        answer = ""
        while stack:
            ch,freq = stack.popleft()
            answer += ch
        return answer

                