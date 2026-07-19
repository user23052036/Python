# 98. Validate Binary Search Tree

class Solution1:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root,lb,ub):
            if root is None:
                return True
            if root.val<=lb or root.val>=ub:
                return False

            bool1=True
            bool2=True
            if root.left:
                bool1 = helper(root.left,lb,root.val)
            if root.right:
                bool2 = helper(root.right,root.val,ub)
            
            if bool1 and bool2:
                return True
            return False
        
        return helper(root,float('-inf'),float('inf'))
    

class Solution2:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, lower, upper):
            if node is None:
                return True

            if not (lower < node.val < upper):
                return False

            return (
                validate(node.left, lower, node.val) and
                validate(node.right, node.val, upper)
            )

        return validate(root, float("-inf"), float("inf"))