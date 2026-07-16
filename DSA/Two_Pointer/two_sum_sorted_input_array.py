# 167. Two Sum II - Input Array Is Sorted

class Solution1:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        my_dict = {}
        for i in range(len(numbers)):
            complement = target-numbers[i]
            complement_indx = my_dict.get(complement,-1)

            if complement_indx!=-1:
                return [complement_indx+1,i+1]
            my_dict[numbers[i]] = i


class Solution2:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # not efficient solution as tc O(nlogN)
        n = len(numbers)

        for i in range(n):
            left, right = i+1, n-1
            complement = target - numbers[i]

            while left <= right:
                mid = (left + right) // 2

                if numbers[mid] == complement:
                    return [i+1, mid+1]
                elif numbers[mid] < complement:
                    left = mid+1
                else:
                    right = mid-1


class Solution3:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Two-pointer approach
        left, right = 0, len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]

            if current_sum == target:
                return [left + 1, right + 1]
            elif current_sum > target:
                right -= 1
            else:
                left += 1