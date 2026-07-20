# 543. Diameter of Binary Tree

class Solution1:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxi = 0
        def helper(root):
            if root is None:
                return 0
            
            left_length = helper(root.left)
            right_length = helper(root.right)

            if left_length+right_length > self.maxi:
                self.maxi = left_length+right_length
            return 1 + max(left_length,right_length)
        
        helper(root)
        return self.maxi
    


class Solution2:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def height(root):
            if root is None:
                return 0

            left_height = height(root.left)
            right_height = height(root.right)

            return 1+max(left_height, right_height)

        def diameter(root):     # func computes diameter
            if root is None:
                return 0
            
            left_height = height(root.left)
            right_height = height(root.right)

            curr_diameter = left_height+right_height

            left_diameter = diameter(root.left)
            right_diameter = diameter(root.right)

            return max(curr_diameter,left_diameter,right_diameter)
    
        return diameter(root)