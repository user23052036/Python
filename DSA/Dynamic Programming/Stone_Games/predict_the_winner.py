# 486. Predict the Winner

from typing import List

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:

        def backtrack(left, right, score1, score2, player):
            if left > right:
                return score1 >= score2

            if player == 1:
                # Player 1 chooses the move that can make him win
                take_left = backtrack(left+1, right, score1+nums[left], score2, 0)
                take_right = backtrack(left, right-1, score1+nums[right], score2, 0)

                return take_left or take_right

            else:
                # Player 2 chooses the move that prevents Player 1 from winning
                take_left = backtrack(left+1, right, score1, score2+nums[left], 1)
                take_right = backtrack(left, right-1, score1, score2+nums[right], 1)

                return take_left and take_right

        return backtrack(0,len(nums)-1,0,0,1)