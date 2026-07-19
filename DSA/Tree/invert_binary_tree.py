# 226. Invert Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        stack = deque()
        stack.append(root)

        while stack:
            node = stack.pop()
            # left pointer points to right and right pointer becomes left
            node.left,node.right = node.right,node.left

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return root
            