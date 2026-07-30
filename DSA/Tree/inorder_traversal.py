# 94. Binary Tree Inorder Traversal


# morris traversal
# tc -> O(2n)
# sc -> O(1)
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        curr = root
        result = []

        while curr:
            if curr.left:
                temp = curr.left
                while temp.right:
                    temp = temp.right

                temp.right = curr
                curr = curr.left
                temp.right.left = None
            
            else:
                result.append(curr.val)
                curr = curr.right
        
        return result


# tc -> O(n)
# sc -> O(n)
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def inorder(root):
            if root is None:
                return None

            inorder(root.left)
            ans.append(root.val)
            inorder(root.right)
        
        inorder(root)
        return ans