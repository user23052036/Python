# 102. Binary Tree Level Order Traversal

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
            
        queue = deque()
        queue.append(root)
        answer = []

        while queue:
            size = len(queue)
            level = []

            while size:
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                size -= 1
            answer.append(level)
        return answer
