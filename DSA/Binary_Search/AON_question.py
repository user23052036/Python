"""
The sequence consists of all positive integers x such that either:

x % k == 0 (divisible by k), or
The decimal representation of x contains the digit k. when k<=9

3, 6, 9, 12, 13, 15, 18, 21, 23, 24, 27, 30, 31, 32, 33, 34, ...
"""

class solution1:
    def check_digit(self, num,k):
        while num:
            digit = num%10
            if digit==k:
                return True
            num /= 10
        return False
    
    def nth_term(self, k, n):

        if k>9:
            return k*n

        count = 0
        num = k
        while True:
            if num%k == 0 or self.check_digit(num,k):        # str(k) in str(num) easier method can be used
                count += 1
                if count == n:
                    return num
            num += 1


# dont know how to implement count function
class solution2:
    def nth_term(self,k,n):
        if k>9:
            return k*n
        
        left = k
        right = k*n
        ans = 0

        while left<right:
            mid = (left+right)//2

            if self.count(mid,k)>=n:
                ans = mid
                high = mid-1
            else:
                low = mid+1
        return ans
    
k = int(input())
n = int(input())
obj = solution1()
print(obj.nth_term(k,n))

