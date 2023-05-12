from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def treeToList(node, result):
    if node is None:
        return

    treeToList(node.left, result)
    result.append(node.val)
    treeToList(node.right, result)


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = []
        treeToList(root, result)
        return result[k - 1]
