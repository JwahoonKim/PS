# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer = []

        if root is None:
            return answer

        q = deque()
        q.append([root, 0])

        cur_level = 0
        cur_level_nodes = []
        while q:
            node, level = q.popleft()

            if level == cur_level:
                cur_level_nodes.append(node.val)
            else:
                answer.append(cur_level_nodes)
                cur_level += 1
                cur_level_nodes = [node.val]

            if node.left is not None:
                q.append([node.left, level + 1])
            if node.right is not None:
                q.append([node.right, level + 1])

        if cur_level_nodes:
            answer.append(cur_level_nodes)

        return answer

