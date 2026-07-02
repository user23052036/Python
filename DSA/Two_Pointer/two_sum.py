from typing_extensions import List

class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]
        return []


class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = []
        for i,num in enumerate(nums):
            arr.append((num,i))
        arr.sort(key=lambda x:x[0])

        left = 0
        right = len(arr)-1

        while left<right:
            total = arr[left][0] + arr[right][0]

            if total == target:
                return [arr[left][1], arr[right][1]]
            elif total < target:
                left += 1
            else:
                right -= 1


class Solution3:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dick = {}

        for indx,num in enumerate(nums):
            my_dick[num] = indx

        for indx,num in enumerate(nums):
            complement_indx = my_dick.get(target - num, -1)
            
            if complement_indx != -1 and complement_indx != indx:
                return [indx, complement_indx]
            

class Solution4:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dick = {}
        for i in range(len(nums)):
            curr_indx = i
            complement_val = target - nums[i]
            complement_indx = my_dick.get(complement_val,-1)
            if complement_indx != -1:
                return [curr_indx,complement_indx] 
            my_dick[nums[i]] = curr_indx


        