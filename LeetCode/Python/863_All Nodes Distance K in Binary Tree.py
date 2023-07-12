# Definition for a binary tree node.
from collections import defaultdict, deque
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def initGraph(node, graph):
    if node is None:
        return

    if node.left is not None:
        graph[node.val].append(node.left.val)
        graph[node.left.val].append(node.val)
        initGraph(node.left, graph)

    if node.right is not None:
        graph[node.val].append(node.right.val)
        graph[node.right.val].append(node.val)
        initGraph(node.right, graph)


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        answer = []
        graph = defaultdict(list)
        initGraph(root, graph)

        visited = [False] * 501
        q = deque()
        q.append((target.val, 0))
        while q:
            nodeValue, dist = q.popleft()

            if visited[nodeValue]:
                continue
            visited[nodeValue] = True

            if dist == k:
                answer.append(nodeValue)

            for nextNodeValue in graph[nodeValue]:
                if not visited[nextNodeValue]:
                    q.append((nextNodeValue, dist + 1))

        return answer
