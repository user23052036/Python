# 297. Serialize and Deserialize Binary Tree

"""
Serialization is the process of converting a data structure or object into a sequence of bits so that 
it can be stored in a file or memory buffer, or transmitted across a network connection link to be 
reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your 
serialization/deserialization algorithm should work. You just need to ensure that a 
binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. 
You do not necessarily need to follow this format, so please be creative and come up with different approaches 
yourself.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return ""
        
        queue = deque()
        result = ""
        queue.append(root)

        while queue:
            # level_size = len(queue)

            # while level_size:
            node = queue.popleft()
            if node is None:
                result += '#'+','
            else:
                result += str(node.val) + ','
                queue.append(node.left)
                queue.append(node.right)
            # level_size -= 1
        return result
            
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0:
            return None
        
        queue = deque()
        list_data = data.strip(',').split(',')
        root = TreeNode(int(list_data[0]))
        queue.append(root)

        counter = 1
        while queue and counter<len(list_data):
            node = queue.popleft()
            if list_data[counter] != '#':
                leftnode = TreeNode(int(list_data[counter]))
                queue.append(leftnode)
                node.left = leftnode
            else:
                node.left = None
            counter += 1
            

            if list_data[counter] != '#':
                rightnode = TreeNode(int(list_data[counter]))
                queue.append(rightnode)
                node.right = rightnode
            else:
                node.right = None
            counter += 1

        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))