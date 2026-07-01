# 7. Reverse Integer

"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go 
outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:
Input: x = 123
Output: 321


Example 2:
Input: x = -123
Output: -321


Example 3:
Input: x = 120
Output: 21
 

Constraints:
-231 <= x <= 231 - 1
"""

class Solution:
    def reverse(self, x: int) -> int:
        reversed_num = 0
        sign = -1 if x<0 else 1
        x = abs(x)

        while x!=0:
            last_dig = x%10
            x //= 10
            reversed_num = reversed_num*10 + last_dig
        reversed_num *= sign

        if -(2**31) <= reversed_num <= ((2**31)-1):
            return reversed_num
        return 0