# 572. Subtree of Another Tree

"""
Given the roots of two binary trees root and subRoot, return true if there is a subtree of 
root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of 
this node's descendants. The tree tree could also be considered as a subtree of itself.
"""

class Solution:
    def match(self,root,subRoot):
        if root is None and subRoot is None:
            return True
        if root is None or subRoot is None:
            return False
        
        if root.val != subRoot.val:
            return False
        return (self.match(root.left,subRoot.left) and
                self.match(root.right,subRoot.right))

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None and subRoot is None:
            return True
        if root is None or subRoot is None:
            return False
        
        if root.val==subRoot.val:
            if self.match(root,subRoot):
                return True

        return (self.isSubtree(root.left,subRoot) or
                self.isSubtree(root.right,subRoot))