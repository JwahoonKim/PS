from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder_traverse(node, nums):
    if node is None:
        return

    inorder_traverse(node.left, nums)
    nums.append(node.val)
    inorder_traverse(node.right, nums)


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        nums = []
        inorder_traverse(root, nums)

        answer = 10 ** 5
        for i in range(len(nums) - 1):
            answer = min(abs(nums[i] - nums[i + 1]), answer)

        return answer



