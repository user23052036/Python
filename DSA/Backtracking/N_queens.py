# 51. N-Queens

"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens 
attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, 
where 'Q' and '.' both indicate a queen and an empty space, respectively.


Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

Input: n = 1
Output: [["Q"]]
"""

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def isSafe(row,col):

            temprow = row
            tempcol = col
            # check for up lower diagonal
            while col>=0 and row>=0:
                if board[row][col] == 'Q':
                    return False
                row -= 1
                col -= 1

            row = temprow
            col = tempcol
            # check for back
            while col>=0:
                if board[row][col] == 'Q':
                    return False
                col -= 1
            
            row = temprow
            col = tempcol
            # check for back lower diagonal
            while col>=0 and row<n:
                if board[row][col] == 'Q':
                    return False
                row += 1
                col -= 1
            return True
        
        def backtrack(col):
            if col==n:
                ans.append(["".join(row) for row in board])
                return
            
            for row in range(n):
                if isSafe(row,col):
                    board[row][col] = 'Q'
                    backtrack(col+1)
                    board[row][col] = '.'
        
        ans = []
        board = []
        for i in range(n):
            board.append(['.']*n)
        
        backtrack(0)
        return ans