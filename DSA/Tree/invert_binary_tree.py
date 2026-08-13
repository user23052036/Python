# 226. Invert Binary Tree


"""
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Input: root = [2,1,3]
Output: [2,3,1]

Input: root = []
Output: []
"""

from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        stack = deque()
        stack.append(root)

        while stack:
            node = stack.pop()
            # left pointer points to right and right pointer becomes left
            node.left,node.right = node.right,node.left

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return root


# Mistake:
# 1. Recursively invert the new root.left
# 2. Swap root.left and root.right
# 3. Recursively invert the new root.right

# I first inverted root.left and then swapped root.left and root.right.
# After swapping, the already-inverted left subtree becomes root.right.
# Then I call invertTree(root.right), which inverts that same subtree again.
# So it gets restored to its original form.
#

# Correct order:
# 1. Swap root.left and root.right
# 2. Recursively invert the new root.left
# 3. Recursively invert the new root.right


# first swap the pointer and recursively do it for the left and the right subtree
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        node = root.left
        root.left = root.right
        root.right = node

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
            