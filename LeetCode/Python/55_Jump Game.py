from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        go = [False] * len(nums)
        go[0] = True
        max_go = 0

        for idx, step in enumerate(nums):
            if not go[idx]:
                continue

            for s in range(max_go + 1, idx + step + 1):
                if s >= len(nums):
                    break

                max_go = s
                go[s] = True

        return go[-1]


print(Solution().canJump([1,2,3]))