# 129. Sum Root to Leaf Numbers

"""
You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer 
will fit in a 32-bit integer.

A leaf node is a node with no children.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:       
        def helper_dfs(root,num):
            if root is None:
                return 0

            num = num*10+root.val
            if root.left is None and root.right is None:
                return num

            left_num = helper_dfs(root.left,num)
            right_num = helper_dfs(root.right,num)
            return left_num+right_num

        return helper_dfs(root,0)