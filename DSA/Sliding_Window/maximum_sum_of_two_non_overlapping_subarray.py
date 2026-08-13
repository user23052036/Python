# 1031. Maximum Sum of Two Non-Overlapping Subarrays



# this greedy soln does not work because of the below test case

# [8,20,6,2,20,17,6,3,20,8,12]
# firstLen = 5
# secondLen = 4
# ans = 108
class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int):

        # the idea is that we use fixed sliding widow in two cynarios
        # 1. run the firstLen and secondLen that gets us maxi1 and similarly
        # 2. run the secondLen first and then firstLen we will get maxi2
        # we will return the max(maxi1,maxi2)
        # remember the exclude the overlapping case

        # ---------------- Scenario 1 ----------------
        # Find best firstLen window

        maxi = 0
        mover = 0
        while mover < firstLen:
            maxi += nums[mover]
            mover += 1

        start1 = 0
        end1 = firstLen - 1

        indx = 0
        curr = maxi

        while mover < len(nums):
            curr = curr - nums[indx] + nums[mover]
            indx += 1

            if curr > maxi:
                maxi = curr
                start1 = indx
                end1 = mover

            mover += 1

        firstWindow = maxi

        # Find best secondLen window excluding overlap

        maxi = 0
        mover = 0
        while mover < secondLen:
            maxi += nums[mover]
            mover += 1

        start2 = 0
        end2 = secondLen - 1

        bestSecond = 0

        if end2 < start1 or start2 > end1:
            bestSecond = maxi

        indx = 0
        curr = maxi

        while mover < len(nums):
            curr = curr - nums[indx] + nums[mover]
            indx += 1

            start2 = indx
            end2 = mover

            if (end2 < start1 or start2 > end1) and curr > bestSecond:
                bestSecond = curr

            mover += 1

        maxi1 = firstWindow + bestSecond

        # ---------------- Scenario 2 ----------------
        # Find best secondLen window

        maxi = 0
        mover = 0
        while mover < secondLen:
            maxi += nums[mover]
            mover += 1

        start2 = 0
        end2 = secondLen - 1

        indx = 0
        curr = maxi

        while mover < len(nums):
            curr = curr - nums[indx] + nums[mover]
            indx += 1

            if curr > maxi:
                maxi = curr
                start2 = indx
                end2 = mover

            mover += 1

        secondWindow = maxi

        # Find best firstLen window excluding overlap

        maxi = 0
        mover = 0
        while mover < firstLen:
            maxi += nums[mover]
            mover += 1

        start1 = 0
        end1 = firstLen - 1

        bestFirst = 0

        if end1 < start2 or start1 > end2:
            bestFirst = maxi

        indx = 0
        curr = maxi

        while mover < len(nums):
            curr = curr - nums[indx] + nums[mover]
            indx += 1

            start1 = indx
            end1 = mover

            if (end1 < start2 or start1 > end2) and curr > bestFirst:
                bestFirst = curr

            mover += 1

        maxi2 = secondWindow + bestFirst

        return max(maxi1, maxi2)