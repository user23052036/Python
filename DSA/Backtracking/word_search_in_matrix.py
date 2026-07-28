# 79. Word Search

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(row,col,indx,visited):
            if board[row][col] != word[indx]:
                return False
            if indx == len(word)-1:
                return True
            if row<0 or row>=len(board) or col<0 or col>=len(board[0]):
                return False
            

            top,bottom,left,right = False,False,False,False

            # top case
            if row-1 >= 0 and not (row-1,col) in visited:
                visited.add((row-1,col))
                top = backtrack(row-1,col,indx+1,visited)
                visited.remove((row-1,col))

            # bottom case
            if row+1 < len(board) and not (row+1,col) in visited:
                visited.add((row+1,col))
                bottom = backtrack(row+1,col,indx+1,visited)
                visited.remove((row+1,col))

            # left case
            if col-1 >= 0 and not (row,col-1) in visited:
                visited.add((row,col-1))
                left = backtrack(row,col-1,indx+1,visited)
                visited.remove((row,col-1))

            # right case
            if col+1 < len(board[0]) and not (row,col+1) in visited:
                visited.add((row,col+1))
                right = backtrack(row,col+1,indx+1,visited)
                visited.remove((row,col+1))
            
            return top or bottom or left or right
        

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    visited = {(row,col)} # otherwise starign call will be not stored
                    if backtrack(row,col,0,visited):
                        return True
        return False


"""
Mistakes I made (LeetCode 79 - Word Search)

1. Boundary Check
-----------------
I mistakenly used:
    row + 1 <= len(board)
and
    col + 1 <= len(board[0])

Valid indices are:
    0 ... len(board)-1

Always use:
    row + 1 < len(board)
    col + 1 < len(board[0])

Otherwise recursion reaches board[len(board)] -> IndexError.


2. Base Case Position
---------------------
I checked:
    if indx == len(word):
        return True

before matching the current character.

Problem:
For a one-letter word ("A"), recursion never moves to a neighbour,
so indx never becomes len(word).

Correct order:
    1. Boundary check
    2. Character check
    3. If current character is the LAST one:
           return True
    4. Explore neighbours

So the correct base case is:
    if indx == len(word) - 1:
        return True


3. Visited Cells
----------------
Initially I only wanted to avoid going back to the previous cell.

That is NOT enough.

Example:

A B
D C

Word = "ABCDA"

Path:
A -> B -> C -> D -> A

Notice:
I never immediately returned to the previous cell,
yet I still reused the first 'A'.

Conclusion:
I must remember EVERY cell currently in the path,
not just the caller.

Current path cells are "locked" until backtracking.


4. Starting Cell
----------------
I created:
    visited = set()

but forgot to add the starting position.

Correct:
    visited = {(row, col)}

Otherwise recursion can revisit the starting cell immediately.


5. Backtracking Rule
--------------------
Before recursion:
    visited.add((newRow, newCol))

After recursion:
    visited.remove((newRow, newCol))

Always undo the choice before returning.

Mental Model:
-------------
Think of recursion as walking through a maze.

Every room already visited on the CURRENT path is locked.

Backtracking unlocks the room when returning.

The rule is NOT:
    "Don't go back to the previous room."

The rule IS:
    "Don't visit ANY room already in the current path."
"""