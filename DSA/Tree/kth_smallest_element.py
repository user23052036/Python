# 230. Kth Smallest Element in a BST

"""
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) 
of all the values of the nodes in the tree.


Input: root = [3,1,4,null,2], k = 1
Output: 1


Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
"""


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


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        def inorder(root):
            nonlocal count

            if root is None:
                return None
            
            left = inorder(root.left)
            if left is not None:
                return left

            count += 1
            if count == k:
                return root.val

            return inorder(root.right)
        
        return inorder(root)