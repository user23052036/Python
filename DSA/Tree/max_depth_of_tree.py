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