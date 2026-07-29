# 235. Lowest Common Ancestor of a Binary Search Tree

"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between 
two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node 
to be a descendant of itself).”


Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.


Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself 
according to the LCA definition.


Input: root = [2,1], p = 2, q = 1
Output: 2
"""

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def inorder(root):
            if root is None:
                return None
            
            # case 1:
            # if both p and q lies in the different branch then the root will be the answer
            if ((p.val<=root.val and q.val>=root.val) or
                (p.val>=root.val and q.val<=root.val)):
                return root

            # case 2:
            # if both p and q lies in the same branch, move recursively
            if p.val<root.val:
                return inorder(root.left)
            else:
                return inorder(root.right)
        
        return inorder(root)