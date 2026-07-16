# 42. Trapping Rain Water

class Solution:
    def trap(self, height: List[int]) -> int:
        
        size = len(height)
        # two arrays to store left-maxand right-max
        left_max = [0]*size
        left_max[0] = height[0]

        right_max = [0]*size
        right_max[size-1] = height[size-1]

        for i in range(1,size):
            left_max[i] = max(left_max[i-1], height[i-1])
        
        for i in range(size-2, -1,-1):
            right_max[i] = max(right_max[i+1], height[i+1])
        
        water = 0
        for i in range(size):
            pos = min(left_max[i], right_max[i]) - height[i]
            if pos>0:
                water += pos
        return water
