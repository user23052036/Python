# 111. Minimum Depth of Binary Tree

"""
Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root node 
down to the nearest leaf node.
Note: A leaf is a node with no children.

Input: root = [3,9,20,null,null,15,7]
Output: 2

Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5
"""

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        if root.left is None:
            return self.minDepth(root.right)+1

        if root.right is None:
            return self.minDepth(root.left)+1

        return min(self.minDepth(root.left), self.minDepth(root.right))+1




"""
Here in this solution we are doing BFS traversal, and we will stop our search once a node is found which terminates
i.e left and right child are None, because this branch will be the smallest branch starting from the top and we 
dont need to move a level down into the tree
"""
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        flag = True
        level = 0
        q = deque()
        q.append(root)

        while q:
            size = len(q)
            level += 1
            while size:
                node = q.popleft()
                if node.left is None and node.right is None:
                    flag = False
                    break
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                size -= 1

            if not flag:
                break    
        return level

