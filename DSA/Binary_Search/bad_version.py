# 278. First Bad Version

"""
You are a product manager and currently leading a team to develop a new product. Unfortunately, 
the latest version of your product fails the quality check. Since each version is developed based on the 
previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the 
following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function 
to find the first bad version. You should minimize the number of calls to the API.
"""

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

def isBadVersion(version):
    return version >= first_bad


class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 1
        high = n
        ans = n+1

        while low<=high:
            mid = low + (high-low)//2

            if isBadVersion(mid):
                ans = mid
                high = mid-1
            else:
                low = mid+1

        return ans


# Input
n = int(input("Enter total number of versions: "))
first_bad = int(input("Enter first bad version: "))

# Output
obj = Solution()
print("First Bad Version:", obj.firstBadVersion(n))