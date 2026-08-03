# https://www.naukri.com/code360/problems/frog-jump_3621012

"""
There is a frog on the '1st' step of an 'N' stairs long staircase. The frog wants to reach the 'Nth' stair. 
'HEIGHT[i]' is the height of the '(i+1)th' stair.If Frog jumps from 'ith' to 'jth' stair, the energy lost in 
the jump is given by absolute value of ( HEIGHT[i-1] - HEIGHT[j-1] ). If the Frog is on 'ith' staircase, he can 
jump either to '(i+1)th' stair or to '(i+2)th' stair. Your task is to find the minimum total energy used by the 
frog to reach from '1st' stair to 'Nth' stair.

For Example
If the given ‘HEIGHT’ array is [10,20,30,10], the answer 20 as the frog can jump from 1st stair to 2nd stair 
(|20-10| = 10 energy lost) and then a jump from 2nd stair to last stair (|10-20| = 10 energy lost). So, the 
total energy lost is 20.


10 20 30 10
20

10 50 10
0 

7 4 4 2 6 6 3 4 
7

4 8 3 10 4 4 
2
"""

def frogJump(n: int, heights: List[int]) -> int:
    def recursion(indx):
        if indx==0:
            return 0
        
        if dp[indx] != -1:
            return dp[indx]

        left = abs(heights[indx]-heights[indx-1]) + recursion(indx-1)

        right = float('inf')
        if indx-2>=0:
            right = abs(heights[indx]-heights[indx-2]) + recursion(indx-2)

        dp[indx] = min(left,right)
        return dp[indx]
    
    n = len(heights)
    dp = [-1]*(n)
    return recursion(n-1)



def frogJump(n: int, heights: List[int]) -> int:

    def tabulation():

        dp[0] = 0
        for i in range(1,len(heights)):
            prev = dp[i-1] + abs(heights[i]-heights[i-1])
            prev2 = float('inf')
            if i-2>=0:
                prev2 = dp[i-2] + abs(heights[i]-heights[i-2])
            
            dp[i] = min(prev,prev2)
        return dp[-1]
    
    dp = [0]*(len(heights))
    return tabulation()



def frogJump(n: int, heights: List[int]) -> int:
    prev2 = 0   # dp[0]
    prev = 0    # dp[0]

    for i in range(1, n):
        one_jump = prev + abs(heights[i] - heights[i - 1])

        two_jump = float('inf')
        if i >= 2:
            two_jump = prev2 + abs(heights[i] - heights[i - 2])

        curr = min(one_jump, two_jump)

        prev2 = prev
        prev = curr
    return prev

