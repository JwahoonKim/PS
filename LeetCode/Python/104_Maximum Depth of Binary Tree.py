from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def calcDepth(node):
    if node is None:
        return 0
    return 1 + max(calcDepth(node.left), calcDepth(node.right))


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return calcDepth(root)
