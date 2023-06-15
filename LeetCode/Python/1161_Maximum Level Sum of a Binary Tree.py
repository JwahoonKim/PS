from collections import defaultdict
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def calc(node, height, height_sum_dict):
    if node is None:
        return

    height_sum_dict[height] += node.val
    calc(node.left, height + 1, height_sum_dict)
    calc(node.right, height + 1, height_sum_dict)


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        height_sum_dict = defaultdict(int)
        calc(root, 1, height_sum_dict)

        answer = 0
        max_value = -10 ** 5
        for k, v in height_sum_dict.items():
            if v > max_value:
                answer = k
                max_value = v

        return answer