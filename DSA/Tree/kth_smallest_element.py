# 230. Kth Smallest Element in a BST

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []

        def inorder_traversal(root):
            if root is None:
                return
            
            inorder_traversal(root.left)
            arr.append(root.val)
            inorder_traversal(root.right)
        
        inorder_traversal(root)
        return arr[k-1]