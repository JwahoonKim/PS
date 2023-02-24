from typing import List


class Solution:
    def maxJump(self, stones: List[int]) -> int:
        answer = stones[1] - stones[0]
        for i in range(len(stones) - 2):
            answer = max(answer, stones[i + 2] - stones[i])
        return answer