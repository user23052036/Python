# 559. Maximum Depth of N-ary Tree


"""
Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Nary-Tree input serialization is represented in their level order traversal, each group of children is 
separated by the null value (See examples).


Input: root = [1,null,3,2,4,null,5,6]
Output: 3


Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: 5
"""


"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

from collections import deque
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        
        q = deque()
        q.append(root)
        level = 0

        while q:
            level += 1
            size = len(q)

            while size:
                node = q.popleft()
                for child in node.children:
                    q.append(child)
                size -= 1
        
        return level