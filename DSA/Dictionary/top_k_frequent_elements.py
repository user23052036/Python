# 347. Top K Frequent Elements

"""
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2
Output: [1,2]

Input: nums = [1], k = 1
Output: [1]
"""

# sort map by frequency
class Solution1:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_map = {}

        for num in nums:
            my_map[num] = my_map.get(num,0)+1
        
        # sort dict by value descending
        sorted_keys = list(sorted(my_map.keys(), key=lambda x: my_map[x], reverse=True))
        return sorted_keys[:k]


# bucket sort solution
class Solution2:
    def topKFrequent(self, nums, k):
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        buckets = [[] for _ in range(len(nums) + 1)]

        for num, count in freq.items():
            buckets[count].append(num)

        ans = []
        for count in range(len(buckets) - 1, -1, -1):
            for num in buckets[count]:
                ans.append(num)
                if len(ans) == k:
                    return ans
                
"""
Bucket Sort (O(n)) ⭐⭐⭐⭐⭐ — Best answer for this problem.
Min Heap (O(n log k)) ⭐⭐⭐⭐ — Best when k is much smaller than the number of unique elements.
Sorting (O(n log n)) ⭐⭐⭐ — Simple and easy to explain.
"""