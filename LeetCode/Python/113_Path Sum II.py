# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


answer = []


def isLeaf(node):
    return node.left is None and node.right is None


def helper(node, path, sum, targetSum):
    if node is None:
        return

    if isLeaf(node) and sum + node.val == targetSum:
        answer.append(path + [node.val])
        return

    helper(node.left, path + [node.val], sum + node.val, targetSum)
    helper(node.right, path + [node.val], sum + node.val, targetSum)


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        global answer
        answer = []
        helper(root, [], 0, targetSum)
        return answer
