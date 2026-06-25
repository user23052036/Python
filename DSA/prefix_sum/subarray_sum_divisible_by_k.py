# 974. Subarray Sums Divisible by K

"""
Given an integer array nums and an integer k, return the number of 
non-empty subarrays that have a sum divisible by k.
A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [4,5,0,-2,-3,1], k = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by k = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
Example 2:

Input: nums = [5], k = 9
Output: 0
 

Constraints:

1 <= nums.length <= 3 * 104
-104 <= nums[i] <= 104
2 <= k <= 104
"""

from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        running_sum = 0
        ans_count = 0
        prefix_sum_dict = {0:1}

        for num in nums:
            running_sum += num
            rem = running_sum%k

            ans_count += prefix_sum_dict.get(rem,0)
            prefix_sum_dict[rem] = prefix_sum_dict.get(rem,0)+1
        return ans_count