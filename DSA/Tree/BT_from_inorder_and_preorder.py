# 105. Construct Binary Tree from Preorder and Inorder Traversal


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder)==0 or len(inorder)==0:
            return None
        
        node = TreeNode(preorder[0])
        indx = inorder.index(preorder[0])

        node.left = self.buildTree(preorder[1:indx+1], inorder[:indx])
        node.right = self.buildTree(preorder[indx+1:], inorder[indx+1:])
        return node