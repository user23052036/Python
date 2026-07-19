# 1448. Count Good Nodes in Binary Tree

"""
Given a binary tree root, a node X in the tree is named good if in the path from root to 
X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs_count_good(root,maxVal):
            if root is None:
                return 0

            res = 1 if root.val>=maxVal else 0 
            maxVal = max(maxVal,root.val)   
            
            left_tree = dfs_count_good(root.left,maxVal)
            right_tree = dfs_count_good(root.right,maxVal)
            return res+left_tree+right_tree
        
        return dfs_count_good(root,root.val)