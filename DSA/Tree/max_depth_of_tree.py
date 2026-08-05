# 104. Maximum Depth of Binary Tree

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def calc_height(root):
            if root is None:
                return 0

            left_height = calc_height(root.left)
            right_height = calc_height(root.right)
            return 1+max(left_height,right_height)
        
        return calc_height(root)


"""
A useful pattern to remember
Many tree DP problems follow this template:
"""

def dfs(node):
    if not node:
        return base

    left = dfs(node.left)
    right = dfs(node.right)

    # Use children's answers to update a global result
    global_answer = ...

    # Return information needed by the parent
    return something_based_on(left, right)