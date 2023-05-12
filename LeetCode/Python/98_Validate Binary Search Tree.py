# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValidBSTHelper(root, float('-inf'), float('inf'))

    def isValidBSTHelper(self, node, minVal, maxVal):
        if node is None:
            return True

        if node.val <= minVal or node.val >= maxVal:
            return False

        return self.isValidBSTHelper(node.left, minVal, node.val) and self.isValidBSTHelper(node.right, node.val, maxVal)