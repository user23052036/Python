# 525. Contiguous Array

"""
Given a binary array nums, return the maximum length of a contiguous subarray with an equal 
number of 0 and 1.

 

Example 1:

Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
Example 2:

Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
Example 3:

Input: nums = [0,1,1,1,1,1,0,0,0]
Output: 6
Explanation: [1,1,1,0,0,0] is the longest contiguous subarray with equal number of 0 and 1.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
"""

from typing import List

class Solution1:
    def findMaxLengthThreeElements(self, nums: List[int]) -> int:
        # Map stores the first time we see the tuple (diff_zero_one, diff_one_two)
        # Base case: at index -1, counts are 0, so differences are (0, 0)
        seen = {(0, 0): -1}

        cnt_zero = 0
        cnt_one = 0
        cnt_two = 0
        max_len = 0
        
        for i, num in enumerate(nums):
            if num == 0:
                cnt_zero += 1
            elif num == 1:
                cnt_one += 1
            elif num == 2:
                cnt_two += 1
                
            # Form the unique state tuple
            state = (cnt_zero - cnt_one, cnt_one - cnt_two)
            if state in seen:
                max_len = max(max_len, i - seen[state])
            else:
                seen[state] = i
        return max_len


class Solution2:
    def findMaxLength(self, nums: List[int]) -> int:
        index_dict = {0:-1}
        running_sum = 0
        max_len = 0
        
        for i,num in enumerate(nums):
            pivot = 2*num - 1
            running_sum += pivot

            if running_sum in index_dict:
                curr_len = i-index_dict.get(running_sum)
                max_len = max(max_len,curr_len)
            else:
                index_dict[running_sum] = i # only we are storing the first occurance
        return max_len