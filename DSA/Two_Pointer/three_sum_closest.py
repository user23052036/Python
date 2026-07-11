# 16. 3Sum Closest

"""
Given an integer array nums of length n and an integer target, find three integers at distinct indices 
in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.


Example 1:
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).


Example 2:
Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
"""

# Sort array and use two pointers to find triplet sum closest to target.
import math
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int: # type: ignore
        nums.sort(key=None, reverse=False)
        min_diff = math.inf
        result_sum = 0

        for i in range(len(nums-2)):
            left = i+1
            right = len(nums)-1

            while left<right:
                curr_sum = nums[i]+nums[left]+nums[right]
                curr_diff = abs(target-curr_sum)

                if curr_diff<min_diff:
                    min_diff = curr_diff
                    result_sum = curr_sum
                
                # now exactly same as two-sum problem structure
                if curr_sum == target:
                    return curr_sum
                elif curr_sum>target:
                    right -= 1
                else:
                    left += 1
        return result_sum
