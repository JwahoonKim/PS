# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def treeToList(node, result):
    if node is None:
        return

    result.append(node.val)
    treeToList(node.left, result)
    treeToList(node.right, result)


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        result = []
        treeToList(root, result)

        cur = root
        for i, v in enumerate(result):
            if i == len(result) - 1:
                cur.val = v
                cur.left = None
                cur.right = None
            else:
                cur.val = v
                cur.left = None
                cur.right = TreeNode()
                cur = cur.right
