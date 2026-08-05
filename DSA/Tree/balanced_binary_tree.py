# 110. Balanced Binary Tree


class Solution1:
    def height(self, root):
        if root is None:
            return 0

        left = self.height(root.left)
        right = self.height(root.right)

        return max(left,right)+1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        left_height = self.height(root.left)
        right_height = self.height(root.right)

        if abs(left_height - right_height) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)


class Solution2:
    def height(self, root):
        if root is None:
            return 0

        left = self.height(root.left)
        if left == -1:
            return -1

        right = self.height(root.right)
        if right == -1:
            return -1

        if abs(left - right) > 1:
            return -1
        return max(left, right) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.height(root) != -1