# 100. Same Tree


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def inorder_dfs(root1,root2):
            if root1 is None and root2 is None:
                return True
            if root1 is None or root2 is None:
                return False
            
            return (inorder_dfs(root1.left,root2.left) 
            and (root1.val == root2.val) 
            and inorder_dfs(root1.right,root2.right))
        
        return inorder_dfs(p,q)