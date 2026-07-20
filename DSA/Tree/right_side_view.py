# 199. Binary Tree Right Side View

"""
Given the root of a binary tree, imagine yourself standing on the right side of it, 
return the values of the nodes you can see ordered from top to bottom.
"""

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
            
        queue = deque()
        queue.append(root)
        answer = []

        while queue:
            size = len(queue)
            temp = []
            while size:
                node = queue.popleft()
                temp.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                size -= 1
            answer.append(temp[-1])
        return answer